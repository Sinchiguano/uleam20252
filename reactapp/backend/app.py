
import os, urllib.parse
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # dev only

# ---- MySQL connection via SQLAlchemy ----
DB_USER = os.getenv("DB_USER", "flaskuser")
DB_PASS = urllib.parse.quote_plus(os.getenv("DB_PASS", "Uleam!2025"))
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_NAME = os.getenv("DB_NAME", "students_db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ---- Model ----
class Student(db.Model):
    __tablename__ = "students"
    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(120), nullable=False)
    age    = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age, "course": self.course}

# Create tables + smoke test
with app.app_context():
    db.session.execute(text("SELECT 1"))
    db.create_all()

# ---- API ----
@app.get("/api/students")
def list_students():
    students = Student.query.order_by(Student.id.desc()).all()
    return jsonify([s.to_dict() for s in students])

@app.post("/api/students")
def create_student():
    data = request.get_json() or {}
    name = (data.get("name") or "").strip()
    course = (data.get("course") or "").strip()
    age = data.get("age")

    if not name or not course:
        return jsonify({"error": "Name and course are required."}), 400
    try:
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError
    except Exception:
        return jsonify({"error": "Age must be a valid number (0–120)."}), 400

    try:
        s = Student(name=name, age=age, course=course)
        db.session.add(s)
        db.session.commit()
        return jsonify(s.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.delete("/api/students/<int:sid>")
def delete_student(sid):
    s = Student.query.get_or_404(sid)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"ok": True, "deleted": sid})

@app.get("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask + MySQL!"})

if __name__ == "__main__":
    app.run(debug=True)

