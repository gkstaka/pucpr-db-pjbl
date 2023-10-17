from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional
from services.database import session


class Psychologist(Base):
    __tablename__ = "psychologist"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Professional.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    crp: Mapped[str] = mapped_column("crp", VARCHAR(10), nullable=False, unique=True)
    professional: Mapped["Professional"] = relationship(back_populates="psychologists")

    def __init__(self, crp, professional):
        self.crp = crp
        self.professional = professional

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_crp(cls, crp):
        return session.query(cls).filter_by(crp=crp).first()
