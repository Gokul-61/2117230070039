import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

BASE_URL = "http://20.207.122.201/evaluation-service"

def get_depots():

    url = f"{BASE_URL}/depots"

    response = requests.get(url, headers=headers)

    return response.json()

def get_vehicles():

    url = f"{BASE_URL}/vehicles"

    response = requests.get(url, headers=headers)

    return response.json()