#Step1 read all numbers
#Step2 compare numbers with other numbers
#Step3 while comparing cross mark the number which is smaller than the other one
#Step4 keep comparing and marking numbers until you reach last number
#Step5 the remaining last number is your biggest of all of the numbers 

numbers = [12, 7, 30, 5, 18]

biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n
    
print(f"biggest number is {biggest}")


smallest = numbers[0]

for s in numbers:
    if s < smallest:
        smallest = s

print(f"smallest number is {smallest}")


a = 12
b = 7

if a > b :
    print(f"bada number {a}")

else:
    print(f"bada number {b}")

