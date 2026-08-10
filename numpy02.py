import numpy as np
marks = np.array([
    [78, 85, 92], 
    [55, 61, 48], 
    [90, 95, 99]
])

shape = marks.shape
print(shape)


print(f"Diya's second subject marks {marks[1, 1]}")

students = ["Aarav", "Diya", "Kabir"]
avg = marks.mean(axis=1)


for i in range(len(students)):
    print(f"{students[i]}'s average {avg[i] :.1f}")



subjects = ["Maths", "Science", "English"]

sub_avg = marks.mean(axis=0)

for i in range(len(subjects)):
    print(f"{subjects[i]} average {sub_avg[i] :.1f}")


print(avg)
print(sub_avg)

print(f"kabir ka row {marks[2]}")
print(f"second subjects all marks {marks[:, 1]}")

print("pehlo do students ke pehle do subjects\n", marks[0:2, 0:2])


bonus = [5, 0, 10]

diff = marks - marks.mean(axis=0)

print(diff)

sub_std = marks.std(axis=0)
for i in range(len(subjects)):
    print(f"{subjects[i]} ka standard deviation {sub_std[i] :.1f}")


nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

reshaping = nums.reshape(3, 4)
print(reshaping)
print(nums.shape)
print(reshaping.shape)









