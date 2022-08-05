from marshmallow import fields, Schema


class CarSchema(Schema):
    id = fields.String()
    object_id = fields.String()
    year = fields.Integer()
    make = fields.String()
    model_of_car = fields.String()
    category = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    owner_id = fields.Integer()


class CarQuerySchema(Schema):
    year = fields.String()
    make = fields.String()
    model = fields.String()
