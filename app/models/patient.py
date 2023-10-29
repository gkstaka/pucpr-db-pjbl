from datetime import datetime, date
from typing import List

from sqlalchemy import ForeignKey, VARCHAR, CHAR, DATE, FLOAT, DATETIME, func, literal_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship, aliased

from models import Base, Person
from services.database import session


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Person.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    weight: Mapped[float] = mapped_column("weight", FLOAT, nullable=False, unique=False)
    marital_status: Mapped[str] = mapped_column(
        "marital_status", VARCHAR(200), nullable=False, unique=False
    )
    profession: Mapped[str] = mapped_column(
        "profession", VARCHAR(200), nullable=False, unique=False
    )
    emergency_contact_name: Mapped[str] = mapped_column(
        "emergency_contact_name", VARCHAR(200), nullable=False, unique=False
    )
    emergency_contact_phone: Mapped[str] = mapped_column(
        "emergency_contact_phone", VARCHAR(14), nullable=False, unique=False
    )
    health_insurance: Mapped[str] = mapped_column(
        "health_insurance", VARCHAR(50), nullable=False, unique=False
    )
    hospitalization_date: Mapped[date] = mapped_column(
        "hospitalization_date",
        DATETIME,
        nullable=False,
        unique=False,
        default=datetime.now(),
    )
    person: Mapped["Person"] = relationship(back_populates="patients")
    consultations: Mapped[List["Consultation"]] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )
    treatment: Mapped["Treatment"] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )

    medical_record: Mapped["MedicalRecord"] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        weight,
        marital_status,
        profession,
        emergency_contact_name,
        emergency_contact_phone,
        health_insurance,
        hospitalization_date,
        person,
        **kw
    ):
        super().__init__(**kw)
        self.weight = weight
        self.marital_status = marital_status
        self.profession = profession
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.health_insurance = health_insurance
        self.hospitalization_date = hospitalization_date
        self.person = person

    @classmethod
    def find_by_weight(cls, weight):
        return session.query(cls).filter_by(weight=weight).all()

    @classmethod
    def find_by_marital_status(cls, marital_status):
        return session.query(cls).filter_by(marital_status=marital_status).all()

    @classmethod
    def find_by_profession(cls, profession):
        return session.query(cls).filter_by(profession=profession).all()

    @classmethod
    def find_by_emergency_contact_name(cls, emergency_contact_name):
        return (
            session.query(cls)
            .filter_by(emergency_contact_name=emergency_contact_name)
            .all()
        )

    @classmethod
    def find_by_emergency_contact_phone(cls, emergency_contact_phone):
        return (
            session.query(cls)
            .filter_by(emergency_contact_phone=emergency_contact_phone)
            .all()
        )

    @classmethod
    def find_by_health_insurance(cls, health_insurance):
        return session.query(cls).filter_by(health_insurance=health_insurance).all()

    @classmethod
    def find_by_hospitalization_date(cls, hospitalization_date):
        return (
            session.query(cls)
            .filter_by(hospitalization_date=hospitalization_date)
            .all()
        )

    @classmethod
    def save_all(cls, patients):
        session.add_all(patients)
        session.commit()

    @classmethod
    def save(cls, patient):
        session.add(patient)
        session.commit()

    @classmethod
    def count_patients(cls):
        return session.query(func.count(cls.id)).scalar()

    def __str__(self):
        return (
            f"Patient: {self.id}, {self.weight}, {self.marital_status}, {self.profession}, {self.emergency_contact_name}, " + 
            f"{self.emergency_contact_phone}, {self.health_insurance}, {self.hospitalization_date}"
        )

    @classmethod
    def hospitalization_date_monthly(cls):
        query = (
            session.query(
                func.count(cls.id),
                func.extract("month", cls.hospitalization_date).label("month"),
            )
            .group_by(func.extract("month", cls.hospitalization_date))
            .order_by(func.extract("month", cls.hospitalization_date))
        )
        return query.all()
        

    @classmethod
    def prefferd_doctor_sex(cls):
        from models import Person, Consultation, Doctor
        doctor_person = aliased(Person)
        query = (
            session.query(Person.sex.label("Patient sex"), doctor_person.sex.label("Doctor sex"), func.count().label("Total"))
            .join(Patient, Patient.id == Person.id)
            .join(Consultation, Consultation.patient_id == Patient.id)
            .join(Doctor, Doctor.id == Consultation.doctor_id)
            .join(doctor_person, Doctor.id == doctor_person.id)
            .group_by(Person.sex, doctor_person.sex)
            .order_by(Person.sex)
        )

        return query.all()

    @classmethod
    def preffered_psychologist_sex(cls):
        from models import Person, Treatment, PsychologistHelpsTreatment, Psychologist
        psychologist_person = aliased(Person)
        query = (
            session.query(Person.sex.label("Patient sex"), psychologist_person.sex.label("Psychologist sex"), func.count().label(""))
            .join(cls, cls.id == Person.id)
            .join(Treatment, Treatment.patient_id == Person.id)
            .join(
                PsychologistHelpsTreatment,
                PsychologistHelpsTreatment.treatment_id == Treatment.id,
            )
            .join(
                Psychologist, PsychologistHelpsTreatment.psychologist_id == Psychologist.id
            )
            .join(psychologist_person, Psychologist.id == psychologist_person.id)
            .group_by(Person.sex, psychologist_person.sex)
            .order_by(Person.sex)
        )
        return query.all()

    @classmethod
    def list_linked_professionals(cls):
        from models import Person, Treatment, PsychologistHelpsTreatment, Psychologist, Doctor, DoctorSuggestTreatment
        doctor_person = aliased(Person)
        psychologist_person = aliased(Person)

        doctor_query = (
            session.query(
                Person.id.label("ID paciente"),
                Person.name.label("Patient name"),
                Doctor.id.label("ID profissional"),
                doctor_person.name.label("Professional name"),
                literal_column("'Doctor'").label("Professional type") 
                )
            .join(Patient, Patient.id == Person.id)
            .join(Treatment, Treatment.patient_id == Patient.id)
            .join(
                DoctorSuggestTreatment, DoctorSuggestTreatment.treatment_id == Treatment.id
            )
            .join(Doctor, Doctor.id == DoctorSuggestTreatment.doctor_id)
            .join(doctor_person, Doctor.id == doctor_person.id)  
            
        )

        psychologist_query = (
            session.query(
                Person.id.label("ID paciente"),
                Person.name.label("Patient name"),
                Psychologist.id.label("ID profissional"),
                psychologist_person.name.label("Professional name"),
                literal_column("'Psychologist'").label("Professional type") 
                )
            .join(Patient, Patient.id == Person.id)
            .join(Treatment, Treatment.patient_id == Patient.id)
            .join(
                PsychologistHelpsTreatment, PsychologistHelpsTreatment.treatment_id == Treatment.id
            )
            .join(Psychologist, Psychologist.id == PsychologistHelpsTreatment.psychologist_id)
            .join(psychologist_person, Psychologist.id == psychologist_person.id)  
            
        )

        return doctor_query.union(psychologist_query).all()
        
        # query = (
        #     session.query(
        #         Person.id.label("ID paciente"),
        #         Person.name.label("Nome"),
        #         Doctor.id.label("ID médico"),
        #         literal_column("'Médico'").label("Médico"), 
        #         Psychologist.id.label("Id psicólogo"),
        #         literal_column("'Psicólogo'").label("Psicólogo"),  
        #     )
        #     .join(Patient, Patient.id == Person.id)
        #     .join(Treatment, Treatment.patient_id == Patient.id)
        #     .outerjoin(
        #         DoctorSuggestTreatment, DoctorSuggestTreatment.treatment_id == Treatment.id
        #     )
        #     .join(Doctor, Doctor.id == DoctorSuggestTreatment.doctor_id)
        #     .join(doctor_person, Doctor.id == doctor_person.id)  #
        #     .outerjoin(
        #         PsychologistHelpsTreatment,
        #         PsychologistHelpsTreatment.treatment_id == Treatment.id,
        #     )
        #     .join(
        #         Psychologist, Psychologist.id == PsychologistHelpsTreatment.psychologist_id
        #     )
        #     .join(psychologist_person, Psychologist.id == psychologist_person.id)  
        # )"

    @classmethod
    def count_marital_status(cls):
        query = session.query(cls.marital_status, func.count().label("Count")).group_by(
            cls.marital_status
        )

        return query.all()
