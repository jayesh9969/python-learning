import numpy as np
marks = np.array([45, 88, 72, 30, 95]) + 5



print(marks)

above50 = marks[marks > 50]
print(above50)
position = marks.argmax()

print(position)


#total = sum(marks)
total = marks.sum()
average = marks.mean()
#average = sum(marks) / len(marks)


print(total)
print(average)