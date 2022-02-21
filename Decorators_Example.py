#A decorator in Python is a function that takes another function as its argument and returns yet another function
def main_welcome(fun):
    def sub_welcome():
        print("Welcome to home!")
        fun()
        print("How are you?")
    return sub_welcome()

@main_welcome
def another_welcome():
    print("Welcome all to home!")

# OR OR OR OR
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
# add_15 = create_adder(15)
# print(add_15(10))
