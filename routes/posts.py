from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
# Internal packages
from flask_base import db
from models import Posts
from forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/blog')
def blog() -> str:
    """Main blog"""
    page = request.args.get('page', 1, type=int)
    posts_to_fetch = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts_to_fetch, title='Blog')


@posts.route("/blog/<int:post_id>")
def post(post_id: float):
    """Loads specific blog post by ID"""
    post_to_fetch = Posts.query.get_or_404(post_id)
    return render_template('blog/post.html', title=post_to_fetch.title, post=post_to_fetch)


@posts.route("/blog/new", methods=('GET', 'POST'))
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post_data = Posts(lang=form.lang.data, title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post_data)
        db.session.commit()
        flash('Your post has been created!', 'alert-success')
        return redirect(url_for('posts.post', post_id=post_data.id))
    return render_template('blog/create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/blog/<int:post_id>/update", methods=('GET', 'POST'))
@login_required
def update_post(post_id: float):
    post_to_update = Posts.query.get_or_404(post_id)
    if post_to_update.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_to_update.title = form.title.data
        post_to_update.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'alert-success')
        return redirect(url_for('posts.post', post_id=post_to_update.id))
    elif request.method == 'GET':
        form.title.data = post_to_update.title
        form.content.data = post_to_update.content
    return render_template('blog/create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/blog/<int:post_id>/delete", methods=('POST',))
@login_required
def delete_post(post_id: float) -> str:
    post_to_delete = Posts.query.get_or_404(post_id)
    if post_to_delete.author != current_user:
        abort(403)
    db.session.delete(post_to_delete)
    db.session.commit()
    flash('Your post has been deleted!', 'alert-success')
    return redirect(url_for('posts.blog'))
