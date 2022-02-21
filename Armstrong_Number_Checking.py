# Check Given Number is Armstrong or Not in Python
# Ex: 153 => 1*1*1 + 5*5*5 + 3*3*3 = 153
num = int(input("Enter Number :"))
x=num
n=len(str(num))
sm=0
while(num>0):
    rem=num%10
    sm=sm+rem**n
    num=num//10
if x==sm:
    print("Armstrong Number:")
else:
    print("Not Armstrong Number:")
