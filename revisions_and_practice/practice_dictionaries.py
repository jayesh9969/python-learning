# ask the user a username using input method
#loop banao read karo users.txt 
# if else to check username is already there in txt or not
#if it is there show username already taken, try another one if it is not there show signup success
# but new username should be added in list of users.txt


ask_username = input("Please enter your username \n")

with open("users.txt") as f:

    for users in f:
        if ask_username == users.strip():
            print("this username is already taken, try another one")  
            break
    else:
        with open("users.txt", "a") as f:

            f.write(f"{ask_username}\n")

        print("sign up successfull")  


def view_expenses():
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.split(",")
            name = parts[0]
            amount = parts[1].strip()
            print(f"{name} - Rupees {amount}")

view_expenses()
