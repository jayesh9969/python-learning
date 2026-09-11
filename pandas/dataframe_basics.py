from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent

# 1. Dictionary se DataFrame banana
df = pd.DataFrame({
    'naam': ['Aarav', 'Diya', 'Kabir', 'Meera'],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Pune'],
    'marks': [78, 55, 90, 83]
})

print("Poori table:")
print(df)
print("\nShape (rows, columns):", df.shape)
print("\nKabir ka row (loc[2]):\n", df.loc[2])
print("\nMarks column:\n", df['marks'])

# 2. CSV file se DataFrame read karna
df_csv = pd.read_csv(BASE_DIR / 'students.csv')
print("\nCSV Head(3):")
print(df_csv.head(3))
print("\nCSV Info:")
df_csv.info()
print("\nCSV Describe:")
print(df_csv.describe())
