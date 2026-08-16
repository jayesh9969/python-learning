import pandas as pd

df = pd.read_csv('students_dirty.csv')




print(df.dropna())

# print(df.fillna(df['marks'].median()))
# print(df['city'].fillna('unknown'))

# null_check = df.isnull().sum()
# print(null_check)


print(df.isnull().sum())
print(df.dropna())


d2 = df.copy()



d2['marks'] = d2['marks'].fillna(d2['marks'].median())
d2['city'] = d2['city'].fillna('unknown')
print(d2)


print(d2.isnull().sum())





    







    

    


