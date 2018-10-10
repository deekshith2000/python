def add(a,b):                         #function to add
    return (a+b)
def sub(a,b):                          
    return (a-b)
def mul(a,b):
    return (a*b)
def divide(a,b):
    if(b==0):
        print("divide by zero error")
        return 0
    else:
        return (a/b)
print('\n\t\t\t SIMPLE CALCULATOR\n')
while 1:
    print('which operation you want to ?\n')
    print('1.addition\n2.subtraction\n3.multiplication\n4.division\n')
    ch=int(input('ENTER YOUR CHOICE\n'))
    a=float(input("Enter first number\n"))
    b=float(input("Enter second number\n"))
    
    if ch is 1:                        #is also used as equality operator
        print("ans=",add(a,b))
    elif(ch==2):
        print("ans=",sub(a,b))
    elif(ch==3):
        print("ans=",mul(a,b))
    elif(ch==4):
        print("ans=",divide(a,b))
    else:print("improper choice\n")
