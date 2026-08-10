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





