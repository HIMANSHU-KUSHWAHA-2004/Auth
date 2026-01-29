import os

# Supabase project URL and anon key
SUPABASE_URL = "https://cgfkbomcjsyrvuwlehck.supabase.co"
SUPABASE_KEY = "sb_publishable_hM1TLN49cr0MO3Wzza-USg_Sh3Vzhc0"

# Flask secret key for sessions
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
