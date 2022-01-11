import math

# n=int(input("enter any not ot find the factorial"))
def fact(x):
    if x==0:
        return 1
    else:
        return (x*fact(x-1))

print(fact(5))
