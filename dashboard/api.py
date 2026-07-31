from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

SAMPLE_PATH = os.path.join(os.path.dirname(__file__), "sample_data.json")

@app.get("/api/timeline")
def timeline():
    with open(SAMPLE_PATH) as f:
        return json.load(f)
