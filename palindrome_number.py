# Write a Python Program to Check if a Number is a Palindrome or not?
n=int(input("Enter Number to Check Palindrome or Not: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
if temp==rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")    