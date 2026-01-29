from flask import Flask
from flask_cors import CORS
import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.auth import auth_bp
from routes.form import form_bp

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(form_bp, url_prefix="/form")

@app.route("/")
def home():
    return {"status": "Backend is running"}

if __name__ == "__main__":
    app.run()
