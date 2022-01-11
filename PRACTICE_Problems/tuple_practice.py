#Tuples cant be changed after it is created : niranjan dahal 2021
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000)) #take long time
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)) #take short time 

first_tuple=('a','b','c','d','e','j','f')
# print(first_tuple)

my_list=first_tuple
# print(my_list)

second_tuple=(1,2,3,4,5,9,8,7,55)
nd=second_tuple[2:7]               #print from the second index 
md=second_tuple[::2]          #begining to the end with step of the 2

third_tuple="niranjan","20","male","youtuber"
name,age,gender,work=third_tuple          #packing/unpacking tuple
# print(name,age,gender,work)


