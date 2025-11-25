import json
import os
from datetime import datetime

def write_log(logs_dir: str, event: dict):
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    log_path = os.path.join(logs_dir, f"log_{timestamp}.json")

    with open(log_path, "w") as f:
        json.dump(event, f, indent=2, default=str)

    return log_path
