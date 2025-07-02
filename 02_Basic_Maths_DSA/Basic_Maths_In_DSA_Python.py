# some qs

# n = 5873
# print number in reverse form
# last digit is always the reminder
# use the floor divison
# n//10 - 5873%10 = 3
# n//10 - 587%10 = 7
# n//10 - 58%10 = 8
# n//10 - 5%10 = 5
# n//10 - 0

# extraction of digit ---- 1
# how to do this with code
n = 5873
num = n
while num>0:
    last_digit = num%10
    print(last_digit)
    num = num//10


# 
 