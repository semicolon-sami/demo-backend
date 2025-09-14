from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ For hackathon/demo: allow all origins (easy, less headache)
# Later, you can restrict to only your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins
    allow_credentials=True,
    allow_methods=["*"],       # allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],       # allow all headers
)

@app.get("/")
def health_check():
    return {"message": "Backend is working!"}

# Example endpoint to test data fetch
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Your backend is live 🚀"}
