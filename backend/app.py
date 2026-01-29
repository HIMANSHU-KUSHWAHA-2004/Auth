from flask import Flask
from flask_cors import CORS
from config import SECRET_KEY
from routes.auth import auth_bp
from routes.form import form_bp

# Initialize Flask app
app = Flask(__name__)
app.secret_key = SECRET_KEY

# Enable CORS so frontend can communicate
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(form_bp, url_prefix="/form")

if __name__ == "__main__":
    app.run(debug=True)
