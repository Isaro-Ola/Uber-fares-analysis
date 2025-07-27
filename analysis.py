import pandas as pd

# Load the dataset
df = pd.read_csv("uber.csv")

# Show basic info
print("\n=== Dataset Info ===")
print(df.info())

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Save the cleaned data to a new CSV
df_cleaned.to_csv("uber_cleaned.csv", index=False)

# Preview the cleaned data
print("\n=== Cleaned Data Preview ===")
print(df_cleaned.head())
# === EDA: Descriptive Statistics ===
print("\n=== Descriptive Statistics ===")
print(df_cleaned.describe())

# === EDA: Median and Mode ===
print("\n=== Median Fare ===")
print(df_cleaned["fare_amount"].median())

print("\n=== Mode Fare ===")
print(df_cleaned["fare_amount"].mode()[0])
import matplotlib.pyplot as plt
import seaborn as sns

# === EDA: Fare Distribution Plot ===
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned["fare_amount"], bins=50, kde=True, color='skyblue')
plt.title("Fare Amount Distribution")
plt.xlabel("Fare Amount ($)")
plt.ylabel("Number of Rides")
plt.grid(True)
plt.tight_layout()
plt.savefig("fare_distribution.png")  # ✅ Save the plot as an image
plt.show()
# === EDA: Outlier Detection using IQR ===
Q1 = df_cleaned["fare_amount"].quantile(0.25)
Q3 = df_cleaned["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Count outliers
outliers = df_cleaned[(df_cleaned["fare_amount"] < lower_bound) | (df_cleaned["fare_amount"] > upper_bound)]
print(f"\nNumber of fare outliers: {outliers.shape[0]}")

# Optional: Visualize outliers using boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_cleaned["fare_amount"], color="salmon")
plt.title("Fare Amount - Outlier Detection")
plt.xlabel("Fare Amount ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fare_boxplot.png")  # ✅ Save the boxplot
plt.show()
from math import radians, cos, sin, asin, sqrt

# === Function to calculate distance between two GPS points ===
def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    # Haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius of earth in kilometers
    return c * r

# === Apply function to each row to compute distance ===
df_cleaned["distance_km"] = df_cleaned.apply(lambda row: haversine(
    row["pickup_longitude"],
    row["pickup_latitude"],
    row["dropoff_longitude"],
    row["dropoff_latitude"]
), axis=1)

# === Scatter Plot: Fare vs Distance ===
plt.figure(figsize=(10, 6))
sns.scatterplot(x="distance_km", y="fare_amount", data=df_cleaned, alpha=0.4)
plt.title("Fare Amount vs. Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Fare Amount ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fare_vs_distance.png")
plt.show()
# === Extract Hour from Pickup Datetime ===
df_cleaned["pickup_datetime"] = pd.to_datetime(df_cleaned["pickup_datetime"], errors='coerce')
df_cleaned["hour"] = df_cleaned["pickup_datetime"].dt.hour

# === Line Plot: Average Fare by Hour ===
plt.figure(figsize=(10, 6))
hourly_avg = df_cleaned.groupby("hour")["fare_amount"].mean()
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker="o", color="green")
plt.title("Average Fare Amount by Hour of Day")
plt.xlabel("Hour of Day (0 = Midnight)")
plt.ylabel("Average Fare ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fare_by_hour.png")
plt.show()
# Add 'hour' column from pickup_datetime
df_cleaned["pickup_datetime"] = pd.to_datetime(df_cleaned["pickup_datetime"], errors='coerce')
df_cleaned["hour"] = df_cleaned["pickup_datetime"].dt.hour

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv("uber_cleaned.csv", index=False)
print("✅ Cleaned data with 'hour' column saved to 'uber_cleaned.csv'")