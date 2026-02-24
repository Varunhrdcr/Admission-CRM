from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    intake = db.Column(db.Integer)


class SeatMatrix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer)
    quota = db.Column(db.String(50))
    total_seats = db.Column(db.Integer)
    filled_seats = db.Column(db.Integer, default=0)


class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    quota = db.Column(db.String(50))
    marks = db.Column(db.Float)
    document_status = db.Column(db.String(50), default="Pending")

class Admission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer)
    program_id = db.Column(db.Integer)
    quota = db.Column(db.String(50))
    admission_number = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(50), default="Allocated")
    fee_status = db.Column(db.String(50), default="Pending")