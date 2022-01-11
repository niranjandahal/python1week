# #check prime no using flags as niranjan variable

num=int(input('enter a no to check prime'))
niranjan = False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            niranjan = True
            break
if (niranjan==True):
    print("it isnt prime number")
else:
    print("it is a prime no")



#to list all prime no between given interval

a=int(input("enter lower no"))
b=int(input("enter upper no"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
            
        else:
            print(i)



