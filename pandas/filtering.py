from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / 'students.csv')

# Boolean filtering (marks > 80)
print("Marks > 80 wale students:")
print(df[df['marks'] > 80])

# Sorting by marks
print("\nTop 3 lowest marks:")
print(df.sort_values('marks').head(3))
