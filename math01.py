import numpy as np

marks = np.array([78, 85, 92, 88, 5])

print(f" mean {marks.mean()}\n median {np.median(marks)}")

temps = np.array([31, 33, 32, 30, 34, 99, 32])
std = temps.std()
mean = temps.mean()

print(f"{np.round((temps - mean) / std, 2)}")


#temp ka sambandh icecream , umbrella ke saath nikalo alag se
# temp ka sambandh tab nikle jab compare kiya jaye temp and season ko icecream aur umbrella ke saath



temperature = np.array([20, 25, 30, 35, 40])
icecream    = np.array([100, 150, 220, 300, 380])
umbrella    = np.array([90, 70, 50, 30, 20])



print(f"correlation between temp and umbrella in number : {np.corrcoef(temperature, umbrella)[0, 1] :.1f}")
print(f"correlation between temp and icecream in number : {np.corrcoef(temperature, icecream)[0, 1] :.1f}")



age    = np.array([25, 32, 47, 51, 62])
salary = np.array([25000, 40000, 60000, 90000, 150000])

print((age - age.min()) / (age.max() - age.min()))
print((salary - salary.min()) / (salary.max() - salary.min()))


qty   = np.array([2, 1, 3, 1])
price = np.array([200, 40, 90, 150])

#bill_total = (qty * price).sum()
total_bill = np.dot(qty, price)

#print(bill_total)
print(total_bill)


