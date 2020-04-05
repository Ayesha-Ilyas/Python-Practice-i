#fn=fn-1+fn+2

a=0
b=1
x=int(input("enter the num :"))
if x<0:
    print("invalid num ")
elif x==0:
    b=a
else:
    for i in range(0,x-1):
        c=a+b
        a=b
        b=c
        print("the output fabonacci num: ",b)
