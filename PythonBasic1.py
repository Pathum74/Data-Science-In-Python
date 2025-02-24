#1
name=input('Enter name:')
byear=int(input('Birth year:'))

age=2025-byear
print(f'{name} is {age} years old.')

#2
#Display z=x^y
x=int(input('X value: '))
y=int(input('y value: '))
z=x**y
print(z)

#3
#Program to input 2 numbers and display highest number
n1=int(input('Number1: '))
n2=int(input('Number2: '))

if(n1>n2):
    high=n1
else:
    high=n2
print('Highest number: ',high)        

#4 Give grade for given marks
marks=int(input('Enter your marks: '))

if(marks>100):
    print('Marks need to be below 100')
elif(marks>=75):
    grade='A'
elif(marks>=65):
    grade='B'
elif(marks>=50):
    grade='C'
elif(marks>=35):
    grade='S'
else:
    grade='F'

print(f'Marks: {marks}\nGrade: {grade}')
                        

#5 Input 3 numbers and display the largest number:
n1=int(input('Enter number1: '))
n2=int(input('Enter number2: '))
n3=int(input('Enter number3: '))

largest=0

if(largest<n1):
    largest=n1
if(largest<n2):
    largest=n2
if(largest<n3):
    largest=n3

print(f'Largest number is {largest}')            

#6 Display 1,2,3,...,100
x=1
while(x<=100):
    print(x)
    x+=1

#7 Display 100,90,80,...,10
x=100
while(x>=10):
    print(x)
    x-=10    

#8 Display 5,10,15,...,100
x=5
while(x<=100):
    print(x)
    x+=5 

#9 Input 10 numbers and display the value is positive,negative,zero 
x=1 
p=0
n=0
z=0
while(x<=10):
    value=float(input(f"Enter number {x}:"))
    
    if(value>0):
       p+=1
    elif(value<0):
       n+=1
    else:
       z+=1

    x+=1


print(f'Positive count: {p}')
print(f'Negative count: {n}')
print(f'Zero count: {z}')