# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

n = 600851475143 # given value
i = 2
while i < n:    

    if n % i == 0:  # check if the given value is divisible by i, which is incremented every time by 1
        n = n/i     # if it is divisible, divide num by that val and reset the num
        i = 2       # reset i
    i += 1          # when I becomes = to n then the value had only been divisible by 1 and itself, which means it is prime
print(n) # the largest prime number
