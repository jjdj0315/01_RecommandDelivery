import os
import urllib

import certifi
from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi


MAPPING_EN2KO = {
    "hangover": "해장",
    "diet": "다이어트",
    "work_dinner": "회식",
    "date": "데이트",
    "after_workout": "운동후",
    "business_trip": "출장",
    "late_night_work": "야근",
    "rainy_day": "비오는날"
}
MAPPING_KO2EN = {v: k for k, v in MAPPING_EN2KO.items()}

app = FastAPI()

username = urllib.parse.quote_plus(os.environ['MONGODB_USERNAME'])
password = urllib.parse.quote_plus(os.environ['MONGODB_PASSWORD'])
uri = f"mongodb+srv://{username}:{password}@cluster0.d7yebsh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client.recommendations_db
collection = db.recommendations


@app.get("/health")
def health():
    return "OK"


@app.get("/recommend/{query_en}")
def recommend(query_en: str = "hangover"):
    print("succsess query")
    query_ko = MAPPING_EN2KO[query_en]
    data = list(collection.find({"_id": query_ko}, {'_id': 0}))
    return data