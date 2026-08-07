nums = [33, 22, 55]

biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
print(biggest)

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n
print(smallest)


education = {"harman": "B.tech", "noah": "BSC", "shahid": "BA"}

print(f"noah ka qualification {education["noah"]} hai")

print(type(education))
total = 0
multi = 0
divi = 0
sub = 0
count = 0
for n in nums:
    total = total + n
    
    multi = n * n
    divi = n / n
    sub = n - n
    count = count + 1
    avg = total / count

print(total)
print(multi)
print(divi)
print(sub)
print(avg)


if education.__contains__("harman"):

    print(education.get("harman"))


total = 0

while True:
    num = int(input())
    if num == 0:
        break
    total = total + num
print(total)

num1 = int(input())


for i in range(1, 11):

    print(num1 * i)


    

age = [22, 55, 99, 44]

def find_oldest(numbers):
    oldest = numbers[0]
    for n in numbers:
        if n > oldest:
            oldest = n
    return oldest
print(find_oldest(age))


def find_young(numbers):
    youngest = numbers[0]
    for n in numbers:
        if n < youngest:
            youngest = n
    return youngest

print(find_young(age))

nums = [33, 43, 77, 88]
def avg(numbers):
    count = 0
    total = 0
    for n in numbers:
        total = total + n
        count = count + 1
    return total / count
print(f"average is {avg(nums)}")

marks = [22, 45, 47, 88, 90]

def passing(marks, passing):
    count = 0
    for m in marks:
        if m >= passing:
            count = count + 1
    return count

print(passing(marks, 40))

def fail(marks):
    count = 0
    for m in marks:
        if m < 35:
            count = count + 1
    return count

print(fail(marks))

marks.append(33)
marks.remove(22)
print(marks)

ulta =sorted(marks, reverse=True)
print(ulta)
marks.sort()
print(marks)

print(f"slice of marks {marks[0:2]}")

def top_3_marks(number):

    sorted_nums = sorted(number, reverse=True)
    return sorted_nums[0:3]

print(f"Tope 3 marks: {top_3_marks(marks)}")

def last_2_marks(number):

    sorted_nums1 = sorted(number, reverse=False)
    return sorted_nums1[3 : 5]

print(last_2_marks(marks))


if 33 in marks:
    print("available")

else:
    print("not available")



food_prices = [
    {"item" : "pizza", "price" : 200},
    {"item" : "croissont", "price" : 170},
    {"item" : "pasta", "price" : 190}
]

ask = str(input("what would you like to have?\n"))
for food in food_prices:
    
    if food['item'] == ask:
        break

print(f"your {food['item']} is ready")

customers = {"name" : "manish", "payment" : 1000}

for key, value in customers.items():
    print(f"{key} : {value}")


students = [
    {"name": "Aarav", "marks": [78, 85, 92]},
    {"name": "Diya",  "marks": [55, 61, 48]},
    {"name": "Kabir", "marks": [90, 95, 99]},
]

for s in students:
    m = s['marks']

    avg = sum(m) / len(m) 
    print(f"{s['name']} : {avg : 1f}")


def topper(students):
    best_avg = 0
    best_name = ""

    for s in students:
        m = s['marks']
        avg = sum(m) / len(m)

        if avg > best_avg:
            best_avg = avg
            best_name = s['name']
    return best_name

print(topper(students))
try:
    age = int(input("Age batao: "))
    print(f"Agle saal {age + 1} ho jaoge")
except ValueError:
    print("hi")