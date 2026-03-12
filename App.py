import pandas as pd
import matplotlib.pyplot as plt

# Create Parking Dataset
data = {
    "Vehicle_ID": ["V101","V102","V103","V104","V105","V106","V107","V108","V109","V110"],
    "Slot_Number": ["S1","S2","S3","S1","S4","S2","S5","S3","S4","S1"],
    "Entry_Time": [
        "2024-03-01 08:00",
        "2024-03-01 09:30",
        "2024-03-01 10:00",
        "2024-03-01 11:15",
        "2024-03-01 12:00",
        "2024-03-01 13:20",
        "2024-03-01 14:10",
        "2024-03-02 09:00",
        "2024-03-02 10:45",
        "2024-03-02 12:30"
    ],
    "Exit_Time": [
        "2024-03-01 09:00",
        "2024-03-01 11:00",
        "2024-03-01 12:30",
        "2024-03-01 13:00",
        "2024-03-01 14:00",
        "2024-03-01 15:00",
        "2024-03-01 16:00",
        "2024-03-02 10:30",
        "2024-03-02 12:15",
        "2024-03-02 14:00"
    ],
    "Parking_Fee": [20,40,50,35,30,45,25,30,40,50]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("Parking Data:")
print(df)

# Convert time columns to datetime
df["Entry_Time"] = pd.to_datetime(df["Entry_Time"])
df["Exit_Time"] = pd.to_datetime(df["Exit_Time"])

# Extract hour from entry time
df["Hour"] = df["Entry_Time"].dt.hour

# Peak Parking Hours
peak_hours = df["Hour"].value_counts().sort_index()

print("\nPeak Parking Hours:")
print(peak_hours)

# Parking Slot Usage
slot_usage = df["Slot_Number"].value_counts()

print("\nParking Slot Usage:")
print(slot_usage)

# Daily Parking Trend
df["Date"] = df["Entry_Time"].dt.date
daily_trend = df.groupby("Date").size()

print("\nDaily Parking Trend:")
print(daily_trend)

# Total Revenue
total_revenue = df["Parking_Fee"].sum()

print("\nTotal Parking Revenue:", total_revenue)

# Graph: Peak Parking Hours
peak_hours.plot(kind="bar")

plt.title("Peak Parking Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Vehicles")

plt.show()

# Graph: Parking Slot Usage
slot_usage.plot(kind="bar")

plt.title("Parking Slot Usage")
plt.xlabel("Slot Number")
plt.ylabel("Number of Vehicles")

plt.show()