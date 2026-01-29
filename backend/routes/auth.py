from flask import Blueprint, request, jsonify
from supabase_client import supabase
import hashlib, uuid

auth_bp = Blueprint("auth", __name__)

# Hash password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------ REGISTER ------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))

    # Check if user exists
    existing = supabase.table("users").select("*").eq("email", email).execute()
    if existing.data:
        return jsonify({"message": "User already exists"}), 400

    # Insert new user
    supabase.table("users").insert({
        "id": str(uuid.uuid4()),
        "email": email,
        "password": password
    }).execute()

    return jsonify({"message": "User registered successfully"}), 201

# ------------------ LOGIN ------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))

    # Fetch user
    user_data = supabase.table("users").select("*").eq("email", email).execute()
    user = user_data.data[0] if user_data.data else None

    if user and user["password"] == password:
        return jsonify({"message": "Login successful", "user_id": user["id"]})
    return jsonify({"message": "Invalid credentials"}), 401
