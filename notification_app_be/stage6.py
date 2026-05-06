import requests
import heapq
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

url = "http://20.207.122.201/evaluation-service/notifications"

response = requests.get(url, headers=headers)

data = response.json()

print(data)

if "notifications" in data:

    notifications = data["notifications"]

    weights = {
        "Placement": 10,
        "Result": 8,
        "Event": 5
    }

    def calculate_priority(notification):

        weight = weights.get(notification["Type"], 1)

        notification_time = datetime.strptime(
            notification["Timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        recency = notification_time.timestamp()

        return weight + recency

    def get_top_notifications(notifications, top_n=10):

        heap = []

        for notification in notifications:

            priority = calculate_priority(notification)

            if len(heap) < top_n:
                heapq.heappush(heap, (priority, notification))

            else:
                heapq.heappushpop(heap, (priority, notification))

        result = sorted(heap, reverse=True)

        return [item[1] for item in result]

    top_notifications = get_top_notifications(notifications)

    print("\nTOP PRIORITY NOTIFICATIONS:\n")

    for notification in top_notifications:
        print(notification)

else:
    print("Notifications API not available or token invalid.")