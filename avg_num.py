# write a program to find the average of numbers in a list in Python?
n=int(input("Enter Size: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    avg=sum(a)/n
print("Average of elements in the list",round(avg,2))
