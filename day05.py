list1 = [12, 7, 30, 5, 18]
list2 = [-5, -12, -30]
list3 = [100]


def find_biggest(numbers):
    
    biggest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

print(f"biggest number in list1 is {find_biggest(list1)}")
print(f"biggest number in list2 is {find_biggest(list2)}")
print(f"biggest number in list3 is {find_biggest(list3)}")

def find_smallest(numbers):
    smallest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest

print(f"smallest number in list1 is {find_smallest(list1)}")
print(f"smallest number in list2 is {find_smallest(list2)}")
print(f"smallest number in list3 is {find_smallest(list3)}")


def average(numbers):
    count = 0
    total = 0

    for n in numbers:
        total = total + n
        count = count + 1
    return total / count

print(f"Average of list1 is {average(list1)}")
print(f"Average of list2 is {average(list2)}")
print(f"Average of list3 is {average(list3)}")


marks = [78, 42, 90, 35]



def count_pass(marks, passing):
    count = 0
    for m in marks:
        if m >= passing:
            count = count + 1
    return count


print(count_pass(marks, 35))
print(count_pass(marks, 50))
print(count_pass(marks, 90))
    