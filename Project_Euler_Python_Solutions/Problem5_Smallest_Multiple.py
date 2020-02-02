class SmallestMultipleFinder:

    # a helper method that checks if every number in the set 'numbers' divides evenly into 'number'
    @classmethod 
    def is_divisible_by_all(self, number, numbers):
        divisible_by_all = True
        for each_number in numbers:
            if not (number % each_number == 0):
                divisible_by_all = False
                break
            
        return divisible_by_all

    # the main method that searches interates through numbers to find one that is divisible by each of the elements in the set passed in 
    # as an argument
    @classmethod
    def search(self, numbers):
        candidate = 1
        while not (self.is_divisible_by_all(candidate, numbers)):
            candidate += 1

        return candidate    

#example use
print(SmallestMultipleFinder.search(range(1, 21)))
