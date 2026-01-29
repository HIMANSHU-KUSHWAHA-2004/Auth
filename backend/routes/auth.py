from flask import Blueprint, request, jsonify
from supabase_client import supabase
from flask_cors import CORS
import hashlib, uuid

auth_bp = Blueprint("auth", __name__)
CORS(auth_bp)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))

    existing = supabase.table("users").select("*").eq("email", email).execute()
    if existing.data:
        return jsonify({"message": "User already exists"}), 400

    supabase.table("users").insert({
        "id": str(uuid.uuid4()),
        "email": email,
        "password": password
    }).execute()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))

    user_data = supabase.table("users").select("*").eq("email", email).execute()
    user = user_data.data[0] if user_data.data else None

    if user and user["password"] == password:
        return jsonify({"message": "Login successful", "user_id": user["id"]})

    return jsonify({"message": "Invalid credentials"}), 401
