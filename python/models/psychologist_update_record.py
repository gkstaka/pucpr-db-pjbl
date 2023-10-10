from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, MedicalRecord, Psychologist

class PsychologistUpdateRecord(Base):
    __tablename__ = "psychologist_update_record"

    id: Mapped[int] = mapped_column("id", 
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    psychologist_id: Mapped[int] = mapped_column("psychologist_id", 
                                               MEDIUMINT, 
                                               ForeignKey(Psychologist.id), 
                                               nullable=False,
                                               unique=False)

    medical_record_id: Mapped[int] = mapped_column("medical_record_id", 
                                                   MEDIUMINT, 
                                                   ForeignKey(MedicalRecord.id), 
                                                   nullable=False, 
                                                   unique=False)