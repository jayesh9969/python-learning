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
    with open("expenses.txt") as f:
        for line in f:
            parts = line.split(",")
            name = parts[0]
            amount = parts[1].strip()
            print(f"{name} - Rs {amount}")

view_expenses()

            
            