from flask import Blueprint,render_template

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def hello_pybo():
    return render_template('finder/find_map.html')

@bp.route('/hello')
def test_hello():
    return 'hello'