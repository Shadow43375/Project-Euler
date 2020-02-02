class PrimeFinder:

    @classmethod
    def is_prime(self, prime_candidate):
        prime = True
        for n in range(2, prime_candidate):
            if(prime_candidate % n == 0):
                prime = False
                break
            
        return prime

    @classmethod
    def search(self, prime_index):
        prime_count = 0
        prime_candidate = 1
        while(prime_count < prime_index):
            prime_candidate += 1
            if(self.is_prime(prime_candidate)):
                prime_count += 1
        
        return prime_candidate

# print(PrimeFinder.search(2))
print(PrimeFinder.search(10001))
