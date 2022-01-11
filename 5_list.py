#declare empty list
niranjan=[]
gg=['data1','data2','data3','data4','data5']
print(gg[0])  #accesing the elements from the data

#appending to the empty list
niranjan.append("apar sharma")
niranjan.append("rajesh hamal")
niranjan.append("cococola")
niranjan.append("bagmati")
print(niranjan)
for mridul in niranjan:
    print("the person is",mridul)

niranjan.remove("bagmati")
niranjan.remove("cococola")
print(niranjan)

for mridul in niranjan:
    print("the person is",mridul)