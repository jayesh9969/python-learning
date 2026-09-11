from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / 'students.csv')
att = pd.read_csv(BASE_DIR / 'attendance.csv')

# Merge students with attendance using left join on 'naam'
merged = pd.merge(df, att, on='naam', how='left')
print("Merged students + attendance (LEFT JOIN):")
print(merged)
