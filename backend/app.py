import sys
import os
from flask import Flask, jsonify
from flask_cors import CORS

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.auth import auth_bp
from routes.form import form_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "Backend is running"})

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(form_bp, url_prefix="/form")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
