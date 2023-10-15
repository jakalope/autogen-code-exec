# filename: rainfall_scatter_plot.py

import requests
import json
import genson
import matplotlib.pyplot as plt
from datetime import date

# Define today's date
today = date.today()

# Define the API URL with the latitude, longitude, start date, and end date
url = f"https://archive-api.open-meteo.com/v1/archive?latitude=37.3394&longitude=-121.895&start_date=2020-01-01&end_date={today}&hourly=rain"

# Define the filename to save the API response
filename = "rainfall_data.json"

# Check if the data file exists
try:
    with open(filename) as file:
        data = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, make a request to the API and save the response to the file
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(filename, "w") as file:
            json.dump(data, file)
    else:
        print("Error:", response.text)
        exit()

# Print the schema of the data using genson
schema = genson.Schema()
schema.add_object(data)
print(schema.to_json(indent=4))

# Extract the rainfall data from the API response
rainfall_data = data["data"]["rain"]

# Create lists to store the dates and rainfall values
dates = []
rainfall_values = []

# Iterate over the rainfall data and append the dates and rainfall values to the lists
for date, value in rainfall_data.items():
    dates.append(date)
    rainfall_values.append(value)

# Create a scatter plot of the rainfall data
plt.scatter(dates, rainfall_values)
plt.xlabel("Date")
plt.ylabel("Rainfall (inches)")
plt.title("Weekly Inches of Rainfall in San Francisco Bay Area (2020-Current Year)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the scatter plot to a local file
plot_filename = "rainfall_scatter_plot.png"
plt.savefig(plot_filename)

print("Scatter plot saved as", plot_filename)