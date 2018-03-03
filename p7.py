# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13
# What is the 10001st prime number?

num = 1
flag = False
cnt = 0 # the number of prime numbers found


# 2 is the 1st prime number so the cnt < 10000 is finding the 10001th including the 2
while cnt < 10000: 
    i = 2 # reset i
    for j in range(2,num): # basically divide num by i 
        if num % j == 0:   # and check if anything was divisible without a remainder
            flag = False   # if there was a value then the flag is set to false 
            break          # exit the forloop right away if this happens
        flag = True        # always set true
    if flag == True:       # if the forloop is terminated early than this statement
        print(num)         # will not be invoked
        cnt += 1           # increment the prime counter
        flag = False       # reset back to false
    num += 1
