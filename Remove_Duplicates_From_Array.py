# Remove Duplicates In Python
arr = [1,2,3,3,2,1]

# # Using set function
# print(set(arr))
# print(list(set(arr)))


# # Using Array
# a=[]
# for i in arr:
#     if i not in a:
#         a.append(i)
# print(a)


# # Using Lambda function
# x=lambda arr : set(arr)
# print(x(arr))


# # Using Dictionary
# d1={
#     'car':["A","B","C","B","A","D"],
#     'brand':["Maruthi","Benz","Tata","Suzuki","Tata"]
# }
# d2={}
# for k,v in d1.items():
#     d2[k]=set(v)
# print(d2)


# # Using Symmetric_Difference
# s1={1,2,4,5}
# s2={2,1,5,7}
# d=s1.symmetric_difference(s2)
# print(d)
 
    