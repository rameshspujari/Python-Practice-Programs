# Find Out Pairs with given sum in an array in python
def find_pairs(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>target):
            right=right-1
        
        elif(arr[left]+arr[right]<target):
            left=left+1
        
        elif(arr[left]+arr[right]==target):
            print("Target Pairs Are : ", [arr[left],arr[right]])
            right=right-1
            left=left+1
        
# arr=[5,7,4,3,9,8,19,21]
arr=[]
n=int(input("Enter Elements Size : "))
for i in range(0,n):
    ele=int(input("Enter Elements : "))
    arr.append(ele)
# target=10
target = int(input("Entr Target Sum : "))
find_pairs(arr,target)
