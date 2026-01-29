import os

# Supabase project URL and anon key
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Flask secret key for sessions
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
