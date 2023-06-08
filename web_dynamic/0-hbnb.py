#!/usr/bin/python3
"""Starts a Flash Web Application"""
from flask import Flask, render_template
from models import *
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """HBNB Route"""
    states = storage.all('State').values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all('Place').values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)