from datetime import datetime

from sqlalchemy import ForeignKey, VARCHAR, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Patient, Doctor, Psychologist, Treatment, Medicine
from models.therapy import Therapy


class MedicalRecord(Base):
    __tablename__ = "medical_record"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)


    
    record_date: Mapped[str] = mapped_column("record_date",
                                             DATETIME,
                                             nullable=False,
                                             unique=False,
                                             default=datetime.now())

    description: Mapped[str] = mapped_column("description",
                                             VARCHAR(200),
                                             nullable=False,
                                             unique=False)

    patient_id: Mapped[int] = mapped_column("patient_id",
                                            MEDIUMINT,
                                            ForeignKey(Patient.id),
                                            nullable=False,
                                            unique=False)

    treatment_id: Mapped[int] = mapped_column("treatment_id",
                                              MEDIUMINT,
                                              ForeignKey(Treatment.id),
                                              nullable=False,
                                              unique=False)