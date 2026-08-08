nums = [5, 12, 8, 20]

total = 0
biggest = nums[0]
count = 0

for n in nums:
   
    total = total + n
    count = count + 1
    avg = total / count
    
if n > biggest:
    biggest = n

print(f"Your total is {total}")
print(f"Your average is {avg}")
print(f"biggest number in the list is {biggest}")


