from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Vercel) to access backend
origins = [
    "https://demo-frontend-eta-ruby.vercel.app",  # your Vercel frontend URL
    "http://localhost:3000"  # for local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is working!"}
