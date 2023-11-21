from flask import session
from app.main import bp

@bp.route('/')
def index():
    if 'loggedin' in session:
        return 'Your loggedin as ' + session["username"] + ' <a href="/logout">Logout</a>'
    return 'Portal Apps ' + ' <a href="/login">Login</a>'