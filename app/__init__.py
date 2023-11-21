from flask import Flask, redirect, url_for, session

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.addons.faba import bp as faba_bp
    app.register_blueprint(faba_bp, url_prefix="/faba")

    @app.route("/login")
    def login():
        session["loggedin"] = True
        session["username"] = "admin"
        return redirect(url_for("main.index"))
    
    @app.route("/logout")
    def logout():
        session.pop("loggedin", None)
        session.pop("username", None)

        return redirect(url_for("main.index"))

    return app