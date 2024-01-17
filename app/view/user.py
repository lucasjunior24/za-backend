from typing import cast
from fastapi import APIRouter
from app.util.dtos.user import UserDTO
from app.db.models.user import User

user_router = APIRouter()

@user_router.get("/user", tags=["users"])
async def get_user(id: str):
    user = cast(User, User.objects(id=id).first())
    return user.to_json()

@user_router.get("/users", tags=["users"])
async def get_all_users():
    User.objects()
    users = [x.to_json() for x in User.objects()]
    return users



@user_router.post("/user", tags=["users"])
async def add_user(item: UserDTO):
    print(item.model_dump())
    new_user = User(**item.model_dump())
    new_user.save()
    return new_user.to_json()