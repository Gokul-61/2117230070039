
# Vehicle Maintenance Scheduler

FastAPI-based backend service for optimizing vehicle maintenance scheduling using Dynamic Programming (0/1 Knapsack Algorithm).

## Features

- Fetch depot data from API
- Fetch vehicle maintenance tasks
- Optimize task selection
- Maximize total impact within mechanic hour limits
- REST API using FastAPI

## Technologies Used

- Python
- FastAPI
- Requests
- Python-dotenv

## Project Structure

```text
vehicle_maintence_scheduler/
│
├── api.py
├── scheduler.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## API Endpoints

### Home Route

```http
GET /
```

Response:

```json
{
  "message": "Vehicle Maintenance Scheduler Running"
}
```

---

### Optimization Route

```http
GET /optimize
```

Returns optimized maintenance task selection for depots.

## Algorithm Used

### 0/1 Knapsack Algorithm

The scheduler uses Dynamic Programming to:

- Maximize total impact
- Stay within mechanic hour constraints
- Select optimal tasks efficiently

## Run Project

Install dependencies:

```bash
pip install fastapi uvicorn requests python-dotenv
```

Run server:

```bash
uvicorn main:app --reload
```

Open browser:

```text
http://127.0.0.1:8000/optimize
```

## Environment Variables

Create `.env` file:

```env
ACCESS_TOKEN=your_token_here
```