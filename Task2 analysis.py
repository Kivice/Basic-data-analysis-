import pandas as pd

# Load dataset (Modify filename as needed)
df = pd.read_csv("iris.csv")

# Compute basic statistics for numerical columns
print("=== Basic Statistics ===")
print(df.describe())  # Includes mean, standard deviation, min, max, etc.

# Compute specific statistics manually
print("\n=== Custom Statistics ===")
print(f"Mean Sepal Length: {df['sepal_length'].mean():.2f}")
print(f"Median Sepal Length: {df['sepal_length'].median():.2f}")
print(f"Standard Deviation of Sepal Length: {df['sepal_length'].std():.2f}")

# Perform groupings (Example: Group by species and compute mean sepal length)
if.columns:
    species_avg = df.groupby('species')['sepal_length'].mean()
    print("\n=== Average Sepal Length Per Species ===")
    print(species_avg)
else:
    print("\nError: 'species' column not found in dataset.")

# Identify patterns or interesting findings
print("\n=== Observations ===")
print("- Some species may have significantly larger sepal lengths.")
print("- Standard deviation shows variability within the dataset.")
print("- Grouping by species helps reveal how measurements differ across categories.")
