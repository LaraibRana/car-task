from flask import jsonify

from database import db
from db_models.car_model import CarModel
from web.car_api import car_blueprint


@car_blueprint.route('/cars-list', methods=['GET'])
def list_cars_data():
    """
    List Cars data
    This requests list all of car data
    """
    cars_list = []
    cars_data = db.session.query(CarModel).all()
    for car in cars_data:
        cars_list.append(car.to_json())

    return jsonify(cars_list)


@car_blueprint.route('/cars', methods=['GET'])
def get_car(car_query):
    """
    Retrieves Cars data
    This requests retrieves all of car data
    """
    year = car_query['year']
    make = car_query['make']
    model = car_query['model']

    car = db.session.query(CarModel).filter_by(year=year, model=model, make=make).first()
    return jsonify(car.to_json() if car else {})
