name = input("Apna naam batao: ")
age = int(input("age batao: "))



def category():

    if age < 13:
        return "bachpan"
   
    elif age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 59:
        return "Adult"
    else:
        return "Senior citizen"

print(f"{name}, tum {age} saal ke ho - {category()}")

if age >= 18:
    print("Tum vote de sakte ho")

else:
    print(f"Vote ke liye abhi {18 - age} saal baaki hain")