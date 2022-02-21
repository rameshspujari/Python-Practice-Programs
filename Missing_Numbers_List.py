# Python3 program to Find missing integers in list
# a=[1,3,4,5]
# def find_miss_num():
#     n=a[-1]
#     sm1=0
#     total=n*(n+1)//2
#     sm1=sum(a)
#     print("Missing Number :", total-sm1)
# find_miss_num()

          
def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]
lst = [1, 2, 4, 6, 7, 9, 10]
print("Missing Numbes :", find_missing(lst))
print("Missing Numbes Sum :", sum(find_missing(lst)))