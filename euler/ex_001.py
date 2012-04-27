# Problem 1

# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

answer = 0 # create container for answer

# loop num from 0-999
for num in range(1000): 

    # if num is multiple of 3 or 5 or both, add num to answer
    if (num % 3 == 0 or num % 5 == 0): 
        answer += num 
        
print answer
# 233168