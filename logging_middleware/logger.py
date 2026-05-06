import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def Log(stack, level, package, message):
    url = "http://20.207.122.201/evaluation-service/logs"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()