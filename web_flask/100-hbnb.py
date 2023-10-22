#!/usr/bin/python3
"""Flask web application listening on 0.0.0.0, port 5000"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask
from flask import render_template
from os import getenv

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def state():
    """Return a template with the listes of states and amenities places"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    owners = {
            place.id: users["User.{}".format(place.user_id)]
            for place in places}
    return render_template(
            '100-hbnb.html',
            states=states,
            amenities=amenities,
            owners=owners,
            places=places)


@app.teardown_appcontext
def teardown(_):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
