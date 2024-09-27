import csv
import random
from datetime import datetime, timedelta
# Function to generate random data
def generate_random_data(num_records=20):
    data = []
    start_date = datetime.now() - timedelta(days=num_records)
    for i in range(num_records):
        timestamp = start_date + timedelta(days=i)
        energy_consumed = round(random.uniform(10, 100), 2)  # Simulate energy consumption in kWh
        device_id = f"device_{random.randint(1, 10)}"  # Random device ID
        data.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), energy_consumed, device_id])
    return data
# Generate data
data = generate_random_data()
# Write data to a CSV file
csv_file_path = "C:/Users/amarj/OneDrive/Desktop/Hexaware_Projects/Energy_Project/Week-2/energy_consumption_data.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "energy_consumed", "device_id"]) 
    writer.writerows(data)
print(f"CSV file '{csv_file_path}' created successfully!")