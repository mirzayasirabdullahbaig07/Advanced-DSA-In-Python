# what is recursion therory

# a function call it self is called resucirton
def greet():
    print("yasir")

    greet()

greet()
# it will become an infinite recursion
# it will show the error of stackoverflow
# python is smart and it is run the program 987 times

# syntax

# def fun():
#     if condition:
#         return
#     # line of codes
#     # line of codes
#     # line of codes
#     fun()

# fun()


# print yasir 4 times using recursion
count = 0
def fun():
    if count == 4:
        return
    print("yasir")
    count = count + 1
    fun()


fun()
# this is head recursion
# jo be ap job krna ha ya phly call kia ha then u call function
#
# tail recursion
count = 0
def fun():
    if count == 4:
        return
    count = count + 1
    fun()
    print("yasir")

fun()