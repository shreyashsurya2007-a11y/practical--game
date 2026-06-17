balance=10000
correct_pin=9701
try:
    pin=int(input("enter the pin :"))

    if pin!= correct_pin:
        raise Exception("Invalid pin!!")
    while True:
    
        print("\n ATM machine")
        print("1.check balance")
        print("2.Deposite money")
        print("3.Withdraw money")
        print("4.Exit")

        choice=int(input("Select your choice :"))

        if choice==1:
            print("Current balance:",balance)

        elif choice==2:
            amount=float(input("enter the amount to deposite:"))
            if amount<=0:
                raise ValueError("Amount must be greater then zero or valid amount!!")
            
            balance+=amount

            print("Deposite succesfully")
            print("current balance:",balance)
        elif choice==3:
            amount=float(input("enter amount to withdraw:"))
            if amount>balance:
                raise Exception("insufficient balance!!")
            
            
            balance-=amount
            print("amount withdrawed ")
            print("remaining balance:",balance)

        elif choice==4:
            print("thank you for using our bank ")

        else:
            print("invalid number!!!")
    
except ValueError as e:
    print("Error :",e)
        

except Exception as e:
    print("Error :",e)


        

