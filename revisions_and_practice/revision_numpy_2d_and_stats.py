# nums = [45, 56, 34, 99, 22]

# total = 0
# count = 0
# for n in nums:
#     total = total + n
    
#     count = count + 1
#     avg = total / count



# print(f"your total is {total}\nyour average is {avg}")

# nums.append(43)

# print(nums)
# nums.sort()
# print(nums)
# sorted_nums = sorted(nums , reverse=True)
# print(sorted_nums)

# nums.remove(45)
# print(nums)

# ask_name = input("Whats your name?\n")

# print(f"{ask_name}, Nice name")

# ask_age = int(input("Whats your age\n"))

# if ask_age > 18:
#     print("you are adult")

# else:
#     print("you are underage")


# slice_nums = nums[0:2]

# print(slice_nums)

# def bottom2(nums):
#     bottom = nums[0:2]
#     return bottom
# print(bottom2(nums))

# def top2(nums):
#     nums_sorted = sorted(nums, reverse=True)
#     return nums_sorted[0:2]
# print(top2(nums))

# def find_biggest(nums):
#     biggest = nums[0]

#     for n in nums:
#         if n > biggest:
#             biggest = n
#     return biggest

# print(find_biggest(nums))


# sachin = [0, 30, 50, 100]

# def score(sachin, scores):
#     count = 0
#     for s in sachin:
#         if s >= scores:
#             count = count + 1
#     return f"{count} baar 50 ke upar run banaye sachin ne"

# print(score(sachin, 50))

# while True:
#     virat = 222
#     try:    
#         if sachin > virat:
#             print("sachin won")
        

        
#     except TypeError:
#             print("hi22")

#     break






# student = input("enter name\n")
# marks = int(input("enter marks\n")) 

# with open("marks.txt", "a") as m:
    
#         m.write(f"{student} {marks}")
        

# file_name = "marks.txt"
# line_to_delete = 1  # Line numbers start at 1

# with open(file_name, "r") as file:
#     lines = file.readlines()

# with open(file_name, "w") as file:
#     for index, line in enumerate(lines, start=1):
#         if index != line_to_delete:
#             file.write(line)

# file_name = "marks.txt"
# delete_line = 1
# with open(file_name, "r") as f:
#     lines = f.readlines()
# with open(file_name, "w") as f:
    
#     for index, line in enumerate(lines, start=1):
#         if index != delete_line:
#             f.write(line)



# students = [
#     {"name": "Aarav", "marks": [78, 85, 92]},
#     {"name": "Diya",  "marks": [55, 61, 48]},
#     {"name": "Kabir", "marks": [90, 95, 99]},
# ]


# def topper(students):

#     best_avg = 0  
#     best_name = ""

#     for s in students:
#         m = s["marks"] 
#         avg = sum(m) / len(m)
#         if avg > best_avg:
#             best_avg = avg
#             best_name = s["name"]
#     return best_name  

# print(topper(students))  

# def weakest(students):
#     first = students[0]
#     weak_avg = sum(first["marks"]) / len(first["marks"])
#     weak_name = first["name"]

#     for s in students:
#         m = s["marks"]
#         avg = sum(m) / len(m)
#         if avg < weak_avg:
#             weak_avg = avg
#             weak_name = s["name"]
#     return weak_name

# print(weakest(students))



        
