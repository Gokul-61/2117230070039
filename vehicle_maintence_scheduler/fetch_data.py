import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

BASE_URL = "http://20.207.122.201/evaluation-service"

def fetch_depots():
    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )

    return response.json()

def fetch_tasks(depot_id):
    response = requests.get(
        f"{BASE_URL}/tasks?depotId={depot_id}",
        headers=headers
    )

    print(response.text)

    return response.text