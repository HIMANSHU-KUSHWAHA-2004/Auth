import sys
import os
from flask import Flask
from flask_cors import CORS

# Make sure backend folder is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.auth import auth_bp
from routes.form import form_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default_secret")
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(form_bp, url_prefix="/form")
