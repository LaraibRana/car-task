import asyncio

from flask import jsonify, request

from database import db
from db_models.user_model import UserModel
from tasks.tasks import get_car_details
from web.user_api import user_blueprint


@user_blueprint.route('/register', methods=['POST'])
def register_user():
    """
    This API call register a user
    """
    name = request.json["name"]
    password = request.json["password"]
    user = db.session.query(UserModel).filter_by(name=name).first()

    if user:
        return jsonify({
            "status": 409,
            "message": "User already in database"
        })

    user = UserModel(name=name, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_json())


@user_blueprint.route('/login', methods=['POST'])
def login_user():
    """
    This API call login a user
    """
    name = request.json["name"]
    password = request.json["password"]
    user = db.session.query(UserModel).filter_by(name=name, password=password).first()

    if not user:
        return jsonify({
            "status": 404,
            "message": "User not found in database"
        })

    asyncio.run(get_car_details(user_id=user.id))
    # get_car_details()
    return jsonify(user.to_json())


@user_blueprint.route('/check', methods=['GET'])
def check():
    return jsonify({
        "status": "happy"
    })
