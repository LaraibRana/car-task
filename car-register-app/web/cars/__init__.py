from apiflask import APIBlueprint

cars_blueprint = APIBlueprint("cars", __name__)
from . import api
