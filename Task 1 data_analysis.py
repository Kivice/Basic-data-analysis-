#!/usr/bin/env python3
"""
Data Loading, Exploration, and Visualization Example

This script performs the following tasks:
1. Loads the Iris dataset from a CSV file.
2. Displays the first few rows of the dataset.
3. Explores the structure by checking data types and counts of missing values.
4. Cleans the dataset by dropping rows with missing values (if found).
5. Provides some basic descriptive statistics.
6. Generates visualizations: a histogram for sepal length and a scatter plot showing 
   the relationship between sepal length and sepal width.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------

# Specify the dataset filename (ensure this file is in your working directory)
filename = "iris.csv"

# Try to load the dataset using Pandas
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found. Please ensure the dataset file exists in the current directory.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit(1)

# Display the first few rows of the dataset
print("=== First 5 Rows of the Dataset ===")
print(df.head())

# Explore the dataset structure: data types and non-null counts
print("\n=== Dataset Info ===")
print(df.info())

# Get basic descriptive statistics
print("\n=== Descriptive Statistics ===")
print(df.describe())

# Check for missing values in each column
print("\n=== Missing Values Per Column ===")
print(df.isnull().sum())

# Clean the dataset: Drop rows with missing values if any exist
if df.isnull().values.any():
    original_shape = df.shape
    df = df.dropna()
    print(f"\nMissing values were found. Dropped rows with missing values. Shape changed from {original_shape} to {df.shape}.")
else:
    print("\nNo missing values were found in the dataset.")

# ------------------------------
# Basic Observations (Findings)
# ------------------------------
# - The first few rows give an idea about the column names and data format.
# - Data exploration with info() and describe() shows the types of measurements and their statistical properties.
# - The missing values check confirms if any data cleaning is required.

# ------------------------------
# Task 2: Visualization
# ------------------------------

# For the visualization, we assume that the dataset contains columns
# named either 'sepal_length' & 'sepal_width' or 'SepalLengthCm' & 'SepalWidthCm'.
# Adjust the column names as needed.

# Define column names based on the dataset
if 'sepal_length' in df.columns and 'sepal_width' in df.columns:
    sepal_length_col = 'sepal_length'
    sepal_width_col = 'sepal_width'
elif 'SepalLengthCm' in df.columns and 'SepalWidthCm' in df.columns:
    sepal_length_col = 'SepalLengthCm'
    sepal_width_col = 'SepalWidthCm'
else:
    print("Error: Expected sepal length and sepal width columns were not found in the dataset.")
    exit(1)

# Create a figure with two subplots: one for a histogram and one for a scatter plot.
plt.figure(figsize=(12, 5))

# Histogram for Sepal Length
plt.subplot(1, 2, 1)
plt.hist(df[sepal_length_col], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")

# Scatter plot between Sepal Length and Sepal Width
plt.subplot(1, 2, 2)
plt.scatter(df[sepal_length_col], df[sepal_width_col], color='red', alpha=0.7)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vsplt.tight_layout()
plt.show()
