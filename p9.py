'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 2^5 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
flag = False
for a in range(1,1000):
    if flag == True:
        break
    for b in range(1,1000):
        c = 1000-a-b
        tmp = a**2+b**2
        if c**2 == tmp:
            answer = a*b*c
            print(answer)
            flag = True



    




