from flask import jsonify, url_for
import random

from app.simulation import bp


@bp.route("/")
def index():
    return jsonify(
        {
            "status": "Rocket offline",
            "location_url": url_for(".location")
        }
    )


@bp.route("/location")
def location():
    return jsonify(
        {
            "latitude": random.uniform(51, 52),
            "longitude": random.uniform(-2, -0.5)
        }
    )
