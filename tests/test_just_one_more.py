import unittest
from just_one_more import increment


class TestJust_One_More(unittest.TestCase):
    def test_level_1(self):
        """
        Get a list with only int.
        Increment all int in list by 1.
         :return: List with ints incremented by 1
        """
        initial_list = [1, 0, -1, 5, 100, 37, 20, 18, 12, 0]
        expected_result = [2, 1, 0, 6, 101, 38, 21, 19, 13, 1]
        self.assertEqual(increment(initial_list), expected_result)

    def test_level_2(self):
        """
        Get a list with strings, discard all strings that
        doesn't represent a number. Increment numbers by 1.
        :return: List with ints.
        """
        initial_list = ['1', 'c', '0', '-1', '5', 'b', '100', '37', 'a', '20', '18', '12', '0']
        expected_result = [2, 1, 0, 6, 101, 38, 21, 19, 13, 1]
        self.assertEqual(increment(initial_list), expected_result)

    def test_level_3(self):
        """
        Get a list with strings that have values containing both
        numeric and non-numeric parts. Increment the number in the
        string, keeping the original 'word'
        :return: List with strings, increment numbers by 1.
        """
        initial_list = ['ab123', 'gh00', 'ijk8', 'lmn12', 'cd99ef11']
        expected_result = ['ab124', 'gh01', 'ijk9', 'lmn13', 'cd100ef12']
        self.assertEqual(increment(initial_list), expected_result)

