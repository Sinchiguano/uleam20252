import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from models import db, Student

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "change-me"  # for flash messages

    user = os.getenv("DB_USER")
    pwd  = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    name = os.getenv("DB_NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{user}:{pwd}@{host}/{name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Routes
    @app.get("/students")
    def list_students():
        students = Student.query.order_by(Student.id.desc()).all()
        return render_template("students_list.html", students=students)

    @app.get("/students/new")
    def new_student():
        return render_template("students_new.html")

    @app.post("/students")
    def create_student():
        name   = request.form.get("name", "").strip()
        career = request.form.get("career", "").strip()
        email  = request.form.get("email", "").strip()

        if not (name and career and email):
            flash("All fields are required.")
            return redirect(url_for("new_student"))

        try:
            db.session.add(Student(name=name, career=career, email=email))
            db.session.commit()
            flash("Student created successfully.")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}")
        return redirect(url_for("list_students"))

    # Optional delete
    @app.post("/students/<int:sid>/delete")
    def delete_student(sid):
        s = Student.query.get_or_404(sid)
        db.session.delete(s)
        db.session.commit()
        flash("Student deleted.")
        return redirect(url_for("list_students"))

    @app.get("/")
    def home():
        return redirect(url_for("list_students"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
