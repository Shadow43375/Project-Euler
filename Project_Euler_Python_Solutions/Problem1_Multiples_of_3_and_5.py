# a class that sums all the integers between arbitary start and end points that are factors of numbers appearing in a set specified at construction
class Multiples:

# list of factors to check for can be of arbitary length. 
    def __init__(self, *args):
        self.factors = list(args)

    # main method
    def sum(self, start, end):
        sum = 0
        for i in range(start, end):
            if(self.is_factor(i)):
                sum += i
        return sum
    
    # helper method decides if a given number i is a factor of the numbers in the instance of sumMultiples
    def is_factor(self, i):
        result = False
        for factor in self.factors:
            if(i % factor == 0):
                result = True
                break
        return result

            
# example of usage
sum3and5 = Multiples(3,5)
sum = sum3and5.sum(1, 1000)
print(sum)