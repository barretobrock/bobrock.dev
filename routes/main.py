from flask import render_template, Blueprint
from flask_babel import _ as BBL

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html', title=BBL('About'))


@main.route('/cv')
def cv():
    return render_template('cv.html', title=BBL('CV'))


@main.route('/projects')
def projects():
    return render_template('projects.html', title=BBL('Projects'))


@main.route('/contact')
def contact() -> str:
    return render_template('contact.html', title=BBL('Contact'))
