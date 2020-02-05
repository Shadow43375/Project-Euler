import math

class Summation_of_primes:

    @classmethod
    def is_prime(self, prime_candidate):
        # edge cases
        if(prime_candidate == 2 or prime_candidate == 3):
            return True

        # many composite numbers are divisible by either 2 or 3. By checking these cases we can weed out a lot of redundant computation
        if(prime_candidate % 2 == 0 or prime_candidate % 3 == 0):
            return False

        # in the worst case, we perform a division test on all numbers up to the square root of the prime candidate.    
        for n in range(2, int(math.sqrt(prime_candidate)) + 1):
            if(prime_candidate % n == 0):
                return False
        
        return True

    # the main function that test submists numbers to test for primality and appends them to a list before returning their sum.
    @classmethod
    def sum_up_to(self, end):
        prime_list = []
        for prime_candidate in range(2, end):
            if(self.is_prime(prime_candidate)):
                prime_list.append(prime_candidate)
        return sum(prime_list)

# example usage
print(Summation_of_primes.sum_up_to(2000000))