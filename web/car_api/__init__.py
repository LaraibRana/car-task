from flask import Blueprint

car_blueprint = Blueprint('car_blueprint', __name__)

from . import car_api
