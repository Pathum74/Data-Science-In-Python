#1
n1=int(input('Number1: '))
n2=int(input('Number2: '))
n3=int(input('Number3: '))

def price_avg(p1,p2,p3):
    avg=(p1+p2+p3)/3
    return avg
t=price_avg(n1,n2,n3)
print('Avg: ',t)

#2
arr=[7,77,777,8,88,888,9,99,999]
print(arr)

sum=0
for x in range (len(arr)):
    sum=sum+arr[x]

avg=sum/(len(arr))
print('Avg: ',avg)

#3
arr1=[1,2,3]
arr2=[4,5,6]
arr3=[]

for x in range (len(arr1)):
    sum=arr1[x]+arr2[x]
    arr3.append(sum)
print(arr3)    

#4
# Function to take input from the user
def input_value():
    arr = []
    print("Enter integer values to store. Type 'done' to finish.")

    while True:
        i = input("Enter number: ")
        if i.lower() == 'done':
            break
        try:
            value = int(i)
            arr.append(value)
        except ValueError:
            print("Invalid input! Please enter an integer or 'done' to finish.")
    
    return arr   

# Function to display values
def display_value(a):
    for i in a:  # Iterate directly over the list
        print(i)

# Call the functions
vall = input_value()
display_value(vall)

#5
a=[[2,4,6,8],[1,3,5,7],[8,6,4,2],[7,5,3,1]]
for  x in range (len(a)):
    for y in range(len(a)):
        print(a[x][y],end=' ')
    print()    

#6
student={'admin':123,'name':'abc','course':'ds'}
for key in student:
    print(key,student[key])

