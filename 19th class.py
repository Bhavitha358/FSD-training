num=int(input("Enter the number:"))
rev=0
temp = num
while num>0 :
    rem= num%10
    rev = rev*10+rem
    num= num/10
if (temp==rev) :
    print("PALINDROME")
else:
    print("NOT PALINDROME")

---------------------------------------------------------------------------------------------------------------
fig = input("Enter the type of the figure: ")
if fig=="triangle" :
    base = int(input("Enter the base:"))
    height = int(input("enter the height:"))
    print("Area of triangle is: ",0.5*base*height)

if fig == "rectangle" :
    l = int(input("Enter the length:"))
    b = int(input("Enter the breadth:"))
    print("Area of the rectangle is :",l*b)
    
if fig== "square" :
    side = int(input("Enter the side:"))
    print("Area of the square is :",side*side)
    -------------------------------------------------------------------------------------------------------------
nums = int(input("Enter three nums:"))
if(a<b and a<c):
    if(b<c) :
        print(a,b,c)
    else:
        print(a,c,b)
    temp=a
    a=b
    b=temp
if(b>c) :
    temp=b
    b=c
    c=temp
print(a,b,c)
----------------------------------------------------------------------------------------------------------------
n = int(input("Enter the number:"))
a=0
b=1
print(a,b,end=" ")
c=a+b
for i in range(n) :
    c=a+b
    print(c,end=" ")
    a=b
    b=c