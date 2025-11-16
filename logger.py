from datetime import datetime, timezone
import json

class Logger:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, path="events.json"):
        self.path = path
        self.events = []

    def log(self, event_type, data):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "type": event_type,
            "data": data
        }
        self.events.append(event)
        print(f"[LOG] {event_type} -> {data}")

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.events, f, indent=4)