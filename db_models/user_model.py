import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
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
