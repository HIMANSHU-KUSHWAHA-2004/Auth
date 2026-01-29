import os
from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.form import form_bp

# Initialize Flask app
app = Flask(__name__)

# Load secret key from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default_secret")

# Enable CORS so frontend can communicate
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(form_bp, url_prefix="/form")

# No need for debug=True; Render will use gunicorn
# app.run(debug=True)  # REMOVE this line for Render

# The Flask app instance must be named 'app' for gunicorn
