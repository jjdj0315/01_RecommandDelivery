import os
import urllib.parse
from dotenv import load_dotenv
import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv() 

def mongodb_connect():
    username = urllib.parse.quote_plus(os.environ['MONGODB_USERNAME'])
    password = urllib.parse.quote_plus(os.environ['MONGODB_PASSWORD'])

    uri = f"mongodb+srv://{username}:{password}@cluster0.d7yebsh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)    
        
        
        
        
        