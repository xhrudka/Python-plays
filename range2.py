total = 0
expenses = []
num_expenses = int(input("Enter # for expenses: "))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, sep='')