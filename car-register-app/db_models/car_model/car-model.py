import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String

from main_app import db


class CarModel(db.Model):
    __tablename__ = 'cars'

    id = Column(String(), primary_key=True)
    name = Column(String(), nullable=True)
    object_id = Column(String(), nullable=True)
    year = Column(String(), nullable=True)
    make = Column(String(), nullable=True)
    model_of_car = Column(String(), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    user_id = Column(String(), ForeignKey("users.id"), nullable=False)

    def __init__(self, name, object_id, year, make, model_of_car, created_at, updated_at):
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.object_id = object_id
        self.year = year
        self.make = make
        self.model_of_car = model_of_car
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "object_id": self.object_id,
            "year": self.year,
            "make": self.make,
            "model_of_car": self.model_of_car,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
