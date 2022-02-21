# Python code to get positive & negetive element from list of list
# Input = [[10, -11, 222], [42, -222, -412, 99, -87],[2,-1,4]]
Input = [[42, -222],[1,-2,5],[-412, 99, -87]]
Output = []
Negetive = []
for elem in Input:
	temp = []
	Neg = []
	for x in elem:
		if x>0:
			temp.append(x)
		else:
		    Neg.append(x)
	Negetive.append(Neg)
	Output.append(temp)

print("Initial List is :", Input)
print("Only Positive :", Output)
print("Only Negetive :", Negetive)

