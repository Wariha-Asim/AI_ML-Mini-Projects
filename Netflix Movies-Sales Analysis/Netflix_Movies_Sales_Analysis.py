# ================================
# Netflix Data Analysis & Visualization
# ================================

# Libraries for data analysis and visualization
import pandas as pd          # For data manipulation
import numpy as np           # For numerical calculations
import matplotlib.pyplot as plt  # For charts and visualization

# ================================
# 1. Data Loading & Inspection
# ================================
# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv', encoding='latin-1')

# Inspect first few rows
# print(df.head(10))

# Check data types and missing values
# print(df.info())
# print(df.describe())

# Fill missing values if required
df.fillna('Unknown', inplace=True)

# ================================
# 2. Genre Analysis
# ================================
# Count number of shows per genre
shows_per_genre = df.groupby('listed_in').size()

# Average number of shows per genre
avg_shows_per_genre = shows_per_genre.mean()
print(f"\nAverage shows per genre: {avg_shows_per_genre}")

# Total shows across all genres
total_shows_genre = shows_per_genre.sum()
print(f"Total shows per genre: {total_shows_genre}")

# ================================
# 3. Country Analysis
# ================================
# Count shows per country
shows_per_country = df.groupby('country')['show_id'].count()

# Identify the top country producing most shows
top_country = shows_per_country.idxmax()
top_country_count = shows_per_country.max()
print(f"\nTop country producing most shows: {top_country} ({top_country_count} shows)")

# Total shows per country
total_shows_country = shows_per_country.sum()
print(f"Total shows per country: {total_shows_country}")

# ================================
# 4. Release Year Analysis
# ================================
# Count number of shows released per year
shows_per_year = df.groupby('release_year').size()
print(f"\nNumber of shows released per year:\n{shows_per_year}")

# Line plot: Shows released over the years
plt.figure(figsize=(10,6))
plt.plot(shows_per_year.index, shows_per_year.values,
         color='green', linestyle="--", marker='s', markersize=8)
plt.grid(True)
plt.title("Netflix Shows Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.show()

# ================================
# 5. Visualizations
# ================================
# Bar chart: Shows per genre
plt.figure(figsize=(12,6))
plt.bar(shows_per_genre.index, shows_per_genre.values,
        color='skyblue', edgecolor='black')
plt.xticks(rotation=45, ha='right')  # Rotate labels for readability
plt.grid(axis='y')
plt.title("Number of Shows per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Shows")
plt.show()

# Bar chart: Top 10 countries by number of shows
top_10_countries = shows_per_country.sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(top_10_countries.index, top_10_countries.values,
        color='orange', edgecolor='black')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.title("Top 10 Countries by Number of Netflix Shows")
plt.xlabel("Country")
plt.ylabel("Number of Shows")
plt.show()
