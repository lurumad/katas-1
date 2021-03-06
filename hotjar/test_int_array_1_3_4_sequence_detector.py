# -*- coding: utf-8 -*-
import unittest

# Exercise: Given an array of ints, return True if the sequence.. 1, 3, 4 .. appears in the array somewhere
# Applied YAGNI and KISS: it is a pure function (no OO), only working for [1, 3, 4]. It could be further generalized or applying recursion IFF NEEDED.
# Other things could be optimised if the sequence to search for were generalized.
# Time complexity:  O(n)
# Space complexity: O(1)
def contains_sequence_1_3_4(numbers):
    searched_sequence = [1, 3, 4]
    searched_sequence_length = len(searched_sequence)
    input_length = len(numbers)
    if input_length < searched_sequence_length:
        return False
    for index in range(input_length - searched_sequence_length + 1):
        if (numbers[index] == searched_sequence[0] and 
            numbers[index + 1] == searched_sequence[1] and 
            numbers[index + 2] == searched_sequence[2]):
            return True
    return False


# To run the tests, from the command line type:  python -test_int_array_sequence_detector.py -v
class Test134SequenceDetector(unittest.TestCase):
    
    def test_a_long_array_containing_the_sequence_should_resturn_True(self):
        self.assertTrue(contains_sequence_1_3_4([1, 3, 45, 8, 1, 3, 4, 9]))

    def test_an_array_containing_exactly_the_sequence_should_resturn_True(self):
        self.assertTrue(contains_sequence_1_3_4([1, 3, 4]))

    def test_a_long_array_not_containing_the_sequence_should_resturn_False(self):
        self.assertFalse(contains_sequence_1_3_4([1, 3, 45, 8, 1, 4, 9]))

    def test_too_short_sequence_should_return_False(self):
        self.assertFalse(contains_sequence_1_3_4([1, 4]))

    def test_an_array_containing_the_sequence_numbers_non_consecutively_should_return_False(self):
        self.assertFalse(contains_sequence_1_3_4([1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()