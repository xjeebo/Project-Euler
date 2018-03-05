# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest = 0
num = 1      # number that is checked for divisibility
flag = False
while 1:

    for i in range(1,21): # check from 1 - 20
        if num % i != 0:  # check if the val is not divisible from any num from 1 - 20
            flag = False  # exit loop right away if so
            break
        elif num % i == 0:
            flag = True
    if flag == True:      # if it never terminates early, then the smallest is found
        smallest = num
        break
            
    num += 1 # check next value

print(smallest)



