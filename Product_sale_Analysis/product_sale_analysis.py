# =========================================================
# Project: Product Sales Analysis
# Libraries: Pandas, NumPy, Matplotlib
# Objective: Analyze sales data to identify top products, monthly trends,
#            total revenue, and visualize insights for business decisions.
# Dataset: sales_data_sample.csv (Product, Quantity, Price, Month, Sales)
# =========================================================

# 1. Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. Load the dataset
# Ensure the CSV file is in the same directory or provide full path
df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')

# 3. Inspect the dataset
print("First 10 rows of the dataset:")
print(df.head(10))
print("\nDataset Info:")
print(df.info())
print("\nDataset Description:")
print(df.describe())

# 4. Calculate total revenue
# Assuming 'SALES' column contains revenue for each transaction
total_revenue = df['SALES'].sum()
print(f"\nTotal Revenue: ${total_revenue}")

# 5. Identify top-selling products
top_selling_product = df.groupby('PRODUCTCODE')['SALES'].sum().sort_values(ascending=False)
print("\nTop Selling Products by Revenue:")
print(top_selling_product)

# 6. Monthly sales trend
sales_by_month = df.groupby('MONTH_ID')['SALES'].sum()
print("\nSales by Month:")
print(sales_by_month)

# 7. Visualization: Monthly Sales Trend (Line Chart)
plt.figure(figsize=(10,5))
plt.plot(sales_by_month.index, sales_by_month.values, marker='o', color='skyblue', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')
plt.xticks(sales_by_month.index)
plt.grid(True)
plt.show()

# 8. Visualization: Sales Percentage by Product (Pie Chart)
plt.figure(figsize=(8,8))
plt.pie(top_selling_product,
        labels=top_selling_product.index,
        autopct='%1.1f%%',
        startangle=140,
        shadow=True)
plt.title("Sales Percentage by Product")
plt.show()

# 9. Key Insights
print("\n--- Key Insights ---")
print(f"Total Revenue Generated: ${total_revenue}")
print(f"Top Selling Product: {top_selling_product.idxmax()} with Revenue: ${top_selling_product.max()}")
print(f"Month with Highest Sales: {sales_by_month.idxmax()} with Sales: ${sales_by_month.max()}")

