a = int(input('enter 1st no '))
b = int(input('enter 2nd number'))
c = int(input("enter 3rd no"))
if (a > b and a > c):
    print('1st number is largest among three no')
elif (b > a and b > c):
    print('2nd number is largest among three no')
else:
    print('3rd number is largest among three no')


# very easy lets do the prime checking using if else for loop start at 1:32 pm at lalbandi,sarlahi

num = int(input("enter no to check prime or not"))

if num > 1:  # prime no are always greater than one
    for i in range(2, num):
        if(num % i == 0):
            print("it isnot prime number")
            print(i, "times the", (num/i), "is equal to", num) # watch this line carefully
            break
        else:
            print("number is prime number")
            break
else:
    print("number cant be negative or 0,if you enter 1 you are fool")
