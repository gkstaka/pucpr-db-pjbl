from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Doctor, MedicalRecord

class DoctorUpdateRecord(Base):
    __tablename__ = "doctor_update_record"

    id: Mapped[int] = mapped_column("id", 
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    doctor_id: Mapped[int] = mapped_column("doctor_id", 
                                           MEDIUMINT, 
                                           ForeignKey(Doctor.id), 
                                           nullable=False,
                                           unique=False)

    medical_record_id: Mapped[int] = mapped_column("medical_record_id", 
                                                   MEDIUMINT, 
                                                   ForeignKey(MedicalRecord.id), 
                                                   nullable=False, 
                                                   unique=False)