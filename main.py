from fastapi import FastAPI

from models import User, Tweet

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}