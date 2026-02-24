from flask import Blueprint, request, jsonify
from models import db, Institution, Department, Program, SeatMatrix, Applicant, Admission

routes = Blueprint("routes", __name__)

@routes.route("/test")
def test():
    return "Routes working"

@routes.route("/institution", methods=["POST"])
def create_institution():
    data = request.json
    inst = Institution(name=data["name"])
    db.session.add(inst)
    db.session.commit()
    return jsonify({"msg": "Institution created"})

@routes.route("/program", methods=["POST"])
def create_program():
    data = request.json
    prog = Program(name=data["name"], intake=data["intake"])
    db.session.add(prog)
    db.session.commit()
    return jsonify({"msg": "Program created"})


@routes.route("/seat", methods=["POST"])
def create_seat():
    data = request.json
    seat = SeatMatrix(
        program_id=data["program_id"],
        quota=data["quota"],
        total_seats=data["total_seats"],
    )
    db.session.add(seat)
    db.session.commit()
    return jsonify({"msg": "Seat matrix created"})


@routes.route("/applicant", methods=["POST"])
def create_applicant():
    data = request.json
    app = Applicant(
        name=data["name"],
        category=data["category"],
        quota=data["quota"],
        marks=data["marks"],
    )
    db.session.add(app)
    db.session.commit()
    return jsonify({"msg": "Applicant created"})

@routes.route("/allocate", methods=["POST"])
def allocate_seat():
    data = request.json

    applicant_id = data["applicant_id"]
    program_id = data["program_id"]
    quota = data["quota"]

    # Step 1 — find seat matrix
    seat = SeatMatrix.query.filter_by(program_id=program_id, quota=quota).first()

    if not seat:
        return jsonify({"error": "Seat matrix not found"}), 400

    # Step 2 — check availability
    if seat.filled_seats >= seat.total_seats:
        return jsonify({"error": "Quota full"}), 400

    # Step 3 — increment seat counter
    seat.filled_seats += 1

    # Step 4 — create admission record
    admission = Admission(
        applicant_id=applicant_id,
        program_id=program_id,
        quota=quota
    )

    db.session.add(admission)
    db.session.commit()

    return jsonify({"msg": "Seat allocated"})

@routes.route("/fee/<int:admission_id>", methods=["PUT"])
def update_fee(admission_id):
    admission = Admission.query.get(admission_id)

    if not admission:
        return jsonify({"error": "Admission not found"}), 404

    admission.fee_status = "Paid"
    db.session.commit()

    return jsonify({"msg": "Fee updated"})


@routes.route("/confirm/<int:admission_id>", methods=["PUT"])
def confirm_admission(admission_id):
    admission = Admission.query.get(admission_id)

    if not admission:
        return jsonify({"error": "Admission not found"}), 404

    if admission.fee_status != "Paid":
        return jsonify({"error": "Fee pending"}), 400

    # Generate admission number
    admission.admission_number = f"INST/2026/UG/{admission.program_id}/{admission.quota}/{admission.id:04d}"
    admission.status = "Confirmed"

    db.session.commit()

    return jsonify({"msg": "Admission confirmed", "admission_number": admission.admission_number})

@routes.route("/dashboard")
def dashboard():

    # Total intake
    total_intake = db.session.query(db.func.sum(Program.intake)).scalar() or 0

    # Total admitted
    total_admitted = Admission.query.count()

    return jsonify({
        "total_intake": total_intake,
        "total_admitted": total_admitted
    })

@routes.route("/quota-status")
def quota_status():
    seats = SeatMatrix.query.all()

    result = []
    for s in seats:
        result.append({
            "program_id": s.program_id,
            "quota": s.quota,
            "filled": s.filled_seats,
            "total": s.total_seats,
            "remaining": s.total_seats - s.filled_seats
        })

    return jsonify(result)

@routes.route("/pending-docs")
def pending_docs():
    apps = Applicant.query.filter(Applicant.document_status != "Verified").all()

    result = [{"id": a.id, "name": a.name, "status": a.document_status} for a in apps]

    return jsonify(result)

@routes.route("/pending-fees")
def pending_fees():
    admissions = Admission.query.filter_by(fee_status="Pending").all()

    result = [{"id": a.id, "applicant_id": a.applicant_id} for a in admissions]

    return jsonify(result)   