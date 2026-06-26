print("===================================")
print("        EXPENSE TRACKER")
print("===================================")


total_spent = 0
expense_count = 0

print("\nEnter your expenses.")
print("Enter 0 to finish.\n")

while True:

    expense = float(input("Enter Expense Amount: ₹"))

    if expense == 0:
        break

    if expense < 0:
        print("Expense cannot be negative.")
        continue
    total_spent = total_spent + expense

    expense_count = expense_count + 1

    print("Expense Added Successfully!")
    print("Current Total = ₹", total_spent)

print("\n===================================")
print("          EXPENSE SUMMARY")
print("===================================")

print("Number of Expenses :", expense_count)
print("Total Amount Spent : ₹", total_spent)

print("\nThank You!")