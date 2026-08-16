import pandas as pd, sqlite3

con = sqlite3.connect('school.db')

# print(pd.read_sql('SELECT * FROM students', con))

# print(pd.read_sql("SELECT naam, marks FROM students WHERE city = 'Mumbai'", con))

# print(pd.read_sql("SELECT naam, marks FROM students WHERE city = 'Delhi' ORDER BY marks DESC LIMIT 2", con))

print(pd.read_sql("SELECT s.naam, s.city, a.days_present FROM students s LEFT JOIN attendance a ON s.naam = a.naam", con))