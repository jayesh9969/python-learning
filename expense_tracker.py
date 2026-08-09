# step 1 pehle view_expense() function banao
# step 2 variable banao loop lagao split karo
# step 3 phir strip karo quotes kachra hatao
# step 4 int me convert karo return karo  print karo
# updated
# step 1: function view_expenses() banao
# step 2: file kholo (with open ... as f)
# step 3: har line par loop
# step 4:     split karo comma se → ['chai', '20\n']
# step 5:     naam aur amount alag nikalo, strip karo
# step 6:     f-string se print karo

def view_expenses():
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.split(',')
            name = parts[0]
            amount = parts[1].strip()
            print(f"{name} - Rs {amount}")



def show_summary():
    total = 0
    count = 0
    max_amount = 0
    max_name = ""

    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.split(',')
            amount = int(parts[1].strip())
            total = total + int(amount)
            count = count + 1
            average = total / count
            if amount > max_amount:
                max_amount = amount
                max_name = parts[0]
                
            
        print(f"Total expenses : {total}\nAverage: Rs {average}\nMost expensive: {max_name} : {max_amount}")
        


#user se input lo
#with open se file open karao
#loop lagao while so user can reenter the amount again if entered string
#if else se coffee item add karo wrong input (string) dalne par else me phir se number dalne bolo
#write() method se input save karo
#input ko print karo
#function ko call karo

# naam poochho (ye kabhi fail nahi hoga - kuch bhi likho, text hai)
# while True:
#     try:
#         amount poochho aur int() mein badlo
#         break                          ← sahi number mila, loop khatam
#     except ValueError:
#         "sirf number daalo" print karo  ← loop dobara chalega
#
# file "a" mode mein kholo
# naam + "," + amount + "\n" likho
# confirmation print karo
# function ko bahar se call karo


def add_expense():
    
    name = input("which expense \n")
    
    while True:
        try:
            amount = int(input("how many rupees? \n"))
            break
        except ValueError:
            print("enter only number")


    with open("expenses.txt", "a") as f:
            f.write(f"{name},{amount}\n")

            print(f"{name} - Rs {amount} is added")
        


            

                
                        
     
                        
                
# while loop jo har baar menu dikhaye
# user ke input pe tay hoga use kya chahiye view expenses, summary etc.
#if elif else decide karega kya dikhana hai
#4th choice par break lagao
#last me print hoga jo user ne decide kiya tha

while True:
    choice = int(input("Menu : enter 1 to view expenses\n enter 2 to see summary\n enter 3 to add new expense\n enter 4 to exit\n"))
    

    if choice == 1:
        view_expenses()
    elif choice == 2:
        show_summary()

    elif choice == 3:
        add_expense()

    elif choice == 4:
        break
print("exited")
    
    


        