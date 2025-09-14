from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
import os

# ------------------------------
# FastAPI app
# ------------------------------
app = FastAPI()

# CORS (for hackathons / frontend testing allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# Supabase client
# ------------------------------
SUPABASE_URL: str = os.getenv("https://meubndlpfrjlqrgjezyv.supabase.co")
SUPABASE_KEY: str = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ldWJuZGxwZnJqbHFyZ2plenl2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzg2MDM2NiwiZXhwIjoyMDczNDM2MzY2fQ.muaXbJY29xhyG8T_wkKZfWxJJdV-YC7ouKgj5AIboaw")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------------------
# Routes
# ------------------------------

@app.get("/")
def health_check():
    """Simple backend health check"""
    return {"message": "Backend is working!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    """Simple hello endpoint"""
    return {"message": f"Hello, {name}! Your backend is live 🚀"}


@app.get("/test-db")
def test_db():
    """Fetch first 5 rows from Supabase 'profiles' table"""
    try:
        response = supabase.table("profiles").select("*").limit(5).execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ------------------------------
# Local dev entrypoint
# ------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
