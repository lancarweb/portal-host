from flask import Blueprint

bp = Blueprint("faba", __name__)

from app.addons.faba import routes