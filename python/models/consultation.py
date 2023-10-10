from datetime import datetime

from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Doctor, Patient


class Consultation(Base):
    __tablename__ = "consultation"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    time: Mapped[str] = mapped_column("time",
                                      DATETIME,
                                      nullable=False,
                                      unique=False,
                                      default=datetime.now())

    patient_id: Mapped[int] = mapped_column("patient_id",
                                            MEDIUMINT,
                                            ForeignKey(Patient.id),
                                            nullable=False,
                                            unique=False)

    doctor_id: Mapped[int] = mapped_column("doctor_id",
                                           MEDIUMINT,
                                           ForeignKey(Doctor.id),
                                           nullable=False,
                                           unique=False)
