from application import db
from models.users import User

def get_all_users():
    return User.query.all()