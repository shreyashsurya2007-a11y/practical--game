student=[]
#create a list to store the data of the because it will become is to store in list better then dictionary

while True:
    print("\n----Student Result-----")
    print("1.Add Student:")
    print("2.Check Result :")
    print("3.Delete Result:")
    print("4.EXIT")

    choice=int(input("Enter your choice: "))
    
    if choice==1:
        name=input("enter student name:" )
        seat_no=int(input("enter Student Seat no:"))
        percentage=float(input("Enter the percentage of student:"))
        if percentage>40:
            result="PASS"
        else:
            result="FAIL"
        
        student.append((name,seat_no,percentage,result))
        print("result added succssfully!!")
    elif choice==2:
        if len(student)==0:
            print("no Student is result is found!!")
        else:
            print("-"*60)
            print(f"|{'Sr':<5}|{'NAME':<12}|{'SEAT NO':<14}|{"PERCENTAGE":<15}|{"RESULT":<8}|")
            print("-"*60)

            for i,(name,seat_no,percentage,result) in enumerate(student,1):
                print(f"|{i:<5}|{name:<12}|{seat_no:<14}|{percentage:<15}|{result:<8}|")
                print("-"*60)
    elif choice==3:
        seat=int(input("enter the seat no to delete:"))

        found=False
        for data in student:
            if data[1]==seat:
                student.remove(data)
                found=True
                print("Result successfully removed!!!")
                break

        if not found:
            print("Result is not Founded")
    elif choice==4:
        print("Thank you for visiting")
        break
    else:
        print("Invalid Choice! Please Try Again.")

        




        
        
    

    







