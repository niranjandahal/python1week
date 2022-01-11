def nd(md):
    return print(f"hello!",md)
nd("niranjan")
print(nd("niranjan"))


def concacinate(a,b):
    return f"{a} {b}"
print(concacinate('niranjan','dahal'))


def greet(name,msg="good morning"):
    print("hello",name,"!",msg)
greet("niranjan dahal")
greet("mridul dahal","how do you do")


def wrc(*names):
    for i in names:
        print("hello welcome to wrc",i)   
wrc("apar sharma","'niraj dhakal'",'no name','hacker')
