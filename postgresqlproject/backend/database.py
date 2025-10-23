import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db_url = os.getenv("DATABASE_URL", "postgresql+psycopg2://sms_user:sms_pass@localhost:5432/sms_db")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        from .models import Student, Course, Enrollment  # noqa
        db.create_all()
