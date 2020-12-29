from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/cv')
def cv():
    return render_template('cv.html', title='CV')


@main.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@main.route('/contact')
def contact() -> str:
    return render_template('contact.html', title='Contact')
