from flask import Blueprint

bp = Blueprint("simulation", __name__)

from app.simulation import routes
