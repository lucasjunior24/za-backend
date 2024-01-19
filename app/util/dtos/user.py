from pydantic import BaseModel

class UserDTO(BaseModel):
    email: str
    name: str
    password: str


class UserResponseDTO(BaseModel):
    _id: str
    email: str
    name: str
    hashed_password: str
    disabled: bool
    admin: bool
    admin_master: bool
    created_at: str
    updated_at: str