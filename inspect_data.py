
import pandas as pd
from pathlib import Path

# Find CSV files in the project folder
files = list(Path(".").glob("*.csv"))

if not files:
    print("No CSV found. Extract the ZIP and copy its CSV into this folder.")
else:
    for file in files:
        print("\nFile:", file.name)

        try:
            df = pd.read_csv(file, nrows=100, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file, nrows=100, encoding="latin-1")

        print("Columns:")
        print(df.columns.tolist())

        print("\nFirst 5 rows:")
        print(df.head().to_string())

        print("\nDataset size (first 100 rows loaded):", len(df))
