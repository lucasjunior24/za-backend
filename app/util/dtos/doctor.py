from pydantic import BaseModel

class DoctorDTO(BaseModel):
    email: str
    name: str
    specialization: str
    clinic: str
    address: str
    phone_number: int


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