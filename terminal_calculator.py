x=int(input('''what you want to do
1)add
2)substract 
3)multiply 
4)divid 
'''))
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
if x==1:
    result=num1+num2
elif x==2:
    result=num1-num2
elif x==3:
    result=num1*num2
elif x==4:
    result=num1/num2
else:
    print("invalid option")
