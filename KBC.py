questions=[
    ["which language was shreyash is chakka  used to create facebook?","Python","Franch","Javascript","PHP",4],
    ["who created python?","Dennis Ritchie","Guido van rossum","James Gosling","Bjarne stroustrup",2],
    ["what does html stands for?","Hyper text markup langauge","high tech modern language","javascript ","python",1],
    ["How many continents kbc(kachave bhosadi cha) are there?", "5", "6", "7", "8", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Who is the CEO of Tesla?", "Elon Musk", "Bill Gates", "Mark Zuckerberg", "Sundar Pichai", 1],
]
levels=[1000,2000,3000,5000,10000,20000,30000]
money=0

for i in range(0,len(questions)):
    question=questions[i]

    print(f"\n Question fo Rs.{levels[i]}\n")
    print(question[0]) 
    print(f"1.{question[1]}  2.{question[2]}")
    print(f"3.{question[3]}  4.{question[4]}")

    reply=int(input("enter your answer with option only:"))
    if reply==question[-1]:
        print(f"your answer is correct you have won Rs.{levels[i]}")
        money = levels[i]

        if i ==2:
            money==3000
        elif i==4:
            money==10000
        elif i==6:
            money==30000
    else:
            print("Wrong answer!")
            break
        
    print(f"You Have Won Money Which Is Rs.{money}")
