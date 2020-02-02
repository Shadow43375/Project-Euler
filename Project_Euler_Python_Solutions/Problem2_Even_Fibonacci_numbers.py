class FibonacciSequence:

    def __init__(self, end = 1):
        self.create(end)

    # this function creates the sequence from 1 to end.
    def create(self, end):
        self.elements = [1]
        for i in range(end):
            self.elements.append(self.next_element(i))
        # the index of the last element in the sequence. used to set bounds of iteration in __next__ method
        self.max = len(self.elements) - 1

    # helper function for getting the next element in the FibonacciSequence
    def next_element(self, i):
        # special case-- first element is 1 and there is no previous element to add. This absence of element is interpreted as a zero and thus we have 0 + 1 = 1
        if(i == 0):
            new_element = 1
        # the normal rule for generating an the next element of the Fibonacci sequence. To find next element take current element and add the element that came before it.
        else:
            new_element = self.elements[i] + self.elements[i - 1]
        return new_element

    # this function defines what to print when an instance of the FibonacciSequence class is passed to the standard python3 print() function.
    def __str__(self):
        return str(self.elements)

    # this function makes class instances indexable in the manner of lists. Does not implement setting of values as this could distort Fibonacci sequence
    def __getitem__(self, i):
        return self.elements[i]

# creates and iterable variable to make class instances interable
    def __iter__(self):
        self.n = 0
        return self

 #  Return next element in sequence  if there is one. If no raise exception to automatically terminate the iteration.   
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.elements[self.n]
        else:
            raise StopIteration

# example use-- find sum of all even members of fibonacci sequence below the value of 4,000,000
series = FibonacciSequence(5)
result = 0
size_limit = 4000000
for element in series:
    if(element % 2 == 0 and element < size_limit):
        result += element
print(series)
print(result)