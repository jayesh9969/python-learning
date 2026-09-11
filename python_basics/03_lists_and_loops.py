
for n in range(1,11):
    print(n)


marks = [78, 85, 92, 55, 61, 42, 35]
total = 0
count = 0
for m in marks:
    total = total + m
    count = count + 1   
average = total / count
print(total)
print(average)



for passs in marks:
    
    if passs > 50:
        print(passs)

total = 0
while True:
    number = int(input())
    if number == 0:
        break
    total = total + number

print(f"Tumhara total: {total}")

num = int(input())
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
