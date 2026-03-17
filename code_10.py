#Question:Program to simulate ATM operations with transaction tracking.
print("Welcome to chaska maksa ATM")
balance=int(input("Enter the intial balance"))
success=0
failed=0
while True:
    print("1)Withdraw,2)Deposit,3)Exit")
    ch=input("choose")
    if ch=="1":
        amount=int(input("Enter the amount"))
        if amount>balance:
            print("Transanction failed")
            failed+=1
        else:
            balance-=amount
            print(amount,"received")
            success+=1
    elif ch=="2":
        deposit=int(input("Enter the amount"))
        balance+=deposit
        print(balance,"amount is there in your account now!")
    elif ch=="3":
            print("Total balance",balance)
            print("Successful transcation",success)
            print("Fquled transcations",failed)
            print("Thank you!Visit again")
            break
    else:
            print("Invalid choice")
            print("Total balance",balance)
            print("Successful transcation",success)
            print("Fquled transcations",failed)
