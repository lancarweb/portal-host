from flask import render_template, redirect, url_for, request, session
from app.addons.faba import bp
from app.models.faba_model import Post
from app.extensions import db

@bp.route("/")
def index():
    if 'loggedin' in session:
        results = Post.query.all()
        return render_template("faba/index.html", content=results)

    return redirect(url_for('main.index'))

@bp.route("/transporter")
def transporter():
    if 'loggedin' in session:
        return render_template("faba/transporter.html")
    
    return redirect(url_for('main.index'))

@bp.route("/post", methods=["GET", "POST"])
def post():
    if 'loggedin' in session:
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
            
            # commit
            content_post = Post(title=title, content=content)
            db.session.add(content_post)
            db.session.commit()

        return redirect(url_for('faba.index'))
    
    return redirect(url_for('main.index')) 