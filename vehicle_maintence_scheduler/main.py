from fastapi import FastAPI

from api import get_depots, get_vehicles
from scheduler import knapsack

# Create FastAPI app
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Vehicle Maintenance Scheduler Running"
    }


@app.get("/optimize")
def optimize():

    depots = get_depots()

    vehicles = get_vehicles()

    print("DEPOTS RESPONSE:")
    print(depots)

    print("VEHICLES RESPONSE:")
    print(vehicles)

    return {
        "depots": depots,
        "vehicles": vehicles
    }

    return result