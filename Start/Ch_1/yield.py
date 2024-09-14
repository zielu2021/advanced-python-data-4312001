def read_large_file(file_path):
    """Reads a large file one line at a time using a generator."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Example usage
for line in read_large_file("large_log_file.txt"):
    if "ERROR" in line:
        print(f"Found error: {line.strip()}")








def fetch_paginated_data(api_url):
    """Fetches data from a paginated API using yield."""
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        if not data['results']:  # No more results
            break
        yield data['results']
        page += 1

# Example usage
for page_data in fetch_paginated_data("https://api.example.com/data"):
    for item in page_data:
        print(item)




import time
import random

def sensor_stream():
    """Simulates streaming data from a sensor using yield."""
    while True:
        data = {
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 60), 2)
        }
        yield data
        time.sleep(1)  # Simulate delay between data points

# Example usage
for sensor_data in sensor_stream():
    print(f"Temperature: {sensor_data['temperature']}°C, Humidity: {sensor_data['humidity']}%")








import os

def find_files(directory, extension):
    """Yields files with a specific extension in a directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

# Example usage
for file_path in find_files("/path/to/dir", ".txt"):
    print(f"Found file: {file_path}")





import csv

def read_large_csv(file_path):
    """Reads a large CSV file row by row using yield."""
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row

# Example usage
for row in read_large_csv("large_data.csv"):
    # Process each row
    print(row)
