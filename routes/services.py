from flask import Blueprint, request, jsonify
from database import db
from datetime import datetime

services_bp = Blueprint("services", __name__)


# -----------------------------
# Database Models
# -----------------------------

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(500))
    department = db.Column(db.String(200))


class ServiceApplication(db.Model):
    __tablename__ = "service_applications"

    id = db.Column(db.Integer, primary_key=True)

    citizen_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)

    status = db.Column(db.String(50), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# -----------------------------
# Get All Government Services
# -----------------------------

@services_bp.route("/api/services", methods=["GET"])
def get_services():

    services = Service.query.all()

    result = []

    for s in services:
        result.append({
            "id": s.id,
            "name": s.name,
            "description": s.description,
            "department": s.department
        })

    return jsonify(result)


# -----------------------------
# Apply For Service
# -----------------------------

@services_bp.route("/api/services/apply", methods=["POST"])
def apply_service():

    data = request.json

    application = ServiceApplication(
        citizen_id=data["citizen_id"],
        service_id=data["service_id"]
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "message": "Application submitted successfully",
        "application_id": application.id
    })


# -----------------------------
# Get Citizen Applications
# -----------------------------

@services_bp.route("/api/services/user/<citizen_id>", methods=["GET"])
def get_user_services(citizen_id):

    apps = ServiceApplication.query.filter_by(
        citizen_id=citizen_id
    ).all()

    result = []

    for a in apps:

        service = Service.query.get(a.service_id)

        result.append({
            "application_id": a.id,
            "service": service.name,
            "status": a.status,
            "date": a.created_at
        })

    return jsonify(result)


# -----------------------------
# Update Application Status
# -----------------------------

@services_bp.route("/api/services/update/<app_id>", methods=["PUT"])
def update_status(app_id):

    data = request.json

    application = ServiceApplication.query.get(app_id)

    if not application:
        return jsonify({"error": "Application not found"}), 404

    application.status = data["status"]

    db.session.commit()

    return jsonify({
        "message": "Application status updated"
    })
