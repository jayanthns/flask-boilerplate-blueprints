from flask import Blueprint, jsonify
from flask import request
from flask.views import MethodView

# from models.users import User
from apps.users.util import get_all_users

users_api_blueprint = Blueprint(
    'users_api', __name__,
)

@users_api_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "SUCCESS"}), 200
    print(request.method)
    data = request.get_json()
    print(get_all_users())
    return jsonify({"message": "SUCCESS"}), 200


class UserAPI(MethodView):
    def get(self):
        print(request)
        return jsonify({"message": "SUCCESS"}), 200

    def post(self):
        print(request.get_json())
        return jsonify({"message": "SUCCESS"}), 200

users_api_blueprint.add_url_rule('/allusers', view_func=UserAPI.as_view('allusers'))
