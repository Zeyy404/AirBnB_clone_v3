#!/usr/bin/python3
"""Index module"""
from flask import jsonify
from . import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

object_classes = [
        ("amenities", Amenity),
        ("cities", City),
        ("places", Place),
        ("reviews", Review),
        ("states", State),
        ("users", User)
]


@app_views.route('/status', methods=['GET'])
def status():
    """retrieves response status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """retrieves the number of objects in a class"""
    stats = {name: storage.count(cls) for name, cls in object_classes}
    return jsonify(stats)
