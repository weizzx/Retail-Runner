from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Access database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
