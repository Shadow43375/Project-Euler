import math

class PalindromeFinder:

    # a helper method for finding if an integer is a palindrome
    @classmethod
    def is_palindrome(self, number):
        #convert number to string format to allow for indexing
        number = str(number)
        # assume that it is a palindrome and attempt to prove this false
        palindrome_status = True
        # check individual digits to see if they read the same forward and backwards (definition of palindrome)
        for digit in range(len(number)):
            if not (number[digit] == number[len(number) - 1 - digit]):
                palindrome_status = False

        return palindrome_status

    # main method for finding the largest palindrome that is the product of two integers of an arbitrary number of digits
    @classmethod
    def search_product_of(self, digits):
        start = int(math.pow(10, digits - 1))
        end = int(start*10)
        palindrome_list = []

        # this esentially generates half a multiplication table (the other half is identical)
        for first_multiplicant in range(start, end):
            for second_multiplicant in range(first_multiplicant, end):
                product = first_multiplicant*second_multiplicant
                if(self.is_palindrome(product)):
                    palindrome_list.append(product)

        return max(palindrome_list)
    
# example use
print(PalindromeFinder.search_product_of(3))