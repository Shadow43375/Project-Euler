# generator function that yields the next element in a Collatz sequence given some starting seed
# the next element in a collatz sequence is n/2 if the current element n is even and 3n + 1 if odd
def collatz_generator_function(seed):
    next_element = seed
    while True:
        yield int(next_element)
        if next_element % 2 == 0:
            next_element /= 2
        else:
            next_element = next_element*3 + 1

# a function that returns the elements of a collatz sequence as a list given some initial seed
def get_collatz_sequence(seed):
        collatz_sequence = []
        for n in collatz_generator_function(seed):
            collatz_sequence.append(n)
            if n == 1:
                break
        
        return collatz_sequence

# function that finds the collatz sequence with the most number of elments from 1 to some natural number 'end' 
def find_longest_collatz(end):
    largest_yet = {"seed": 1, "period": 1}
    for seed in range(1, end):
        if seed % 1000 == 0:
            print(seed)
        next_squence = get_collatz_sequence(seed)
        if len(next_squence) > largest_yet["period"]:
            largest_yet["seed"] = seed
            largest_yet["period"] = len(next_squence)
    
    return largest_yet["seed"]
    
# example usage
print(find_longest_collatz(1000000))