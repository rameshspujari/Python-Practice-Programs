# Write a program to reverse a number in Python?
n = int(input("Enter Number: "))
rev = 0
while(n>0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
print(rev)  

# OR
# print(str(n)[::-1])