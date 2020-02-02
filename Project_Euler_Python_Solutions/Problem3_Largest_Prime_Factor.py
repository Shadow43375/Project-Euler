import math
import time


class LargestPrimeFinder:

    def __init__(self):
        self.prime_list = []
        self.composite_list = []

    # helper method for adding primes to list
    def add_prime(self, prime):
        if not prime in self.prime_list:
            self.prime_list.append(prime)

    # helper method for adding composites to the list
    def add_composite(self, composite):
        if not composite in self.composite_list:
            self.composite_list.append(composite)
        
    # primary method for searching for largest prime
    def search(self, number):
        largest_prime = False
        highest_possible_candidate = math.ceil(number/2)
        # any integer that isn't at least half the size of the number won't be a factor. So we can reduce search field by half
        for prime_candidate in range(highest_possible_candidate, 1, -1):
            if(self.is_factor(prime_candidate, number)):
                if self.is_prime(prime_candidate):
                    largest_prime = prime_candidate
                    self.add_prime(largest_prime)
                    break
                else:
                    self.add_composite(prime_candidate)
                    
        return largest_prime

    # helper function to figure out if a number is prime
    def is_prime(self, prime_candidate):
        is_prime_number = True
        # check to see if prime number is already in list of primes
        if(prime_candidate in self.prime_list):
            pass
        elif(prime_candidate in self.composite_list):
            is_prime_number = False
            pass
        else:
            for n in range(2, math.ceil(prime_candidate/2) + 1):
                # if divisor is found greater than 1 then we know it is NOT prime and can stop checking.
                if(prime_candidate % n == 0):
                    is_prime_number = False
                    break
        return is_prime_number    

    # helper function for determining if a number is factor
    def is_factor(self, prime_candidate, number):
        if(number % prime_candidate == 0):
            factor_of = True
        else:
            factor_of = False

        return factor_of


start_time = time.time()
prime_finder = LargestPrimeFinder()
print(prime_finder.search(13195))


