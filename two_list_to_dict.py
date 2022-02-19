# # Conversion of two list into Dictionary Using Python
# l1=['R','S','P']
# l2=[1,4,3]
# z=zip(l1,l2)
# print(dict(z))

# OR
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))

# using naive method to convert lists to dictionary
res = {}
for key in test_keys:
	for value in test_values:
		res[key] = value
		test_values.remove(value)
		break
print ("Resultant dictionary is : " + str(res))
