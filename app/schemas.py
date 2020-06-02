from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    phone = fields.String()
    username = fields.String()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
