# Logging Middleware

Reusable Python logging middleware integrated with the Affordmed Evaluation Logging API.

## Features

- Centralized logging
- API-based logging system
- Supports different log levels
- Reusable logging function
- Environment variable support

## Technologies Used

- Python
- Requests
- Python-dotenv

## Project Structure

```text
logging_middleware/
│
├── logger.py
├── test.py
├── requirements.txt
├── .env
└── README.md

```

## Logger Function

```python
Log(stack, level, package, message)
```

### Example

```python
Log(
    "backend",
    "info",
    "service",
    "Logging middleware working"
)
```

## Supported Log Levels

- debug
- info
- warn
- error
- fatal

## Environment Variables

Create `.env` file:

```env
ACCESS_TOKEN=your_token_here
```

## Run Test

```bash
python test.py
```

## Output

Successful log creation returns:

```json
{
  "logID": "...",
  "message": "log created successfully"
}
```