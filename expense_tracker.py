FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")

    file = open(FILE_NAME, "a")
    file.write(f"{date},{category},{amount}\n")
    file.close()

    print("Expense Added Successfully!")

def view_expenses():
    try:
        file = open(FILE_NAME, "r")

        print("\nDATE\t\tCATEGORY\tAMOUNT")

        for line in file:
            data = line.strip().split(",")
            print(data[0], "\t", data[1], "\t", data[2])

        file.close()

    except FileNotFoundError:
        print("No expenses found!")

def generate_report():
    total = 0

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")
            total += float(data[2])

        file.close()

        print("\n===== REPORT =====")
        print("Total Expense =", total)

    except FileNotFoundError:
        print("No expenses found!")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        generate_report()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")