# Reverse Words in String Python
s = input("Enter String of words : ")
words = s.split(' ')
# string =[]
# for word in words:
# 	string.insert(0, word)
# print('Reversed Word :'," ".join(string))

# OR
p=' '.join(reversed(words))
print(p)