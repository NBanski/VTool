import json

with open("report_test.json", "r") as f:
    data = json.load(f)

print(data.keys())
