#1
x=1
while(x<=10):
    print(x)
    number=int(input(f"Enter number{x}"))
    
    if number %2==0:
        print(f"{x} is Even")
    else:
        print(f"{x} is Odd")
    x+=1


#2
for x in range (1,11):
    print(x)
#3

for x in range(100,0,-1):
    print(x)

#4

for x in range(2,100,+2):
    print(x)

#5

for x in range(100,4,-5):
    print(x)

#6

for x in range(1,6):
    for y in range(1,6):
        print(y,end=" ")
    print()


#7
num1=int(input(f"Enter number 1 :"))
num2=int(input(f"Enter number 2 :"))
num3=int(input(f"Enter number 3 :"))

maxx=max(num1,num2,num3)
minn=min(num1,num2,num3)
print('Max: ',maxx,'\n','Min: ',minn)            

#8
import math
num=int(input("Enter:"))
sqrtt=math.sqrt(num)
print(sqrtt)

#9
def display():
    print('My name is x and i\'m y years old')

display()    

#10
def display(name,age):
    age=2025-age
    print(f'Name: {name} \nAge: {age}')
display('x',2003)    

#11
def display(num1,num2):
    print('Highest value: ',max(num1,num2))
display(2000,2003)    