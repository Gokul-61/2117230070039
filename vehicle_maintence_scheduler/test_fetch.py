from fetch_data import fetch_depots, fetch_tasks

depots = fetch_depots()

print("DEPOTS:")
print(depots)

first_depot_id = depots["depots"][0]["ID"]

print("\nTASKS:")
tasks = fetch_tasks(first_depot_id)

print(tasks)