
# Campus Notification System Design

## Stage 1

### Core Features
- Send notifications to students
- Mark notifications as read/unread
- Get all notifications
- Priority notifications
- Real-time updates

---

## API Design

### Get Notifications

GET /api/notifications

Response:

```json
{
  "notifications": [
    {
      "id": "1",
      "type": "Placement",
      "message": "Company hiring",
      "timestamp": "2026-04-22T17:50:00"
    }
  ]
}
---

### Mark Notification as Read

PATCH /api/notifications/:id/read

Response:

```json
{
  "message": "Notification marked as read"
}
```

---

### Create Notification

POST /api/notifications

Request:

```json
{
  "type": "Placement",
  "message": "Amazon hiring"
}
```

Response:

```json
{
  "message": "Notification created"
}
```

---

## Real-Time Notification Approach

- Use WebSockets for live updates
- Frontend subscribes to notification events
- Backend pushes notifications instantly

---

## Stage 4

### Performance Improvements

- Use Redis caching
- Pagination for notifications
- Lazy loading
- Database indexing
- WebSocket connections instead of repeated polling

### Tradeoffs

| Solution | Advantage | Disadvantage |
|---|---|---|
| Redis Cache | Faster reads | Extra memory cost |
| Pagination | Less DB load | More API calls |
| WebSockets | Real-time updates | Persistent connections |

---

## Stage 5

### Problems in Existing Approach

- Sequential processing is slow
- One email failure can affect loop
- No retry mechanism
- Database and email tightly coupled

### Improved Design

- Use message queues
- Separate email service
- Retry failed notifications
- Async processing using workers

### Improved Pseudocode

```python
def notify_all(student_ids, message):
    save_notification(message)

    for student_id in student_ids:
        queue.publish({
            "student_id": student_id,
            "message": message
        })

worker():
    while True:
        task = queue.consume()

        try:
            send_email(task)
            push_notification(task)
        except:
            retry(task)
```

---

## Stage 6

### Priority Inbox Design

Priority Score Formula:

```text
Priority = Weight + Recency
```

### Weight Rules

- Placement = 10
- Result = 8
- Event = 5

### Efficient Top 10 Strategy

- Use Min Heap
- Maintain only top 10 notifications
- Replace lower priority items when higher priority arrives

### Advantages

- Efficient for large streams
- O(n log k) complexity
- Works for real-time notifications