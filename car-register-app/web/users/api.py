from apiflask import abort
from db_models.user_model import UserModel
from flask import jsonify

from main_app import db
from . import users_blueprint
from . import UserSchema


@users_blueprint.post('/register')
@input(UserSchema)
def register_user(data):
    """
    This API call register a user
    """
    name = data["name"]
    password = data["password"]
    user = UserModel(name=name, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        201
    })


@users_blueprint.post('/login')
@input(UserSchema)
def login_user(data):
    """
    This API call login a user
    """
    name = data["name"]
    password = data["password"]
    user = db.session.query(UserModel).filter_by(name=name, password=password).first()
    if not user:
        abort(404, "User not found in database")

    return jsonify(user.to_json())
