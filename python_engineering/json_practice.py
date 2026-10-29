
from datetime import datetime
import json

user_data = {"name": "jayu", "skills": ["python", "FastAPI"], "created_at": datetime.now()}

user_json = json.dumps(user_data, indent=2, default=str)

print(user_json)
try:
    broken_json = '{"name": "Amit"'

    json.loads(broken_json)
    

except json.JSONDecodeError:
    print("Invalid Json Caught!")