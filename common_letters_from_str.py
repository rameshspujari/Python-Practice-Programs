# Find out common letters between two strings Using Python
def common_letters():
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")
    print(set(s1)&set(s2))
common_letters()