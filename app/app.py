from datetime import datetime

from models import (
    Person,
    Professional,
    Patient,
    Doctor,
    Psychologist,
    Consultation,
    Medicine,
)
from services.database import session
from utils.database_utils import create_db

from sqlalchemy import select


def create_people():
    people = [
        Person(
            name="Bruno Miglioretto",
            cpf="06411448908",
            birth_date="2013-02-01",
            sex="m",
            zip="70040912",
            street="Rua dos santos",
            street_number=12,
            complement="APT 239",
            neighborhood="Boa vista",
            city="Curitiba",
            state="PR",
            country="BRL",
            phone="+5541996438691",
            email="bruno@exemple.com",
        ),
        Person(
            name="João da Silva",
            cpf="31076567045",
            birth_date=datetime.strptime("1985-07-15", "%Y-%m-%d").date(),
            sex="m",
            zip="74120080",
            street="Rua 18",
            street_number=12,
            complement=None,
            neighborhood="Boa vista",
            city="Curitiba",
            state="PR",
            country="BRL",
            phone="+5541396438691",
            email="joao@exemple.com",
        ),
        Person(
            name="John Smith",
            cpf="98765432109",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="m",
            zip="543210",
            street="Maple Avenue",
            street_number=30,
            complement="Suite 101",
            neighborhood="Downtown",
            city="Metropolis",
            state="CA",
            country="USA",
            phone="+5122334455",
            email="john@example.com",
        ),
        Person(
            name="Maria Garcia",
            cpf="34567891234",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="f",
            zip="654321",
            street="Oak Street",
            street_number=55,
            complement="",
            neighborhood="West End",
            city="Riverside",
            state="CA",
            country="USA",
            phone="+1987654321",
            email="maria@example.com",
        ),
        Person(
            name="Luis Rodriguez",
            cpf="78901234567",
            birth_date=datetime.strptime("1992-11-10", "%Y-%m-%d").date(),
            sex="m",
            zip="987654",
            street="Pine Street",
            street_number=88,
            complement="APT 305",
            neighborhood="East Side",
            city="Springfield",
            state="IL",
            country="USA",
            phone="+1654321879",
            email="luis@example.com",
        ),
        Person(
            name="Sophia Johnson",
            cpf="56789012345",
            birth_date=datetime.strptime("1982-05-30", "%Y-%m-%d").date(),
            sex="f",
            zip="234567",
            street="Cedar Lane",
            street_number=18,
            complement="",
            neighborhood="North End",
            city="Hill Valley",
            state="CA",
            country="USA",
            phone="+1555123456",
            email="sophia@example.com",
        ),
        Person(
            name="Eva Johnson",
            cpf="98765432100",
            birth_date=datetime.strptime("1982-05-30", "%Y-%m-%d").date(),
            sex="f",
            zip="543210",
            street="Willow Street",
            street_number=22,
            complement="Suite 301",
            neighborhood="Downtown",
            city="Metropolis",
            state="CA",
            country="USA",
            phone="+1112334455",
            email="eva@example.com",
        ),
        Person(
            name="Daniel Brown",
            cpf="11122334455",
            birth_date=datetime.strptime("1995-09-02", "%Y-%m-%d").date(),
            sex="m",
            zip="332211",
            street="Chestnut Avenue",
            street_number=45,
            complement="",
            neighborhood="West End",
            city="Riverside",
            state="CA",
            country="USA",
            phone="+1987614321",
            email="daniel@example.com",
        ),
        Person(
            name="Sophie Miller",
            cpf="22233445566",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="f",
            zip="998877",
            street="Magnolia Street",
            street_number=78,
            complement="APT 205",
            neighborhood="East Side",
            city="Springfield",
            state="IL",
            country="USA",
            phone="+1614321879",
            email="sophie@example.com",
        ),
        Person(
            name="William Clark",
            cpf="33344556677",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="m",
            zip="112233",
            street="Maple Lane",
            street_number=13,
            complement="",
            neighborhood="North End",
            city="Hill Valley",
            state="CA",
            country="USA",
            phone="+1555113456",
            email="william@example.com",
        ),
        Person(
            name="Ava Baker",
            cpf="44455667788",
            birth_date="2013-02-01",
            sex="f",
            zip="334455",
            street="Pine Drive",
            street_number=36,
            complement="",
            neighborhood="South Side",
            city="Springfield",
            state="IL",
            country="USA",
            phone="+1444333222",
            email="ava@example.com",
        ),
        Person(
            name="Liam Wilson",
            cpf="55566677788",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="m",
            zip="123456",
            street="Sunset Boulevard",
            street_number=99,
            complement="Suite 501",
            neighborhood="Hollywood Hills",
            city="Los Angeles",
            state="CA",
            country="USA",
            phone="+1122334455",
            email="liam@example.com",
        ),
        Person(
            name="Emma Davis",
            cpf="66677788899",
            birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
            sex="f",
            zip="654321",
            street="Ocean Avenue",
            street_number=11,
            complement="",
            neighborhood="Beachfront",
            city="Santa Monica",
            state="CA",
            country="USA",
            phone="+6987654321",
            email="emma@example.com",
        ),
        Person(
            name="Noah Martinez",
            cpf="77788899900",
            birth_date=datetime.strptime("1992-11-10", "%Y-%m-%d").date(),
            sex="f",
            zip="112233",
            street="Palm Street",
            street_number=22,
            complement="APT 102",
            neighborhood="Palm Beach",
            city="Miami",
            state="FL",
            country="USA",
            phone="+1654321829",
            email="noah@example.com",
        ),
        Person(
            name="Olivia Taylor",
            cpf="88899900011",
            birth_date=datetime.strptime("1982-05-30", "%Y-%m-%d").date(),
            sex="f",
            zip="334455",
            street="Grove Avenue",
            street_number=55,
            complement="",
            neighborhood="Green Park",
            city="Orlando",
            state="FL",
            country="USA",
            phone="+1555123156",
            email="olivia@example.com",
        ),
        Person(
            name="James Johnson",
            cpf="99900011222",
            birth_date=datetime.strptime("1992-11-10", "%Y-%m-%d").date(),
            sex="m",
            zip="998877",
            street="Hillside Drive",
            street_number=77,
            complement="Suite 303",
            neighborhood="Hilltop",
            city="Tampa",
            state="FL",
            country="USA",
            phone="+1444333252",
            email="james@example.com",
        ),
        Person(
            name="Isabella Brown",
            cpf="00011122233",
            birth_date=datetime.strptime("1985-07-15", "%Y-%m-%d").date(),
            sex="f",
            zip="223344",
            street="Forest Road",
            street_number=33,
            complement="",
            neighborhood="Woodland",
            city="Jacksonville",
            state="FL",
            country="USA",
            phone="+1888777666",
            email="isabella@example.com",
        ),
        Person(
            name="Sophia Hernandez",
            cpf="11223341156",
            birth_date=datetime.strptime("1992-11-10", "%Y-%m-%d").date(),
            sex="f",
            zip="223344",
            street="Oak Street",
            street_number=99,
            complement="APT 401",
            neighborhood="Downtown",
            city="Metropolis",
            state="CA",
            country="USA",
            phone="+1111134455",
            email="sophiaa@example.com",
        ),
    ]

    session.add_all(people)


def create_professionals():
    stmt = select(Person)
    people = [person for person in session.scalars(stmt)][:12]

    professionals = [
        Professional(
            enrollment="AKDFJKKKD",
            salary=10000,
            start_date=datetime.now(),
            working_range="Junior",
            speciality="Cardio",
            consultation_fee=80,
            person=people[0],
        ),
        Professional(
            enrollment="JKLFJSDFE",
            salary=12000,
            start_date=datetime.now(),
            working_range="Senior",
            speciality="Neurology",
            consultation_fee=100,
            person=people[1],
        ),
        Professional(
            enrollment="IODFJNSDF",
            salary=9500,
            start_date=datetime.now(),
            working_range="Mid-Level",
            speciality="Dermatology",
            consultation_fee=90,
            person=people[2],
        ),
        Professional(
            enrollment="ALSKDFJSD",
            salary=11000,
            start_date=datetime.now(),
            working_range="Junior",
            speciality="Oncology",
            consultation_fee=85,
            person=people[3],
        ),
        Professional(
            enrollment="POIUERLKJ",
            salary=11500,
            start_date=datetime.now(),
            working_range="Senior",
            speciality="Orthopedics",
            consultation_fee=110,
            person=people[4],
        ),
        Professional(
            enrollment="QWERTYUIO",
            salary=10500,
            start_date=datetime.now(),
            working_range="Mid-Level",
            speciality="Gynecology",
            consultation_fee=95,
            person=people[5],
        ),
        Professional(
            enrollment="KDFJNSDF1",
            salary=9500,
            start_date=datetime.now(),
            working_range="Junior",
            speciality="Pediatrics",
            consultation_fee=85,
            person=people[6],
        ),
        Professional(
            enrollment="DFJNSKDF2",
            salary=11000,
            start_date=datetime.now(),
            working_range="Senior",
            speciality="Ophthalmology",
            consultation_fee=90,
            person=people[7],
        ),
        Professional(
            enrollment="KJDFNSDF3",
            salary=10500,
            start_date=datetime.now(),
            working_range="Mid-Level",
            speciality="Dentistry",
            consultation_fee=80,
            person=people[8],
        ),
        Professional(
            enrollment="KJDFNSDF4",
            salary=10000,
            start_date=datetime.now(),
            working_range="Junior",
            speciality="Psychiatry",
            consultation_fee=95,
            person=people[9],
        ),
        Professional(
            enrollment="SKDFNSDF5",
            salary=11500,
            start_date=datetime.now(),
            working_range="Senior",
            speciality="Gastroenterology",
            consultation_fee=100,
            person=people[10],
        ),
        Professional(
            enrollment="KJDFNSDF6",
            salary=9800,
            start_date=datetime.now(),
            working_range="Mid-Level",
            speciality="Dermatology",
            consultation_fee=88,
            person=people[11],
        ),
    ]

    session.add_all(professionals)


def create_patients():
    stmt = select(Person)
    people = [person for person in session.scalars(stmt)][12:18]

    patients = [
        Patient(
            weight=56,
            marital_status="single",
            profession="Programmer",
            emergency_contact_name="Alice",
            emergency_contact_phone="390809384",
            health_insurance="Unimed",
            hospitalization_date="2023-10-03",
            person=people[0],
        ),
        Patient(
            weight=70,
            marital_status="married",
            profession="Teacher",
            emergency_contact_name="John",
            emergency_contact_phone="123456789",
            health_insurance="BlueCross",
            hospitalization_date=datetime.strptime("2023-09-20", "%Y-%m-%d").date(),
            person=people[1],
        ),
        Patient(
            weight=85,
            marital_status="divorced",
            profession="Doctor",
            emergency_contact_name="Sarah",
            emergency_contact_phone="987654321",
            health_insurance="Aetna",
            hospitalization_date=datetime.strptime("2023-11-05", "%Y-%m-%d").date(),
            person=people[2],
        ),
        Patient(
            weight=62,
            marital_status="single",
            profession="Engineer",
            emergency_contact_name="Michael",
            emergency_contact_phone="555123456",
            health_insurance="Cigna",
            hospitalization_date=datetime.strptime("2023-10-15", "%Y-%m-%d").date(),
            person=people[3],
        ),
        Patient(
            weight=75,
            marital_status="married",
            profession="Nurse",
            emergency_contact_name="Emily",
            emergency_contact_phone="678987654",
            health_insurance="Humana",
            hospitalization_date=datetime.strptime("2023-09-10", "%Y-%m-%d").date(),
            person=people[4],
        ),
        Patient(
            weight=68,
            marital_status="single",
            profession="Artist",
            emergency_contact_name="Oliver",
            emergency_contact_phone="9122334455",
            health_insurance="Kaiser",
            hospitalization_date=datetime.strptime("2023-10-25", "%Y-%m-%d").date(),
            person=people[5],
        ),
    ]

    session.add_all(patients)


def create_doctors():
    stmt = select(Professional)
    professionals = [professional for professional in session.scalars(stmt)][0:6]

    doctors = [
        Doctor(
            crm="39489",
            professional=professionals[0],
        ),
        Doctor(
            crm="340809",
            professional=professionals[1],
        ),
        Doctor(
            crm="20398",
            professional=professionals[2],
        ),
        Doctor(
            crm="32322311",
            professional=professionals[3],
        ),
        Doctor(
            crm="3948939",
            professional=professionals[4],
        ),
        Doctor(
            crm="39489999",
            professional=professionals[5],
        ),
    ]

    session.add_all(doctors)


def create_psychologists():
    stmt = select(Professional)
    professionals = [professional for professional in session.scalars(stmt)][6:12]

    psychologists = [
        Psychologist(
            crp="0as9d8f9",
            professional=professionals[0],
        ),
        Psychologist(
            crp="asdf90909",
            professional=professionals[1],
        ),
        Psychologist(
            crp="98sd7f897",
            professional=professionals[2],
        ),
        Psychologist(
            crp="asdf976",
            professional=professionals[3],
        ),
        Psychologist(
            crp="23498dgfs",
            professional=professionals[4],
        ),
        Psychologist(
            crp="0as1d8f9",
            professional=professionals[5],
        ),
    ]

    session.add_all(psychologists)


def create_consultations():
    stmt = select(Patient)
    patients = [patient for patient in session.scalars(stmt)]

    consultations = [
        Consultation(
            time=datetime.strptime("2022-07-15", "%Y-%m-%d").date(),
            patient=patients[0],
        ),
        Consultation(
            time=datetime.strptime("2023-05-15", "%Y-%m-%d").date(),
            patient=patients[1],
        ),
        Consultation(
            time=datetime.strptime("2023-09-15", "%Y-%m-%d").date(),
            patient=patients[2],
        ),
        Consultation(
            time=datetime.strptime("2021-05-01", "%Y-%m-%d").date(),
            patient=patients[3],
        ),
        Consultation(
            time=datetime.strptime("2022-03-10", "%Y-%m-%d").date(),
            patient=patients[4],
        ),
        Consultation(
            time=datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
            patient=patients[5],
        ),
    ]

    session.add_all(consultations)


def create_medicines():
    medicines = [
        Medicine(
            name="Paracetamol",
            composition="Magnesium stearate, cellulose, docusate sodium and sodium benzoate or sodium lauryl sulfate, starch, hydroxypropyl methylcellulose, propylene glycol",
            usage_type="Oral use",
            indication="Adults",
            contraindication="Kids",
        ),
        Medicine(
            name="Ibuprofen",
            composition="Croscarmellose sodium, colloidal silicon dioxide, hypromellose, iron oxide, polyethylene glycol",
            usage_type="Oral use",
            indication="Pain relief, fever reduction, anti-inflammatory",
            contraindication="Patients with a history of allergic reactions to aspirin or NSAIDs",
        ),
        Medicine(
            name="Amoxicillin",
            composition="Colloidal silicon dioxide, polyethylene glycol, starch, sodium lauryl sulfate, titanium dioxide",
            usage_type="Oral use",
            indication="Bacterial infections",
            contraindication="Patients with a history of allergic reactions to penicillin",
        ),
        Medicine(
            name="Omeprazole",
            composition="Crospovidone, hypromellose, magnesium stearate, mannitol, sodium lauryl sulfate",
            usage_type="Oral use",
            indication="Gastric acid reduction",
            contraindication="Patients with hypersensitivity to proton pump inhibitors",
        ),
        Medicine(
            name="Loratadine",
            composition="Calcium phosphate, lactose, magnesium stearate, corn starch",
            usage_type="Oral use",
            indication="Allergy relief",
            contraindication="Patients with severe kidney disorders",
        ),
        Medicine(
            name="Aspirin",
            composition="Corn starch, hypromellose, powdered cellulose, triacetin",
            usage_type="Oral use",
            indication="Pain relief, fever reduction, anti-inflammatory",
            contraindication="Patients with a history of bleeding disorders",
        ),
    ]

    session.add_all(medicines)


if __name__ == "__main__":
    print("Creating database...")
    create_db()

    create_people()
    create_professionals()
    create_patients()
    create_doctors()
    create_psychologists()
    create_consultations()
    create_medicines()

    # Todo:
    # create_dosages()
    # create_suggestions()
    # create_medical_record()

    session.commit()
