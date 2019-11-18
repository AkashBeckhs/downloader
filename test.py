
def checkPerfectRootIfExists(num):
    x=int(num/2)
    for i in range(2,x+1):
        root=num**(1/i)
        if root**root==num:
            return "Yes"
    return "No"

def checkPandatic(num):
    if num=='Yes':
       return "Yes"
    if num==1:
        return "Yes"

    if checkPerfectRootIfExists(num) == "Yes":
        return "Yes"
    possibleValues=list()
    temp=str(num)
    for i in range(len(temp)):
        t=num-int(temp[i])**2
        x=checkPerfectRootIfExists(t)
        if x!='Yes':
            checkPandatic(t)
        else:
            return 'No'
   

    

x=checkPandatic(13)
print(x)

    

