from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Patient, Treatment

class TreatmentTreatsDisorder(Base):
    __tablename__ = "treatment_treats_disorder"

    id: Mapped[int] = mapped_column("id", 
                                    MEDIUMINT, 
                                    nullable=False, 
                                    primary_key=True, 
                                    autoincrement=True)

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