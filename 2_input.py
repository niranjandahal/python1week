# a=int(input("enter the no"))
# b=int(input("enter the no "))
# sum=a+b
# print(f"the sum is {sum}")

# num = [1,2,3,4,5,6,7,8,9,10]
# for i in num: #for variable in list and inside loop only variable can be used not list
#     print(i*i)

# for i in range(1,11):
#     print('square of a number is',i**2)


a=int(input("enter the no to show table"))
b=int(input("enter no up to which should be multiply"))
for i in range(1,b+1):
    print(a,"*",i,"=",a*i)