import numpy as np

students = [
    {"name": "Aarav", "marks": [78, 85, 92]},
    {"name": "Diya",  "marks": [55, 61, 48]},
    {"name": "Kabir", "marks": [90, 95, 99]},
]




for s in students:
    total = 0
        
    for marks in s["marks"]:
        total = total + marks
       
    print(f"{s['name']} - {total}")




chats = [
    {"naam": "Amit",  "messages": [3, 5, 2]},
    {"naam": "Priya", "messages": [10, 1]},
    {"naam": "Rahul", "messages": [7, 7, 7, 7]},
]

kul_msg = 0
for c in chats:
    kul_msg = sum(c["messages"])

    print(f"{c['naam']} - {kul_msg}")










    


        
    


        



    





