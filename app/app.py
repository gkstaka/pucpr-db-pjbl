from datetime import datetime

from sqlalchemy import func, text, literal_column
from sqlalchemy.orm import aliased

from models import (
    Person,
    Professional,
    Patient,
    Doctor,
    Psychologist,
    Consultation,
    Medicine,
    Dosage,
    MedicalRecord,
    Disorder,
    Treatment,
    Therapy,
    Suggestion,
    DoctorSuggestTreatment,
    DoctorUpdateRecord,
    MedicalRecordIncludedTherapy,
    PsychologistHelpsTreatment,
    PsychologistUpdateRecord,
    TreatmentTreatsDisorder,
)
from services.database import session
from utils.database_utils import create_db


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

    Person.save_all(people)


def create_professionals():
    people = Person.find_all()[:12]

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

    Professional.save_all(professionals)


def create_patients():
    people = Person.find_all()[12:18]

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

    Patient.save_all(patients)


def create_doctors():
    professionals = Professional.find_all()[0:6]

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

    Doctor.save_all(doctors)


def create_psychologists():
    professionals = Professional.find_all()[6:12]

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

    Psychologist.save_all(psychologists)


def create_consultations():
    patients = Patient.find_all()
    doctors = Doctor.find_all()
    consultations = [
        Consultation(
            time=datetime.strptime("2022-07-15", "%Y-%m-%d").date(),
            patient=patients[0],
            doctor=doctors[0],
        ),
        Consultation(
            time=datetime.strptime("2023-05-15", "%Y-%m-%d").date(),
            patient=patients[1],
            doctor=doctors[1],
        ),
        Consultation(
            time=datetime.strptime("2023-09-15", "%Y-%m-%d").date(),
            patient=patients[2],
            doctor=doctors[2],
        ),
        Consultation(
            time=datetime.strptime("2021-05-01", "%Y-%m-%d").date(),
            patient=patients[3],
            doctor=doctors[3],
        ),
        Consultation(
            time=datetime.strptime("2022-03-10", "%Y-%m-%d").date(),
            patient=patients[4],
            doctor=doctors[4],
        ),
        Consultation(
            time=datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
            patient=patients[5],
            doctor=doctors[5],
        ),
    ]

    Consultation.save_all(consultations)


def create_disorders():
    disorder_list = [
        Disorder(
            name="Anxiety",
            category="Anxiety disorders",
            symptoms="Excessive worry, restlessness, fatigue, difficulty concentrating, irritability, sleep problems",
            risk_factors="Trauma, stress due to an illness, stress buildup, personality",
            prevalence=0.89,
        ),
        Disorder(
            name="Depression",
            category="Mood disorders",
            symptoms="Sadness, loss of interest, feelings of guilt or low self-worth, disturbed sleep or appetite, tiredness, poor concentration",
            risk_factors="Childhood trauma, other mental disorders, abuse of alcohol or recreational drugs, personal problems, poverty or isolation",
            prevalence=0.76,
        ),
        Disorder(
            name="Bipolar disorder",
            category="Mood disorders",
            symptoms="Mood changes, elevated mood, high energy, sleep problems, loss of appetite, psychosis",
            risk_factors="Genetic, environmental, brain structure and function",
            prevalence=0.35,
        ),
        Disorder(
            name="Schizophrenia",
            category="Psychotic disorders",
            symptoms="Delusions, hallucinations, disorganized thinking, lack of motivation, speaking little",
            risk_factors="Genetic, environmental, brain chemistry, substance abuse",
            prevalence=0.01,
        ),
        Disorder(
            name="Autism",
            category="Neurodevelopmental disorders",
            symptoms="Difficulty with communication and interaction with other people, restricted interests and repetitive behaviors",
            risk_factors="Genetic, environmental",
            prevalence=0.12,
        ),
        Disorder(
            name="ADHD",
            category="Neurodevelopmental disorders",
            symptoms="Difficulty paying attention, hyperactivity, impulsivity",
            risk_factors="Genetic, environmental",
            prevalence=0.06,
        ),
    ]

    Disorder.save_all(disorder_list)


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

    Medicine.save_all(medicines)


def create_dosages():
    dosages = [
        Dosage(
            dose_quantity=30,
            dose_frequency=400,
        ),
        Dosage(
            dose_quantity=10,
            dose_frequency=40,
        ),
        Dosage(
            dose_quantity=300,
            dose_frequency=90,
        ),
        Dosage(
            dose_quantity=20,
            dose_frequency=300,
        ),
        Dosage(
            dose_quantity=220,
            dose_frequency=10,
        ),
        Dosage(
            dose_quantity=30,
            dose_frequency=300,
        ),
    ]

    Dosage.save_all(dosages)


def create_treatments():
    patient_list = Patient.find_all()

    treatments = [
        Treatment(
            name="Anxiety treatment",
            start_date=datetime.strptime("2022-07-15", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2023-07-15", "%Y-%m-%d").date(),
            patient=patient_list[0],
        ),
        Treatment(
            name="Depression treatment",
            start_date=datetime.strptime("2023-05-15", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2024-05-15", "%Y-%m-%d").date(),
            patient=patient_list[1],
        ),
        Treatment(
            name="Bipolar disorder treatment",
            start_date=datetime.strptime("2023-09-15", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2024-09-15", "%Y-%m-%d").date(),
            patient=patient_list[2],
        ),
        Treatment(
            name="Schizophrenia treatment",
            start_date=datetime.strptime("2021-05-01", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2022-05-01", "%Y-%m-%d").date(),
            patient=patient_list[3],
        ),
        Treatment(
            name="Autism treatment",
            start_date=datetime.strptime("2022-03-10", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2023-03-10", "%Y-%m-%d").date(),
            patient=patient_list[4],
        ),
        Treatment(
            name="ADHD treatment",
            start_date=datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
            planned_end_date=datetime.strptime("2021-01-01", "%Y-%m-%d").date(),
            patient=patient_list[5],
        ),
    ]

    Treatment.save_all(treatments)


def create_therapies():
    psychologists = Psychologist.find_all()

    therapy_list = [
        Therapy(
            time=datetime.strptime("01:00:00", "%H:%M:%S"),
            purpose="Cognitive behavioral therapy (CBT) is a form of psychological treatment.",
            capacity=1,
            psychologist=psychologists[0],
        ),
        Therapy(
            time=datetime.strptime("02:00:00", "%H:%M:%S"),
            purpose="Dialectical behavior therapy (DBT) is a specific type of cognitive-behavioral psychotherapy.",
            capacity=1,
            psychologist=psychologists[1],
        ),
        Therapy(
            time=datetime.strptime("03:00:00", "%H:%M:%S"),
            purpose="Interpersonal therapy (IPT) is a time-limited treatment.",
            capacity=1,
            psychologist=psychologists[2],
        ),
        Therapy(
            time=datetime.strptime("04:00:00", "%H:%M:%S"),
            purpose="Psychodynamic therapy is a form of therapy with a focus on a holistic perspective of the client.",
            capacity=1,
            psychologist=psychologists[3],
        ),
        Therapy(
            time=datetime.strptime("05:00:00", "%H:%M:%S"),
            purpose="Family therapy is a type of psychological counseling (psychotherapy) that helps family members.",
            capacity=1,
            psychologist=psychologists[4],
        ),
        Therapy(
            time=datetime.strptime("06:00:00", "%H:%M:%S"),
            purpose="Couple therapy is a type of psychological therapy that helps couples of all types.",
            capacity=2,
            psychologist=psychologists[5],
        ),
    ]

    Therapy.save_all(therapy_list)


def create_medical_record():
    patient_list = Patient.find_all()
    treatment_list = Treatment.find_all()

    medical_records = [
        MedicalRecord(
            patient=patient_list[0],
            treatment=treatment_list[0],
            record_date=datetime.strptime("2022-07-15", "%Y-%m-%d").date(),
            description="Patient is suffering from anxiety disorder",
        ),
        MedicalRecord(
            patient=patient_list[1],
            treatment=treatment_list[1],
            record_date=datetime.strptime("2023-05-15", "%Y-%m-%d").date(),
            description="Patient is suffering from depression",
        ),
        MedicalRecord(
            patient=patient_list[2],
            treatment=treatment_list[2],
            record_date=datetime.strptime("2023-09-15", "%Y-%m-%d").date(),
            description="Patient is suffering from bipolar disorder",
        ),
        MedicalRecord(
            patient=patient_list[3],
            treatment=treatment_list[3],
            record_date=datetime.strptime("2021-05-01", "%Y-%m-%d").date(),
            description="Patient is suffering from schizophrenia",
        ),
        MedicalRecord(
            patient=patient_list[4],
            treatment=treatment_list[4],
            record_date=datetime.strptime("2022-03-10", "%Y-%m-%d").date(),
            description="Patient is suffering from autism",
        ),
        MedicalRecord(
            patient=patient_list[5],
            treatment=treatment_list[5],
            record_date=datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
            description="Patient is suffering from ADHD",
        ),
    ]

    MedicalRecord.save_all(medical_records)


def create_suggestions():
    medicines = Medicine.find_all()
    dosage_list = Dosage.find_all()
    medical_records = MedicalRecord.find_all()

    suggestion_list = []
    for index in range(0, len(medicines)):
        suggestion_list.append(
            Suggestion(
                medicine_id=medicines[index].id,
                dosage_id=dosage_list[index].id,
                medical_record_id=medical_records[index].id,
            )
        )

    Suggestion.save_all(suggestion_list)


def create_doctor_suggest_treatment():
    doctor_list = Doctor.find_all()
    treatment_list = Treatment.find_all()

    doctor_suggest_treatment_list = []
    for index in range(0, len(doctor_list)):
        doctor_suggest_treatment_list.append(
            DoctorSuggestTreatment(
                doctor=doctor_list[index], treatment=treatment_list[index]
            )
        )

    DoctorSuggestTreatment.save_all(doctor_suggest_treatment_list)


def create_doctor_update_record():
    doctor_list = Doctor.find_all()
    medical_records = MedicalRecord.find_all()

    doctor_update_record_list = []
    for index in range(0, len(doctor_list)):
        doctor_update_record_list.append(
            DoctorUpdateRecord(
                doctor=doctor_list[index], medical_record=medical_records[index]
            )
        )

    DoctorUpdateRecord.save_all(doctor_update_record_list)


def create_medical_record_included_therapy():
    medical_records = MedicalRecord.find_all()
    therapy_list = Therapy.find_all()

    medical_record_included_therapy_list = []
    for index in range(0, len(medical_records)):
        medical_record_included_therapy_list.append(
            MedicalRecordIncludedTherapy(
                medical_record=medical_records[index], therapy=therapy_list[index]
            )
        )

    MedicalRecordIncludedTherapy.save_all(medical_record_included_therapy_list)


def create_psychologist_helps_treatment():
    psychologists = Psychologist.find_all()
    treatment_list = Treatment.find_all()

    psychologist_helps_treatment_list = []
    for index in range(0, len(psychologists)):
        psychologist_helps_treatment_list.append(
            PsychologistHelpsTreatment(
                psychologist=psychologists[index], treatment=treatment_list[index]
            )
        )

    PsychologistHelpsTreatment.save_all(psychologist_helps_treatment_list)


def create_psychologist_update_record():
    psychologists = Psychologist.find_all()
    medical_records = MedicalRecord.find_all()

    psychologist_update_record_list = []
    for index in range(0, len(psychologists)):
        psychologist_update_record_list.append(
            PsychologistUpdateRecord(
                psychologist=psychologists[index], medical_record=medical_records[index]
            )
        )

    PsychologistUpdateRecord.save_all(psychologist_update_record_list)


def create_treatment_treats_disorder():
    disorder_list = Disorder.find_all()
    treatment_list = Treatment.find_all()

    treatment_treats_disorder_list = []
    for index in range(0, len(treatment_list)):
        treatment_treats_disorder_list.append(
            TreatmentTreatsDisorder(
                disorder=disorder_list[index],
                treatment=treatment_list[index],
            )
        )

    TreatmentTreatsDisorder.save_all(treatment_treats_disorder_list)


def query_1():
    print("1. Contar quantidade total de pacientes atendidos")
    patients = Patient.find_all()
    print(patients)


def query_2():
    print("2. Contar quantidade total de consultas realizadas")
    consultations = Consultation.find_all()
    print(consultations)


def query_3():
    print("3. Contar a quantidade de total terapias realizadas")
    therapies = Therapy.find_all()
    print(therapies)


def query_4():
    print("4. Listar todos os tratamentos em andamento")
    treatments = Treatment.find_all()
    current_treatments = []
    for treatment in treatments:
        if treatment.planned_end_date > datetime.now():
            current_treatments.append(treatment)
    print(current_treatments)


def query_5():
    print("5. Listar profissionais por ordem de salário")
    professionals = Professional.find_all()
    sorted_professionals = sorted(professionals, key=lambda x: getattr(x, "salary"))
    print(sorted_professionals)


def query_6():
    d = aliased(Disorder)
    ttd = aliased(TreatmentTreatsDisorder)
    t = aliased(Treatment)

    query = (
        session.query(
            d.name.label("Disorder name"), func.count(t.id).label("Treatments count")
        )
        .join(ttd, ttd.disorder_id == d.id)
        .join(t, t.id == ttd.treatment_id)
        .group_by(d.name)
    )

    results = query.all()
    print(results)


def query_7():
    # subquery = (
    #     session.query(Suggestion.medicine_id, func.count().label("count")).select_from(Suggestion).group_by(Suggestion.medicine_id).subquery()
    # )

    # query = (
    #     session.query(
    #         subquery.c["count"]
    #         / func.count(MedicalRecord.id).label("Average medication per patient")
    #     )
    #     .join(MedicalRecord, MedicalRecord.id == subquery.c["medicine_id"])
    #     .group_by(subquery.c["count"])
    # )

    query = (
        session.query(
            (func.count(Suggestion.id) / func.count(MedicalRecord.id)).label("Average medication taken")
        )
        .join(MedicalRecord, MedicalRecord.id == Suggestion.medical_record_id)
    )

    results = query.all()
    print(results)


def query_8():
    query = (
        session.query(
            func.count(Patient.id),
            func.extract("month", Patient.hospitalization_date).label("month"),
        )
        .group_by(func.extract("month", Patient.hospitalization_date))
        .order_by(func.extract("month", Patient.hospitalization_date))
    )

    results = query.all()
    print(results)


def query_9():
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

    results = query.all()
    print(results)


def query_10():
    psychologist_person = aliased(Person)

    query = (
        session.query(Person.sex.label("Patient sex"), psychologist_person.sex.label("Psychologist sex"), func.count().label(""))
        .join(Patient, Patient.id == Person.id)
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

    results = query.all()
    print(results)


def query_11():
    query = session.query(Disorder).order_by(Disorder.prevalence.desc())

    results = query.all()
    print(results)


def query_12():
    doctor_person = aliased(Person)
    psychologist_person = aliased(Person)
    
    query = (
        session.query(
            Person.id.label("ID paciente"),
            Person.name.label("Nome"),
            Doctor.id.label("ID médico"),
            literal_column("'Médico'").label("Médico"), 
            Psychologist.id.label("Id psicólogo"),
            literal_column("'Psicólogo'").label("Psicólogo"),  
        )
        .join(Patient, Patient.id == Person.id)
        .join(Treatment, Treatment.patient_id == Patient.id)
        .outerjoin(
            DoctorSuggestTreatment, DoctorSuggestTreatment.treatment_id == Treatment.id
        )
        .join(Doctor, Doctor.id == DoctorSuggestTreatment.doctor_id)
        .join(doctor_person, Doctor.id == doctor_person.id)  #
        .outerjoin(
            PsychologistHelpsTreatment,
            PsychologistHelpsTreatment.treatment_id == Treatment.id,
        )
        .join(
            Psychologist, Psychologist.id == PsychologistHelpsTreatment.psychologist_id
        )
        .join(psychologist_person, Psychologist.id == psychologist_person.id)  
    )

    results = query.all()
    print(results)


def query_13():
    query = (
        session.query(
            Disorder.name,
            func.avg(
                func.datediff(Treatment.planned_end_date, Treatment.start_date)
            ).label("Average time"),
        )
        .join(
            TreatmentTreatsDisorder,
            TreatmentTreatsDisorder.treatment_id == Treatment.id,
        )
        .join(Disorder, TreatmentTreatsDisorder.disorder_id == Disorder.id)
        .group_by(Disorder.name)
    )

    results = query.all()
    print(results)


def query_14():
    current_datetime = datetime.now()

    query = (
        session.query(
            Disorder.name.label("Transtorno"),
            func.count(Treatment.id).label("quantidade"),
        )
        .join(
            TreatmentTreatsDisorder,
            TreatmentTreatsDisorder.treatment_id == Treatment.id,
        )
        .join(Disorder, TreatmentTreatsDisorder.disorder_id == Disorder.id)
        .filter(current_datetime < Treatment.planned_end_date)
        .group_by(Disorder.name)
    )

    results = query.all()
    print(results)


def query_15():
    query = session.query(
        Professional.speciality, func.count().label("Quantity")
    ).group_by(Professional.speciality)

    results = query.all()
    print(results)


def query_16():
    psychologist_alias = aliased(Person)

    query = (
        session.query(
            psychologist_alias.name.label("Psychologist name"), Person.name.label("Patient name")
        )
        .join(Patient, Patient.id == Person.id)
        .join(Treatment, Treatment.patient_id == Patient.id)
        .join(
            PsychologistHelpsTreatment,
            PsychologistHelpsTreatment.treatment_id == Treatment.id,
        )
        .join(
            Psychologist, PsychologistHelpsTreatment.psychologist_id == Psychologist.id
        )
        .join(psychologist_alias, Psychologist.id == psychologist_alias.id)
        .order_by(psychologist_alias.name)
    )

    results = query.all()
    print(results)

    results = query.all()
    print(results)


def query_17():
    query = session.query(Patient.marital_status, func.count().label("Count")).group_by(
        Patient.marital_status
    )

    results = query.all()
    print(results)


def query_18():
    query = (
        session.query(
            Person.name.label("Name"),
            func.count(DoctorUpdateRecord.id).label("Medical records updated"),
        )
        .join(Doctor, Doctor.id == DoctorUpdateRecord.doctor_id)
        .join(Professional, Professional.id == Doctor.id)
        .join(Person, Person.id == Professional.id)
        .group_by(Doctor.id)
        .order_by(func.count(DoctorUpdateRecord.id).desc())
    )

    results = query.all()
    print(results)


def query_19():
    query = (
        session.query(
            Person.name.label("Nome do Psicólogo"),
            func.count(PsychologistUpdateRecord.id).label("Quantidade de Atualizações"),
        )
        .join(Professional, Professional.id == Person.id) 
        .join(Psychologist, Psychologist.id == Person.id) 
        .join(
            PsychologistUpdateRecord, 
            Psychologist.id == PsychologistUpdateRecord.psychologist_id
        )  
        .group_by(Person.name)
        .order_by(func.count(PsychologistUpdateRecord.id).desc())
    )

    results = query.all()
    print(results)


def query_20():
    query = (
    session.query(
            Person.name, func.count(Consultation.id).label("Consultation stats")
        )
        .join(Professional, Professional.id == Person.id)  # Joining with Professional using Person's ID
        .join(Doctor, Doctor.id == Person.id)  # Joining with Doctor using Person's ID
        .join(Consultation, Consultation.doctor_id == Doctor.id)  # Joining with Consultation using Doctor's ID
        .group_by(Person.name)
        .limit(1)
    )

    result = query.first()
    print(result)


if __name__ == "__main__":
    print("Creating database...")
    
    # create_db()
    
    # create_people()
    # create_patients()
    
    # create_professionals()
    # create_doctors()
    # create_psychologists()
    
    # create_consultations()
    # create_disorders()
    # create_dosages()
    # create_medicines()
    # create_treatments()
    # create_therapies()
    # create_medical_record()
    # create_suggestions()
    
    # create_doctor_suggest_treatment()
    # create_doctor_update_record()
    # create_medical_record_included_therapy()
    # create_psychologist_helps_treatment()
    # create_psychologist_update_record()
    # create_treatment_treats_disorder()

    query_1()
    query_2()
    query_3()
    query_4()
    query_5()
    query_6()
    query_7()
    query_8()
    query_9()
    query_10()
    query_11()
    query_12()
    query_13()
    query_14()
    query_15()
    query_16()
    query_17()
    query_18()
    query_19()
    query_20()

    session.close()
#
# total_patients = count_total_patients()
# print(f"Total de pacientes atendidos: {total_patients}")
#
# total_consultations = count_total_consultations()
# print(f"Total de consultas realizadas: {total_consultations}")
#
# total_therapies = count_total_therapies()
# print(f"Total de terapias realizadas: {total_therapies}")
#
#
# for treatment in ongoing_treatments:
#     print(f"ID: {treatment.id}, Nome: {treatment.name}, Data de Término: {treatment.end_date}")
#
#
# for professional in professionals:
#     print(f"ID: {professional.id}, Nome: {professional.name}, Salário: {professional.salary}")
#
#
# for name, count in results:
#     print(f"Transtorno: {name}, Quantidade de Pacientes: {count}")
#
#
# average_medicines_per_patient = calculate_average_medicines_per_patient()
# print(f"Média de medicamentos por paciente: {average_medicines_per_patient}")
#
#
# for row in results:
#     patient_sex = row.patient_sex
#     doctor_sex = row.doctor_sex
#     consultation_count = row.consultation_count
#     print(f"Paciente Sexo: {patient_sex}, Médico Sexo: {doctor_sex}, Número de Consultas: {consultation_count}")
#
#
# for symptom, occurrences in results:
#     print(f"Sintoma: {symptom}, Ocorrências: {occurrences}")
#
#
# results = get_currently_treated_disorders()
#
# if results:
#     print("Transtornos atualmente em tratamento:")
#     for disorder in results:
#         print(disorder.name)
# else:
#     print("Nenhum transtorno está sendo tratado atualmente.")
#
#
# for specialization, count in results:
#     print(f"Especialização: {specialization}, Número de Profissionais: {count}")
