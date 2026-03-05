from database import db
from datetime import datetime

class Citizen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name_nep = db.Column(db.String(200))
    full_name_eng = db.Column(db.String(200))
    dob = db.Column(db.String(50))
    gender = db.Column(db.String(20))

    province = db.Column(db.String(100))
    district = db.Column(db.String(100))
    municipality = db.Column(db.String(100))
    ward = db.Column(db.Integer)

    citizenship_number = db.Column(db.String(50), unique=True)
    issued_district = db.Column(db.String(100))

    father_name = db.Column(db.String(200))
    mother_name = db.Column(db.String(200))

    mobile = db.Column(db.String(20))
    password = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    constituency = db.Column(db.String(200))
    status = db.Column(db.String(50))


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    party = db.Column(db.String(200))
    election_id = db.Column(db.Integer)


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer)
    candidate_id = db.Column(db.Integer)
    election_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200))
    level = db.Column(db.String(200))
    description = db.Column(db.Text)
    file_path = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
