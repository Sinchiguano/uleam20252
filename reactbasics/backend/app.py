# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from http://localhost:5173 while developing

@app.get("/api/time")
def get_time():
    from datetime import datetime
    return jsonify({"time": datetime.now().isoformat()})


# @app.get("/api/students")
# def list_students():
#     # TODO: query PostgreSQL (SQLAlchemy)
#     rows = [{"id":1,"name":"Ana"}, {"id":2,"name":"Luis"}]
#     return jsonify({"items": rows})



if __name__ == "__main__":
    app.run(port=5000, debug=True)
