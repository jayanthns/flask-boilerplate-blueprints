from flask import Blueprint, jsonify
from flask import request

from models.users import User

users_blueprint = Blueprint(
    'users', __name__,
    # template_folder='templates',
    # static_folder='static',
    # static_url_path='/static'
)

@users_blueprint.route('/')
def index():
    if request:
        print("HELLO")
    return jsonify({"message": "SUCCESS"})