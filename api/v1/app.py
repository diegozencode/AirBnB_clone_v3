#!/usr/bin/python3
""" Script that loads a Flask instance """

from models import storage
from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown():
    """ function that calls close from storage """
    storage.close()

if __name__ == "__main__":
    """ iniciatizate the app by run """
    app.run(host="0.0.0.0", port="5000", threaded=True)