from flask import request, jsonify
from . import api_bp
from ..database import db
from ..models import Course

def serialize_course(c: Course):
    return {
        "id": c.id,
        "code": c.code,
        "title": c.title,
        "credits": c.credits,
        "created_at": c.created_at.isoformat(),
    }

@api_bp.get("/courses")
def list_courses():
    search = request.args.get("search", "").strip()
    q = Course.query
    if search:
        like = f"%{search}%"
        q = q.filter((Course.title.ilike(like)) | (Course.code.ilike(like)))
    items = [serialize_course(c) for c in q.order_by(Course.id.desc()).all()]
    return jsonify({"items": items, "total": len(items)}), 200

@api_bp.post("/courses")
def create_course():
    data = request.get_json() or {}
    required = ["code", "title", "credits"]
    if not all(k in data for k in required):
        return jsonify({"error": "ValidationError", "message": "Missing fields"}), 400
    if Course.query.filter_by(code=data["code"]).first():
        return jsonify({"error": "ValidationError", "message": "course code exists"}), 409
    try:
        credits = int(data["credits"])
    except Exception:
        return jsonify({"error": "ValidationError", "message": "credits must be integer"}), 400
    c = Course(code=data["code"], title=data["title"], credits=credits)
    db.session.add(c)
    db.session.commit()
    return jsonify(serialize_course(c)), 201

@api_bp.get("/courses/<int:cid>")
def get_course(cid):
    c = Course.query.get_or_404(cid)
    return jsonify(serialize_course(c)), 200

@api_bp.put("/courses/<int:cid>")
def update_course(cid):
    c = Course.query.get_or_404(cid)
    data = request.get_json() or {}
    for k in ["code", "title", "credits"]:
        if k in data:
            setattr(c, k, data[k])
    db.session.commit()
    return jsonify(serialize_course(c)), 200

@api_bp.delete("/courses/<int:cid>")
def delete_course(cid):
    c = Course.query.get_or_404(cid)
    db.session.delete(c)
    db.session.commit()
    return ("", 204)
