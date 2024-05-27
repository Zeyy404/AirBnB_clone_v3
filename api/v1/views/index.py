#!/usr/bin/python3
"""Index module"""
from flask import jsonify
from . import app_views

@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
