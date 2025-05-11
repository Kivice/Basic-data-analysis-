import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (Modify filename as needed)
df = pd.read_csv("iris.csv")

# Ensure column names match dataset
if 'sepal_length' in df.columns and 'sepal_width' in df.columns and 'petal_length' in df.columns:
    sepal_length_col = 'sepal_length'
    sepal_width_col = 'sepal_width'
    petal_length_col = 'petal_length'
    species_col = 'species'
else:
    print("Error: Required columns not found in the dataset.")
    exit(1)

# ------------------------------
# 1. Line Chart: Trends over Time (Simulated sales data)
# ------------------------------
# Creating a sample date column for demonstration
df['date'] = pd.date_range(start="2025-01-01", periods=len(df), freq='D')

plt.figure(figsize=(8, 4))
plt.plot(df['date'], df[sepal_length_col], marker='o', linestyle='-', color='blue', label="Sepal Length Trend")
plt.xlabel("Date")
plt.ylabel("Sepal Length")
plt.title("Line Chart: Sepal Length Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------
# 2. Bar Chart: Comparison across Categories (Average Sepal Length per Species)
# ------------------------------
species_avg = df.groupby(species_col)[sepal_length_col].mean()

plt.figure(figsize=(8, 4))
plt.bar(species_avg.index, species_avg.values, color=['green', 'blue', 'red'])
plt.xlabel("Species")
plt.ylabel("Average Sepal Length")
plt.title("Bar Chart: Average Sepal Length Per Species")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# 3. Histogram: Distribution of Sepal Length
# ------------------------------
plt.figure(figsize=(8, 4))
plt.hist(df[sepal_length_col], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram: Sepal Length Distribution")
plt.show()

# ------------------------------
# 4. Scatter Plot: Relationship between Sepal Length and Petal Length
# ------------------------------
plt.figure(figsize=(8, 4))
plt.scatter(df[sepal_length_col], df[petal_length_col], c='purple', alpha=0.7)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Scatter Plot: Sepal Length vs. Petal Length")
plt.show()
