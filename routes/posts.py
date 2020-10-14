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
    posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts, title='Blog')


@posts.route("/blog/<int:post_id>")
def post(post_id: float):
    """Loads specific blog post by ID"""
    post = Posts.query.get_or_404(post_id)
    return render_template('blog.html', title=post.title, post=post)


@posts.route("/blog/new", methods=('GET', 'POST'))
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/blog/<int:post_id>/update", methods=('GET', 'POST'))
@login_required
def update_post(post_id: float):
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/blog/<int:post_id>/delete", methods=('POST',))
@login_required
def delete_post(post_id: float) -> str:
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('routes.main'))
