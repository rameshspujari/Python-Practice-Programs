# # Python Program for simple interest Simple Interest = (P x T x R)/100
while True:
    ch=int(input("Enter Choice: 1.Simple Interest 2.Compound Interest\n"))
    if ch==1:
        p=int(input("Enter Price: "))
        t=int(input("Enter Time: "))
        r=int(input("Enter Rate: "))
        sm = (p*t*r)//100
        print("Simple Interest is :", sm)
    
    elif ch==2:
        # # compound nterest. A = P(1 + R/100)t, Compound Interest = A – P 
        principle =int(input("Enter principle: "))
        rate =float(input("Enter rate: "))
        time =int(input("Enter time: "))
        Amount = principle * (pow((1 + rate / 100), time))
        print("Compound interest is :", Amount - principle)
    else:
        print("Invalid Input")

