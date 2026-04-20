#wap to find the greatest of four numbers entered by the user
n1=int(input("enter the num1"))
n2=int(input("enter the num2"))
n3=int(input("enter the num3"))
n4=int(input("enter the num4"))
if(n1>n2 and n1>n3 and n1>n4  ):
    print("number 1 is greater then all")
elif(n2>n1 and n2>n3 and n2>n4):
    print("number 2 is greater then all")
elif(n3>n1 and n3>n2 and n3>n4):
    print("number 3 is greatest")
else:
    print("number 4 is greatest")