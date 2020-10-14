from flask import render_template, Blueprint
from flask_babel import _

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html', title=_('About'))


@main.route('/cv')
def cv():
    return render_template('cv.html', title=_('CV'))


@main.route('/projects')
def projects():
    return render_template('projects.html', title=_('Projects'))


@main.route('/contact')
def contact() -> str:
    return render_template('contact.html', title=_('Contact'))
