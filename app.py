import pandas as pd
import json
with open("nested_json.js", "r") as f:
    obj = json.load(f)
frame = pd.json_normalize(obj["items"])

print(frame)