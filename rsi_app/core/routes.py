from flask import Blueprint, jsonify, request

core = Blueprint('core', __name__)

@core.route('/')
def home():
    return jsonify(status='Alive')