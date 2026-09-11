marks = [78, 42, 90, 35, 61]
print(f"first {marks[0]}, last {marks[-1]}, third{marks[2]}")




print(f"first slice {marks[0:3]}, second slice {marks[3:5]}")

marks.remove(35)
marks.append(55)
marks.append(88)
print(marks)


if 90 in marks:
    print("it is there")

else:
    print("not there")

ulti = sorted(marks, reverse=True)
print(ulti)
print(marks)

def top_three(nums):
    
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[0:3]

print(top_three(marks))




    

