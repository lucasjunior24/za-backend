from typing import Annotated
from fastapi import Form
from pydantic import BaseModel

class DoctorDTO(BaseModel):
    email:  Annotated[str, Form()]
    name: Annotated[str, Form()]
    specialization: Annotated[str, Form()]
    clinic: Annotated[str, Form()]
    address: Annotated[str, Form()]
    phone_number: Annotated[int, Form()]


class DoctorResponseDTO(BaseModel):
    id: str
    email: str
    name: str
    specialization: str
    clinic: str
    address: str
    phone_number: int
    created_at: str
    updated_at: str