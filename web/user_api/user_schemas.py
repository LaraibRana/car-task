from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    password = fields.String()
