# returns the sum of each of the individual digits in a number
def sum_digits(number, start, end):
    return sum([int(each_digit) for each_digit in list(str(number))[start:end]])

# example usage
print(sum_digits(2**15, 1, 4))
