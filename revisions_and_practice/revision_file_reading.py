def view_expenses():
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.split(',')
            name = parts[0]
            amount = parts[1].strip()
            print(f"{name} - $ {amount}")

view_expenses()