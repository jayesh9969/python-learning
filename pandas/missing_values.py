from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / 'students_dirty.csv')

print("Dirty DataFrame:")
print(df)

print("\nMissing values count (isnull().sum()):")
print(df.isnull().sum())

print("\nDropna (sirf poori rows):")
print(df.dropna())

# Clean missing values: marks with median, city with 'unknown'
d2 = df.copy()
d2['marks'] = d2['marks'].fillna(d2['marks'].median())
d2['city'] = d2['city'].fillna('unknown')

print("\nCleaned DataFrame (fillna):")
print(d2)
print("\nNull check after fillna:")
print(d2.isnull().sum())
