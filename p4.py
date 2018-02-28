# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# may not be the fastest...but hey it worked!
lst = []
largest = 0
tmp = 0
strtmp = ''
for i in range(1,1000):     # test values from 1-999
    for j in range(1,1000):
        tmp = i * j
        strtmp = str(tmp)   # convert int to string
        for k in strtmp:    # traverse string and insert each character into the list
            lst.append(k)   

        if lst == lst[::-1] and i > 99 and j > 99: # check if the list = the inverse of itself
            if tmp > largest:                      # check if both multiplier and multiplicand are 3 digits
                largest = tmp                      # check for the greatest palindromic #
                var1 = i
                var2 = j
        lst = []                                   # clear the list 

print("\nLargest palindromic # of two 3-digit #'s:")       
print(str(var1)+" * "+str(var2)+" = "+str(largest))

