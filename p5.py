# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest = 0
num = 1
flag = False
while 1:

    for i in range(1,21):
        if num % i != 0:
            flag = False
            break
        elif num % i == 0:
            flag = True
    if flag == True:
        smallest = num
        break
            
    num += 1

print(smallest)



