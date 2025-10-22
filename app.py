import pandas as pd
import json
with open("nested_json.js", "r") as f:
    obj = json.loads(f)
pd.json_normalize(obj["items"])

print(obj)