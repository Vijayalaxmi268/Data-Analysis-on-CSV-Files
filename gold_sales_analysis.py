import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("gold_sales.csv")

# Explore data
print("First 5 rows:")
print(data.head())
print("\n Summary:")
print(data.describe())

# Calculate total sales
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Branch-wise sales
branch_sales = data.groupby("Branch")["Total_Sales"].sum().reset_index()
print("\n Total Sales by Branch:")
print(branch_sales)

# Product-wise sales
product_sales = data.groupby("Product")["Total_Sales"].sum().reset_index()
print("\n Total Sales by Product:")
print(product_sales)

# Plot 1: Branch-wise Sales
plt.figure(figsize=(6,4))
sns.barplot(x="Branch", y="Total_Sales", data=branch_sales)
plt.title("Branch-wise Total Sales")
plt.ylabel("Total Sales (₹)")
plt.show()

# Plot 2: Product-wise Sales
plt.figure(figsize=(7,4))
sns.barplot(x="Product", y="Total_Sales", data=product_sales)
plt.title("Product-wise Total Sales")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.show()

# Plot 3: Daily Sales Trend
daily_sales = data.groupby("Date")["Total_Sales"].sum().reset_index()
plt.figure(figsize=(8,4))
plt.plot(daily_sales["Date"], daily_sales["Total_Sales"], marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.grid(True)
plt.show()
