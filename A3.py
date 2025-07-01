import os
import csv

# Get the absolute path to the CSV file
SCRIPT_PATH = os.path.dirname(__file__)
CSV_FILE = os.path.join(SCRIPT_PATH, "data", "restaurants.csv")  # ✅ FIX 1

def find_location(name):
    if not name:  # ✅ FIX 2: Handle None or empty input
        return None

    with open(CSV_FILE, "r", encoding="ISO-8859-1") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if name == row.get("Restaurant Name"):
                return (row.get("Lat"), row.get("Lon"))
    return None

location1 = find_location("Hotel Gasthaus Adler")
print(location1)  # should be ('48.05', '7.93')

location2 = find_location(None)
print(location2)  # should be None

location3 = find_location("Café Öbergska")
print(location3)  # should be ('57.61', '11.79')
