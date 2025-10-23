import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from .database import init_db
from .routes import api_bp

def create_app():
    load_dotenv()  # loads backend/.env if present
    app = Flask(__name__)

    init_db(app)

    origins = os.getenv("CORS_ORIGINS", "*")
    CORS(app, resources={r"/api/*": {"origins": origins}})

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"}), 200

    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host=host, port=port, debug=debug)
