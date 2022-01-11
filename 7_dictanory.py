# vvicurly bracket is compulsary to make dictonary
niranjan = {'twitter': '76Xy!pENRdCncpE3','google': '#BE7C6B8ueBgx8ts','fb': '!*SCKT=^PYu?+RW3E*','github': 'dhUtmj#%7K7LmCU','linkdin': '5foSW3yAGz9X7G9'}
place=["bagmati","lalbandi","wrc","lamachaur","lumbini","biratnagar"]

print(place[2])            #to print from list its number inside big paranthesis is used

niranjan['microsoft'] = ['uifgbueruifhrui2df'] # adding to the dictonary
print(niranjan['twitter']) #to print something from dictnary its key is used
print(niranjan.get('google'))
print(niranjan.keys())   #to print all keys that refer to dictonary
print(niranjan)
print(place)

blog_post = {'tittle': '11 use of dictonary','body':'bl blah blahhh',"footeer":"made by"}

mridul = {'name': 'mridul dahal','class': 'eight','hobbies': ['badminton','cricket','chess','tt']}
apar = {'name': 'apar sharm','class': 'kindergarden','hobbies': ['coding','sleep','pubg','ff']}

names = [mridul,apar]

for i in names:      #same as line no 8 and 9 in below print statement
    print(i['name']) #here i value is mridul and apar so code print(mridul['names]) 7 print(apar['name'])
    print(i.get('class'))
