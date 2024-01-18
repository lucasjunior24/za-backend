from typing import cast
from fastapi import APIRouter, Depends
from typing import Annotated

from app.util.dtos.user import UserDTO
from app.db.models.user import User
from app.view.login import get_password_hash, get_current_active_user


user_router = APIRouter()

@user_router.get("/users/{id}", tags=["users"])
async def get_user(id: str):
    user = cast(User, User.objects(id=id).first())
    return user.to_json()

@user_router.get("/user", tags=["users"])
async def get_user_by_email(email: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    user = cast(User, User.get_user_by_email(email))
    return user.to_json()

@user_router.get("/users", tags=["users"])
async def get_all_users():
    User.objects()
    users = [x.to_json() for x in User.objects()]
    return users



@user_router.post("/user", tags=["users"])
async def add_user(item: UserDTO):
    print(item.model_dump())

    hash = get_password_hash(item.password)
    new_user = User(email=item.email, name=item.name, hashed_password=hash)
    new_user.save()
    return new_user.to_json()