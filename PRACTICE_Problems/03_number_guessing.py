import random
n=int(input("enter the higher limit for guessing"))
a=int(input("enter the no of moves u required or enter 0 to have unlimited try"))

if a==0:
    guess=random.randint(1,n)
    nd=0
    while nd!=guess:
        nd=int(input(f"guess a no between 1 to {n} to match"))
        if nd>guess:
            print("your guess is too high")
        elif nd<guess:
            print("your guess is too low ")
        else:
            print("CONGRATS!!! you have the game against a bot")

else:
    guess=random.randint(1,n)
    i=0
    while (i<a):
        md=int(input(f"guess a no between 1 to {n} to match"))
        i=i+1
        if md>guess:
            print("your guess is too high")
        elif md<guess:
            print("your guess is too low ")
        else:
            print("CONGRATS !!! u won the game within your desired moves")
print(f"you didnt guess no correctly within the {a} no of moves ! try again")





