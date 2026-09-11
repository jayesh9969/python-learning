student = {"name": "Aarav", "age": 20, "marks": [78, 85, 92]}
print(f"{student['name']} ki age {student['age']} hai")

student["city"] = "Delhi"
student["age"] = 21

print(student)

print(student.get("phone", "N/A"))


for key, value in student.items():
    print(f"{key}: {value}")  


students = [
    {"name": "Aarav", "marks": [78, 85, 92]},
    {"name": "Diya",  "marks": [55, 61, 48]},
    {"name": "Kabir", "marks": [90, 95, 99]},
]

for s in students:
    m = s['marks']
    avg = sum(m) / len(m)


    print(f"{s['name']}: {avg:.1f}")

def topper(students):
    best_avg = 0
    best_name = ""

    for s in students:
        m = s["marks"]
        avg = sum(m) / len(m)

        if avg > best_avg:
            best_avg = avg
            best_name = s["name"]

    return best_name

print(f"Topper is {topper(students)}")

def weakest(students):
    first = students[0]

    weak_avg = sum(first["marks"]) / len(first["marks"])
    weak_name = first["name"]

    for s in students:
        m = s['marks']
        avg1 = sum(m) / len(m)

        if avg1 < weak_avg:
            weak_avg = avg1
            weak_name = s['name']

    return weak_name

print(weakest(students))

marks = [78, 42, 90, 35]
pass_marks = [m for m in marks if m >= 50]

print(pass_marks)


      

    
