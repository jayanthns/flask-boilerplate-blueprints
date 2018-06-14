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


class RegisterUserAPI(MethodView):

    def post(self):
        print(request.get_json())
        data = request.get_json()
        validated_data = validate_data(data, type="Register")
        print(validated_data)
        return jsonify({"message": "SUCCESS"}), 200


users_api_blueprint.add_url_rule('/register', view_func=RegisterUserAPI.as_view('register'))


def validate_data(data, type):
    validated_data = {"errors": None}
    if type == "Register":
        if not valid_email(data['email']):
            validated_data['errors']['email'] = "Entered email is not valid."
        if not valid_username(data['username']):
            validated_data['errors']['username'] = "Username is required."
        if not valid_passwords(data['password'], data['confirm_password']):
            validated_data['errors']['password'] = "Passwords are incorrect."
        return validated_data
