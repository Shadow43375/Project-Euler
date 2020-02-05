import math

# function generates triangle numbers ad infinitum until a conditional breaks out of the function
# the Nth triangle number is equal to the sum of the first N natural numbers (1 + 2 + 3 + ... + N)
def triangle_number_generator():
    next_element = 1
    i = 1
    while True:
        yield next_element
        i += 1
        next_element += i

# function counts number of factors that are in an integer
def count_divisors(number):
    divisor_count = 0
    n = 1
    # the largest possible factors of a number are the square root of that number (eg 100 = 10*10).
    while n < math.sqrt(number):
        if(number % n == 0):
            divisor_count += 1
        n += 1

    return divisor_count*2 + 1

# find first triangular number that has more than 500 factors
for each_element in triangle_number_generator():
    if count_divisors(each_element) > 500:
        print(each_element)
        break