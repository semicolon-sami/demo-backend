from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

# Supabase config
SUPABASE_URL = "https://meubndlpfrjlqrgjezyv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ldWJuZGxwZnJqbHFyZ2plenl2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzg2MDM2NiwiZXhwIjoyMDczNDM2MzY2fQ.muaXbJY29xhyG8T_wkKZfWxJJdV-YC7ouKgj5AIboaw"  # backend only
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Backend is working!"}

@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data
