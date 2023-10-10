from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, MedicalRecord, Therapy

class MedicalRecordIncludedTherapy:
    __tablename__ = "medical_record_included_therapy"

    id: Mapped[int] = mapped_column("id", 
                                    MEDIUMINT, 
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    medical_record_id: Mapped[int] = mapped_column("medical_record_id", 
                                                   MEDIUMINT, 
                                                   ForeignKey(MedicalRecord.id), 
                                                   nullable=False, 
                                                   unique=False)

    therapy_id: Mapped[int] = mapped_column("therapy_id", 
                                            MEDIUMINT, 
                                            ForeignKey(Therapy.id), 
                                            nullable=False, 
                                            unique=False)

    