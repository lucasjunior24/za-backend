from typing import cast
from fastapi import APIRouter, Depends
from typing import Annotated

from app.db.models.doctor import Doctor
from app.db.models.user import User
from app.util.dtos.doctor import DoctorResponseDTO, DoctorDTO
from app.view.login import get_current_active_user
from fastapi.middleware.cors import CORSMiddleware


doctor_router = APIRouter()


@doctor_router.get("/doctors/{id}", tags=["doctors"])
async def get_doctor(id: str):
    doctor = cast(Doctor, Doctor.objects(id=id).first())
    return doctor.to_json()


@doctor_router.get("/doctors/{name}/name", tags=["doctors"])
async def get_doctors_by_name(name: str):
    doctors = [x.to_json() for x in Doctor.objects(name=name)]
    return doctors


@doctor_router.get("/doctors/{email}/email", tags=["doctors"], response_model=list[DoctorResponseDTO])
async def get_doctor_by_email(email: str):
    doctor = Doctor.get_doctor_by_email(email)
    return doctor.to_json()


@doctor_router.get("/doctors", tags=["doctors"], response_model=list[DoctorResponseDTO])
async def get_all_doctors():
    Doctor.objects()
    doctors = [x.to_json() for x in Doctor.objects()]
    return doctors


@doctor_router.post("/doctors", tags=["doctors"], response_model=DoctorResponseDTO) 
async def add_doctor(item: DoctorDTO):
    new_doctor = Doctor(email=item.email, name=item.name, specialization=item.specialization, clinic=item.clinic, address=item.address, phone_number=item.phone_number)
    new_doctor.save()
    return new_doctor.to_json()