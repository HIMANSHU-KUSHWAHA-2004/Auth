from flask import Blueprint, request, jsonify
from supabase_client import supabase
import uuid

form_bp = Blueprint("form", __name__)

@form_bp.route("/submit-form", methods=["POST"])
def submit_form():
    data = request.json
    user_id = data.get("user_id")
    field1 = data.get("field1")
    field2 = data.get("field2")

    if not user_id:
        return jsonify({"message": "User ID is required"}), 400

    # Insert submission
    supabase.table("submissions").insert({
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "field1": field1,
        "field2": field2
    }).execute()

    return jsonify({"message": "Form submitted successfully"})
