# scripts/preview_meta_first20.py
# Displays and saves the first 20 rows of cars_meta.csv

import pandas as pd
import os

# Set path directly to cars_meta.csv
meta_path = r"D:\cars_project\cars_meta.csv"

# Verify the file exists
if not os.path.exists(meta_path):
    raise FileNotFoundError(f"cars_meta.csv not found at {meta_path}")

# Read CSV
df = pd.read_csv(meta_path)

# Display first 20 rows
print("\n=== Preview: First 20 rows of cars_meta.csv ===\n")
print(df.head(20).to_string(index=False))

# Save preview for documentation
preview_path = r"D:\cars_project\reports\cars_meta_preview.csv"
os.makedirs(os.path.dirname(preview_path), exist_ok=True)
df.head(20).to_csv(preview_path, index=False)
print(f"\nPreview saved to {preview_path}")
