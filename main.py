# ================== IMPORTS (MODULE 4 + 3) ==================
import json
import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# ================== MODULE 2: CLASS DESIGN ==================
class FarmRecord:
 def __init__(self, crop, moisture, temperature, humidity):
 self.crop = crop
 self.moisture = moisture
 self.temperature = temperature
 self.humidity = humidity
 self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 def analyze(self):
 """Analyze farm conditions"""
 result = {}
 if self.moisture < 40:
 result["moisture"] = "Dry - Irrigation Needed"
 elif self.moisture > 80:
 result["moisture"] = "Too Wet"
 else:
 result["moisture"] = "Optimal"
 if self.temperature > 35:
 result["temperature"] = "High"
 elif self.temperature < 15:
 result["temperature"] = "Low"
 else:
 result["temperature"] = "Normal"
 if self.humidity < 50:
 result["humidity"] = "Low"
 else:
 result["humidity"] = "Good"
 return result
 def to_dict(self):
 """Convert object to dictionary"""
 return {
 "crop": self.crop,
 "moisture": self.moisture,
 "temperature": self.temperature,
 "humidity": self.humidity,
 "date": self.date,
 "analysis": self.analyze()
 }
# ================== MODULE 3: FILE HANDLING ==================
class FileManager:
 FILE_JSON = "farm_data.json"
 FILE_CSV = "farm_data.csv"
@staticmethod
 def save_json(data):
 with open(FileManager.FILE_JSON, "w") as f:
 json.dump(data, f, indent=4)
@staticmethod
 def load_json():
 if not os.path.exists(FileManager.FILE_JSON):
 return []
 with open(FileManager.FILE_JSON, "r") as f:
 return json.load(f)
@staticmethod
 def save_csv(data):
 with open(FileManager.FILE_CSV, "w", newline="") as f:
 writer = csv.writer(f)
 writer.writerow(["Crop", "Moisture", "Temperature", "Humidity", "Date"])
 for d in data:
 writer.writerow([d["crop"], d["moisture"], d["temperature"], d["humidity"], d["date"]])
# ================== MODULE 2: FUNCTIONAL LOGIC ==================
def add_record():
 """Take input from user"""
 try:
 crop = input("Enter crop name: ")
 moisture = float(input("Enter soil moisture: "))
 temp = float(input("Enter temperature: "))
 humidity = float(input("Enter humidity: "))
record = FarmRecord(crop, moisture, temp, humidity)
 return record.to_dict()
 except ValueError:
 print("Invalid input! Try again.")
 return None
def display_records(data):
 print("\n===== FARM DATA =====")
 for d in data:
 print(d)
def analyze_summary(data):
 """Use NumPy for analytics"""
 if not data:
 print("No data available")
 return
 moisture = np.array([d["moisture"] for d in data])
 temp = np.array([d["temperature"] for d in data])
 humidity = np.array([d["humidity"] for d in data])
 print("\n===== ANALYTICS =====")
 print("Average Moisture:", np.mean(moisture))
 print("Average Temperature:", np.mean(temp))
 print("Average Humidity:", np.mean(humidity))
# ================== MODULE 4: DATAFRAME OPERATIONS ==================
def pandas_operations(data):
 df = pd.DataFrame(data)
 print("\n===== DATAFRAME =====")
 print(df)
 print("\nHigh Temperature Records:")
 print(df[df["temperature"] > 35])
 print("\nGrouping by Crop:")
 print(df.groupby("crop")["moisture"].mean())
# ================== MODULE 4: VISUALIZATION ==================
def visualize(data):
 df = pd.DataFrame(data)
 plt.figure()
 plt.plot(df["crop"], df["moisture"])
 plt.title("Soil Moisture by Crop")
 plt.xlabel("Crop")
 plt.ylabel("Moisture")
 plt.show()
 plt.figure()
 plt.bar(df["crop"], df["temperature"])
 plt.title("Temperature by Crop")
 plt.show()
# ================== MODULE 3: EXCEPTION HANDLING ==================
def safe_load():
 try:
 return FileManager.load_json()
 except Exception as e:
 print("Error loading file:", e)
 return []
# ================== MAIN MENU SYSTEM ==================
def main():
 data = safe_load()
 while True:
 print("\n====== SMART AGRICULTURE SYSTEM ======")
 print("1. Add Record")
 print("2. View Records")
 print("3. Analyze Data")
 print("4. Pandas Operations")
 print("5. Visualize Data")
 print("6. Save to CSV")
 print("7. Exit")
 choice = input("Enter choice: ")
 if choice == "1":
 record = add_record()
 if record:
 data.append(record)
 elif choice == "2":
 display_records(data)
 elif choice == "3":
 analyze_summary(data)
 elif choice == "4":
 pandas_operations(data)
 elif choice == "5":
 visualize(data)
 elif choice == "6":
 FileManager.save_csv(data)
 print("Saved to CSV")
 elif choice == "7":
 FileManager.save_json(data)
 print("Data saved. Exiting...")
 break
 else:
 print("Invalid choice!")
# ================== RUN PROGRAM ==================
if __name__ == "__main__":
 main()
