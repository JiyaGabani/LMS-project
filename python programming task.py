#store and print name,age and city
name=input("enter your name:")
print("hello",name)

age=input("enter your age:")
print("your age is",age)

city=input("enter your city:")
print("my city name is",city)

#swap two variable
x=25
y=30
x,y=y,x
print(x)
print(y)

#find square and cube of number
number=int(input("enter a number:"))
print("square:",number**2)
print("cube:",number**3)

#convert temperature
c=int(input("enter a temperature:"))
print(((c*1.8)+32),"farenheit:")

#simple calculator
x=int(input("enter a no:"))
y=int(input("enter a no:"))

print("add:",x+y)
print("sub:",x-y)
print("multiply:",x*y)
print("devision:",x/y)

#find remider using %
x=int(input("enter a no:"))
y=int(input("enter a no:"))
print("reminder",x%y)

#calculate are of rectangle/circle
l=int(input("enter a length"))
b=int(input("ente a breadth"))
print("area of rectangle:",l*b)
pi=22/7
r=int(input("enter  a radius"))
print("area of circle:",pi*r**2)

#calculate simple intrest
p=int(input("enter the principle amount:"))
r=int(input("enter the rate of interest:"))
t=int(input("enter the time of period in years:"))
print("simple interest:",(p*r*t)/100)

#print frist five elements

a=input("enter a value")
print(a[0:5])

#check equal number between two inputs

a=int(input("enter a no:"))
b=int(input("enter a no:"))
if a==b:
    print(a, "is equal to", b)
else:
    print(a, "is mot equal to", b)

#voting eligibility
age=int(input("enter your age:"))
if age>=18:
    print("you are eligiblr for voting")
else:
    print("you are not eligible for voting")

#check greater number between two inputs

a=int(input("enter a no:"))
b=int(input("enter a no:"))
if a>b:
    print(a, "is greater than", b)
else:
    print(b, "is greater thsn", a)

#find largest of 3 number
num1=int(input("enter a first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter a third number:"))
if num1>=num2 and num1>=num3:
    print(f"the largest number is {num1}")
elif num2>=num1 and num2>=num3:
    print(f"the largest number is {num2}")
else:
    print(f"the largest number is {num3}")

#check pass or fail
marks=int(input("enter your marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")

#check if number is between 1-100
number=int(input("enter a number:"))
if number>0 and number<100:
    print("it is between")
else:
    print("it is not between")

#check leap year
year=int(input("enter a year:"))
if year%4==0 and year%100!=0 and year%400!=0:
    print("it is leap year")
else:
    print("it is not leap year")

#check if number is divisible by 3 and 5

n=float(input("enter a no:"))
if n%3==0 and n%5==0:
    print("it is devisible")
else:
    print("it is not devisible")

#valid input
age=int(input("enter your age:"))
city=int(input("enter your city:"))
if age>=18:
    print("major")
else:
    print("minor")
if city=='surat':
    print("person is from surat")
else:
    print("person is not from surat")

#increment and decrement a numer
n=int(input("enter a number:"))
a=int(input("how much want to add"))
d=int(input("how much want to decrese "))
print("after increment:",n+a)
print("after decrement:"n-d)

  
