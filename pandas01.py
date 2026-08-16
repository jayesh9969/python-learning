import pandas as pd

# df = pd.DataFrame({
#     'naam' : ['Aarav', 'Diya', 'Kabir', 'Meera'],
#     'city' : ['Delhi', 'Mumbai', 'Delhi', 'Pune'],
#     'marks' : [78, 55, 90, 83]
# })


# print(f"poori table\n{df}")
# print(f"{df.shape}")
# print(f"kabir ka row\n{df.loc[2]}")
# #print(df.loc[:,'marks'])
# print(df['marks'])

df = pd.read_csv('students.csv')

# print(df.head(3))
# df.info()
# print(df.describe())

# for n, m in df.groupby('naam')['marks']:   
#     if int(m) > 80:   


#         print(f"{n}\n")

# print(df[df['marks'] > 80])
# average_city = df.groupby('city')['marks'].mean()
# print(f"{average_city}")
# print(df['marks'].mean())
# print(df.sort_values('marks').head(3))

att = pd.read_csv('attendance.csv')

print(pd.merge(df, att, on='naam', how='left'))
att1 = att['days_present'].astype('int64')

# att1 = att['days_present'].astype('int64')






    

   