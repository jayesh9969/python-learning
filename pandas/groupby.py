from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / 'students.csv')

# Groupby city and calculate average marks
average_city = df.groupby('city')['marks'].mean()
print("City wise average marks:")
print(average_city)

print("\nOverall average marks:", df['marks'].mean())
