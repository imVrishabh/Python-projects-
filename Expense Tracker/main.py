# Expense Tracker Project

expenses = []  #list of all expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya karo")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice"))

# ADD Expenses 

    if(choice ==1):
        date= input("Date of Expense")
        category= input("Type of Expense (Food, Travel, Makeup, Etc.)")
        description= input("Detail about expense")
        amount= input("How Much you spent")

        expense={
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)
        print("\n Expense is added succesfully")

# 2. View all Expenses
    elif(choice ==2):
        if( len(expenses)==0):
            print("No Expenses Added.")
        else:
            print("===== Your Total Expense =====")
            count=1
            for eachExpense in expenses:
                    print(f"Expense Number {count} -> {eachExpense["date"]}, {eachExpense['category']}, {eachExpense[description]}, {eachExpense['amount']}")
                    count= count+1


# 3. View Total Expense
    elif(choice ==3):
        total=0
        for eachExpense in expenses:
              total = total + eachExpense['amount']
    
        print("\n TOTAL EXPENSE = ", total)
    

# 4. EXIT
    elif(choice ==4):
         print("Thanks for using this system")
         break
    else:
         print("INVALID CHOICE. TRY AGAIN")
