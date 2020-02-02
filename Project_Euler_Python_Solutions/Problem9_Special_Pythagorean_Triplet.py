import math

class SpecialPythagoreanTriplet:

    # method generates all triplets (a, b, c) such that a < b < c AND a + b + c = condition
    @classmethod
    def find_sum_condition_matches(self, condition):
        # create a list of triplets for storing those that satisfy the conditions
        triplet_list = []
        for a in range(1, condition + 1, 1):
            # starting place a + 1 ensures that b is always greater that a 
            for b in range(a + 1, condition + 1, 1):
                # starting place b + 1 ensures that c is always greater than both b and a
                for c in range(b + 1, condition + 1, 1):
                    # if the condition is met then append it to the list of triplets
                    if(a + b + c == condition):
                        triplet_list.append((a, b, c))

        return triplet_list

    # helper method for checking if the condition a^2 + b^2 = c^2 is satisfied    
    @classmethod
    def is_pythagorean_condition_matches(self, triplet):
        condition_match = False
        if(math.pow(triplet[0], 2) + math.pow(triplet[1], 2) == math.pow(triplet[2], 2)):
            condition_match = True
        
        return condition_match

    # main method for finding product of triplet that meets sum and pythagorean criteria
    @classmethod
    def triplets_product(self, condition):
        for each_triplet in self.find_sum_condition_matches(condition):
            if(self.is_pythagorean_condition_matches(each_triplet)):
                product = each_triplet[0]*each_triplet[1]*each_triplet[2]
                break

        return product

# example use
print(SpecialPythagoreanTriplet.triplets_product(1000))