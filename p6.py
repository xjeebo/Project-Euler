# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

SumSquare = 0
SquareSum = 0
for i in range(1,101):
    SumSquare += i**2 # running sum of i squared
    SquareSum += i    # running sum of i, which will later be squared when the total is found

print("Answer: "+str(SquareSum**2-SumSquare))
