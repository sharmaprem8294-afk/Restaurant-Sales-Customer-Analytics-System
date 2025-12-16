# Restaurant Sales & Customer Analytics System

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. Load Dataset
df = pd.read_excel("restaurant_dataset.xlsx")

# Display first 5 rows
print("First 5 Rows")
print(df.head())

# Dataset information
print("\nDataset Info")
df.info()

# Summary statistics
print("\nSummary Statistics")
print(df.describe())

# Column names
print("\nColumn Names")
print(df.columns)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Unique values in each column
print("\nUnique Values in Each Column")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Data types
print("\nData Types")
print(df.dtypes)


# 3. Data Visualization

# 1. Line Chart: Orders over time
plt.figure(figsize=(10, 5))
df.groupby("order_date").size().plot()
plt.title("Orders Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.show()

# 2. Bar Chart: Orders by Restaurant
plt.figure(figsize=(8, 5))
df["restaurent_name"].value_counts().plot(kind="bar")
plt.title("Orders by Restaurant")
plt.xlabel("Restaurant")
plt.ylabel("Total Orders")
plt.show()

# 3. Pie Chart: Payment Mode Distribution
plt.figure(figsize=(7, 7))
df["payment_mode"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Mode Distribution")
plt.ylabel("")
plt.show()

# 4. Histogram: Customer Age Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["age"], bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 5. Bar Chart: Most Ordered Food Items
plt.figure(figsize=(8, 5))
df["food_item"].value_counts().plot(kind="bar")
plt.title("Most Ordered Food Items")
plt.xlabel("Food Item")
plt.ylabel("Order Count")
plt.show()

# 6. Stacked Bar Chart: Delivery Type by Restaurant
pd.crosstab(df["restaurent_name"], df["delivery_type"]).plot(
    kind="bar", stacked=True, figsize=(10, 6)
)
plt.title("Delivery Type by Restaurant")
plt.xlabel("Restaurant")
plt.ylabel("Count")
plt.show()

# 7. Scatter Plot: Age vs Quantity Ordered
plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["quantity"])
plt.title("Age vs Quantity Ordered")
plt.xlabel("Age")
plt.ylabel("Quantity")
plt.show()

# 8. Bar Chart: Monthly Orders
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month

plt.figure(figsize=(8, 5))
df["month"].value_counts().sort_index().plot(kind="bar")
plt.title("Orders Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.show()
