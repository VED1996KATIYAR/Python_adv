def balance1(balance):
    
    print(f"The balance in your account is {balance}")

def deposit1(deposit):
    global balance
    if deposit <= 0:
        print("Invalid amount. Deposit must be greater than 0")
    else:
        balance+=deposit
        print(f"Successfully deposited {deposit} now balance is {balance}")

def withdraw1(amount):
    global balance
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance-=amount
        print(f"Successfully withdrew {amount} now balance is {balance}")
        

print("Welcome to the bank of idios")    
balance=200000
while True:
    print("1.CHECK BALANCE")
    print("2. DEPOSIT THE AMOUNT")
    print("3.WITHDRAW THE AMOUNT")
    print("4.QUIT IT")
    choice=int(input("Enter the choice"))
    if choice==1:
        balance1(balance)
    elif choice==2:
        deposit=float(input("Enter the amount to be deposited"))
        deposit1(deposit)
    elif choice==3:
        amount=float(input("Enter the amount to withdraw"))
        withdraw1(amount)
    elif choice==4:
        break
    else:
        print("Invalid choice")

print("Thanks for choosing the platform")    