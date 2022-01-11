import random

x=int(input("how many times u want to play r/p/s"))

for i in range(x):
    a=input("enter 'r'  'p'  's' for rock paper and scissor :: ")
    pc=['rock','paper','scissor']
    n=random.randint(0,2)
    b=(pc[n])
    if (a=='r' or a=='R') and b=='rock':
        print('tie')
    elif (a=='r' or a=='R') and b=='paper':
        print(f"computer : {b}")
        print('you lose')
    elif (a=='r' or a=='R') and b=='scissor':
        print(f"computer : {b}")
        print('you win')
    elif (a=='p' or a=='P') and b=='paper':
        print(f"tie")
    elif (a=='p' or a=='P') and b=='scissor':
        print(f"computer : {b}")
        print('you lose')
    elif (a=='p' or a=='P') and b=='rock':
        print(f"computer : {b}")
        print('you win')
    elif (a=='s' or a=='S') and b=='paper':
        print(f"computer : {b}")
        print('you win')
    elif (a=='s' or a=='S') and b=='rock':
        print(f"computer : {b}")
        print('you lose')
    else:
        print("tie")
    print("choose again")
        

