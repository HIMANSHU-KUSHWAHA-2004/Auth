import os
from supabase import create_client

# Get from environment variables
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Create client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Example test query
data = supabase.table("users").select("*").execute()
print(data.data)
