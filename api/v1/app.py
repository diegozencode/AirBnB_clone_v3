#!/usr/bin/python3
""" Script that loads a Flask instance """

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ function that calls close from storage """
    storage.close()


@app.errorhandler(404)
def handle_not_found(exception):
    """handle 404 error not found"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    """ iniciatizate the app by run """
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', '5000'))
