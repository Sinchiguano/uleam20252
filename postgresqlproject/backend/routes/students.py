from flask import request, jsonify
from . import api_bp
from ..database import db
from ..models import Student

def serialize_student(s: Student):
    return {
        "id": s.id,
        "first_name": s.first_name,
        "last_name": s.last_name,
        "email": s.email,
        "age": s.age,
        "created_at": s.created_at.isoformat(),
    }

@api_bp.get("/students")
def list_students():
    search = request.args.get("search", "").strip()
    q = Student.query
    if search:
        like = f"%{search}%"
        q = q.filter(
            (Student.first_name.ilike(like)) |
            (Student.last_name.ilike(like)) |
            (Student.email.ilike(like))
        )
    items = [serialize_student(s) for s in q.order_by(Student.id.desc()).all()]
    return jsonify({"items": items, "total": len(items)}), 200

@api_bp.post("/students")
def create_student():
    data = request.get_json() or {}
    required = ["first_name", "last_name", "email", "age"]
    if not all(k in data for k in required):
        return jsonify({"error": "ValidationError", "message": "Missing fields"}), 400
    try:
        age = int(data["age"])
    except Exception:
        return jsonify({"error": "ValidationError", "message": "Age must be an integer"}), 400
    if not (16 <= age <= 80):
        return jsonify({"error": "ValidationError", "message": "Age must be between 16 and 80"}), 400
    if Student.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "ValidationError", "message": "email already exists"}), 409

    s = Student(first_name=data["first_name"], last_name=data["last_name"], email=data["email"], age=age)
    db.session.add(s)
    db.session.commit()
    return jsonify(serialize_student(s)), 201

@api_bp.get("/students/<int:sid>")
def get_student(sid):
    s = Student.query.get_or_404(sid)
    return jsonify(serialize_student(s)), 200

@api_bp.put("/students/<int:sid>")
def update_student(sid):
    s = Student.query.get_or_404(sid)
    data = request.get_json() or {}
    for k in ["first_name", "last_name", "email", "age"]:
        if k in data:
            setattr(s, k, data[k])
    db.session.commit()
    return jsonify(serialize_student(s)), 200

@api_bp.delete("/students/<int:sid>")
def delete_student(sid):
    s = Student.query.get_or_404(sid)
    db.session.delete(s)
    db.session.commit()
    return ("", 204)
