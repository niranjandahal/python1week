from typing import Text
def upper_case(word):
    print(Text.upper(word))                 #main code to go uppercase
a=input("enter the strings to be uppercase")
upper_case(a)


def reverse(words):
    print(words[len(words)::-1])        #main code to reverse a strng from google
s=input("enter any strins to reverse")
reverse(s)


import math
def fact(n):
    if (n==1):
        return 1
    else:
        return (n*fact(n-1))
a=int(input("enter the no tot find its factorial"))
print(fact(a))