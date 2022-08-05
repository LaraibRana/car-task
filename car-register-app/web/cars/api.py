from db_models.car_model import CarModel
from flask import jsonify

from main_app import db
from . import CarQuerySchema
from . import cars_blueprint


@cars_blueprint.get('/cars-list')
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


@cars_blueprint.get('/cars')
@input(CarQuerySchema)
def get_car(car_query):
    """
    Retrieves Cars data
    This requests retrieves all of car data
    """
    year = car_query['year']
    make = car_query['make']
    model = car_query['model']

    car = db.session.query(CarModel).filter_by(year=year, model=model, make=make).first()
    return car.to_json() if car else {}
