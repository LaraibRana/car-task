import json

import requests
from db_models.car_model import CarModel

from main_app import db

headers = {
    'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
    'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
}


def get_car_details():
    url = f'https://parseapi.back4app.com/classes/Car_Model_List'
    request_data = requests.get(url, headers=headers).content.decode('utf-8')
    response = json.loads(request_data)
    for result in response['results']:
        car_obj = CarModel(
            object_id=result['objectId'],
            year=result['Year'],
            make=result['Make'],
            model_of_car=result['Model'],
            category=result['Category'],
            created_at=result['createdAt'],
            updated_at=result['updatedAt'],
        )
        db.session.add(car_obj)
        db.session.commit()

    print("The data has been added has in local database successfully")
