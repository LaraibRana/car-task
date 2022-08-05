from apiflask import APIBlueprint

users_blueprint = APIBlueprint("users", __name__)
from . import api
