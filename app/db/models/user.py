from mongoengine import *

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)
    password = StringField(max_length=50)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "email": self.email,
            "name": self.name,
        }