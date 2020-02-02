import math

class SumSquareDifferenceFinder:

    @classmethod
    def sum_of_squares(self, numbers):
        current_sum = 0
        for each_number in numbers:
            current_sum += math.pow(each_number, 2)

        return current_sum

    @classmethod
    def square_of_sums(self, numbers):
        current_sum = 0
        for each_number in numbers:
            current_sum += each_number

        return math.pow(current_sum, 2)

    @classmethod
    def difference(self, numbers):
        return int(self.square_of_sums(numbers) - self.sum_of_squares(numbers))

print(SumSquareDifferenceFinder.difference(list(range(1, 101))))