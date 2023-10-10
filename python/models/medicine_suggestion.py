from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT

from models import Base, Medicine, Dosage

class MedicineSuggestion(Base):
    __tablename__ = "medicine_suggestion"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    medicine_id: Mapped[int] = mapped_column("medicine_id",
                                             MEDIUMINT,
                                             ForeignKey(Medicine.id),
                                             nullable=False,
                                             unique=False)

    dosage_id: Mapped[int] = mapped_column("dosage_id",
                                            MEDIUMINT,
                                            ForeignKey(Dosage.id),
                                            nullable=False,
                                            unique=False)