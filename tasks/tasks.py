import asyncio
import json

import requests

from database import db
from db_models.car_model import CarModel

headers = {
    'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
    'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
}


async def get_car_details(user_id=None):
    while True:
        url = f'https://parseapi.back4app.com/classes/Car_Model_List'
        response = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))
         # = request_data)
        for result in response['results']:
            object_id = str(result["objectId"])
            make = result["Make"]
            model_of_car = result["Model"]
            year = result["Year"]
            created_at = result["createdAt"]
            updated_at = result["updatedAt"]

            name = f"{object_id}_{make}_{model_of_car}_{year}"

            car = db.session.query(CarModel).filter_by(name=name, object_id=result["objectId"],
                                                       make=result["Make"], user_id=user_id).first()
            if car:
                continue

            car_obj = CarModel(
                name=name,
                object_id=object_id,
                year=year,
                make=make,
                model_of_car=model_of_car,
                created_at=created_at,
                updated_at=updated_at,
                user_id=user_id
            )
            db.session.add(car_obj)
            db.session.commit()

        await asyncio.sleep(1)

        print("The data has been added has in local database successfully")
