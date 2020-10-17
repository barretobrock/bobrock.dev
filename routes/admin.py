from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flask_babel import _ as BBL
# Internal packages
from flask_base import db
from models import Posts
from forms import PostForm

admin = Blueprint('admin', __name__)


@admin.route('/admin')
@login_required
def tables() -> str:
    """Main blog"""
    # Render buttons to tables
    tbls = db.metadata.tables.keys()
    return render_template('admin.html', tables=tbls, title=BBL('Admin'))




@admin.route('/admin/tbl/<string:tbl_name>')
@login_required
def render_table(tbl_name: str):
    page = request.args.get('page', 1, type=int)
    if tbl_name in db.metadata.tables.keys():
        # Begin rendering table
        model = get_model_by_tablename(tbl_name)
        results = model.query.paginate(page=page, per_page=20)
        return render_template('admin_table.html', results=results)
    else:
        flash(BBL(f'Table {tbl_name} not found. Please check the name and try again.'), 'alert-danger')
