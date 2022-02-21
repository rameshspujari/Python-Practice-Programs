# Function to Segregate 0's and 1's in an array list
def segregate(arr):
    res = ([x for x in arr if x==0] + [x for x in arr if x==1])
    print(res)
  
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
segregate(arr)