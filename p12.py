'''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
triangle_divisors = []
running_sum = 0
i = 0
flag = True
my_dict={}
while flag == True:
    i += 1
    running_sum += i
    triangle_divisors.append(running_sum)
    x = math.ceil((running_sum+1)/2)
    for j in range(1,x):
        if running_sum%j == 0:
            x = int(running_sum/2)
            triangle_divisors.append(j)
            my_dict[str(j)] = j
            j = 2    
            if len(triangle_divisors) == 6:
                print(triangle_divisors)
                print(running_sum)
                flag = False
    triangle_divisors = []

print(my_dict)
    