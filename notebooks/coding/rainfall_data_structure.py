# filename: rainfall_data_structure.py
import json

# Read data from JSON file into a Python object
with open("rainfall_data.json", "r") as file:
    data = json.load(file)

# Print the structure of the JSON data
print(json.dumps(data, indent=4))