from typing import cast
from mongoengine import *

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)
    hashed_password = StringField(max_length=100)
    disabled = BooleanField(default=False)
    admin = BooleanField(default=False)
    admin_master = BooleanField(default=False)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "email": self.email,
            "name": self.name,
            "hashed_password": self.hashed_password,
            "disabled": self.disabled,
            "admin": self.admin,
            "admin_master": self.admin_master,
        }
    
    @classmethod
    def get_user_by_email(cls, email: str):
        user = cast(User, cls.objects(email=email).first())
        return user