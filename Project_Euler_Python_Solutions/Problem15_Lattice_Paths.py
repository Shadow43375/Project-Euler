def factorial(argument):
    result = 1
    for x in range(argument, 0, -1):
        result *= x

    return result

def get_possible_paths(x, y):
    return int(factorial(x + y)/(factorial(x)*factorial(y)))

print(get_possible_paths(20, 20))