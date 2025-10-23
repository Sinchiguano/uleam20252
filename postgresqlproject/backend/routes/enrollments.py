from flask import request, jsonify
from . import api_bp
from ..database import db
from ..models import Student, Course, Enrollment

@api_bp.post("/enrollments")
def enroll():
    data = request.get_json() or {}
    sid, cid = data.get("student_id"), data.get("course_id")
    if not (sid and cid):
        return jsonify({"error": "ValidationError", "message": "student_id and course_id required"}), 400
    if Enrollment.query.filter_by(student_id=sid, course_id=cid).first():
        return jsonify({"error": "Conflict", "message": "already enrolled"}), 409
    e = Enrollment(student_id=sid, course_id=cid)
    db.session.add(e)
    db.session.commit()
    return jsonify({"id": e.id, "student_id": sid, "course_id": cid, "enrolled_at": e.enrolled_at.isoformat()}), 201

@api_bp.delete("/enrollments")
def unenroll():
    data = request.get_json() or {}
    sid, cid = data.get("student_id"), data.get("course_id")
    e = Enrollment.query.filter_by(student_id=sid, course_id=cid).first()
    if not e:
        return jsonify({"error": "NotFound", "message": "enrollment not found"}), 404
    db.session.delete(e)
    db.session.commit()
    return ("", 204)

@api_bp.get("/students/<int:sid>/courses")
def student_courses(sid):
    s = Student.query.get_or_404(sid)
    courses = [{"id": c.id, "code": c.code, "title": c.title, "credits": c.credits} for c in s.courses]
    return jsonify({"student_id": s.id, "courses": courses}), 200

@api_bp.get("/courses/<int:cid>/students")
def course_students(cid):
    c = Course.query.get_or_404(cid)
    students = [{"id": s.id, "first_name": s.first_name, "last_name": s.last_name, "email": s.email} for s in c.students]
    return jsonify({"course_id": c.id, "students": students}), 200
