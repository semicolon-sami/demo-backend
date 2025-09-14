from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
import os

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # for hackathons, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Supabase client (read from Render env vars)
SUPABASE_URL: str = os.getenv("https://meubndlpfrjlqrgjezyv.supabase.co")
SUPABASE_KEY: str = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ldWJuZGxwZnJqbHFyZ2plenl2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzg2MDM2NiwiZXhwIjoyMDczNDM2MzY2fQ.muaXbJY29xhyG8T_wkKZfWxJJdV-YC7ouKgj5AIboaw")  # 🔑 updated

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase environment variables. Check Render settings.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def health_check():
    return {"message": "Backend is working!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Your backend is live 🚀"}

# ✅ Database test: fetch rows from "profiles"
@app.get("/test-db")
def test_db():
    try:
        response = supabase.table("profiles").select("*").limit(5).execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
