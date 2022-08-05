import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from main_app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(String(), primary_key=True)
    name = Column(String(), nullable=True)
    password = Column(String(), nullable=True)
    cars = relationship(
        "CarModel", backref="car", cascade="all, delete-orphan", lazy="dynamic"
    )

    def __init__(self, name, password):
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.password = password

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password
        }
