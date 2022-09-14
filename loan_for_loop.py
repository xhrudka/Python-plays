# Get the loan details
money_owed=float(input("How much money do you owe, in dollars?\n"))  #50,000 dollars
apr=float(input("What is the annual percentage rate?\n")) #3%
payment=float(input("What will your montly payment be, in dollars?\n")) # 1,000 dollars
months=int(input("How many months do you want to see result for?\n")) # 24

monthly_rate = apr/100/12

for i in range(months):
    
    if (money_owed - payment < 0):
        print("This is the last payment", money_owed)
        print("You paid off the loan in",i+1,"months")
        break

    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid

    money_owed=money_owed-payment

    print("Paid", payment, "of which", interest_paid, "was interest", end="")
    print("Now I owe", money_owed)
