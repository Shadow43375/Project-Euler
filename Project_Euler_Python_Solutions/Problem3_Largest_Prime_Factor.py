import math

class LargestPrimeFinder:

    @classmethod
    def is_prime(self, prime_candidate):
        if prime_candidate == 2 or prime_candidate == 3 :
            return True

        if prime_candidate % 2 == 0 or prime_candidate % 3 == 0 :
            return False

        for n in range(4, int(math.sqrt(prime_candidate)) + 1):
            if prime_candidate % n  == 0:
                return False

        return True

       
    @classmethod
    def find_greatest_prime_factor(self, integer):
        for possible_factor in range(math.ceil(integer/2), 1, -1):
            print(possible_factor)
            if integer % possible_factor == 0:
                if self.is_prime(possible_factor):
                    return possible_factor

        return False

print(LargestPrimeFinder.find_greatest_prime_factor(600851475143))