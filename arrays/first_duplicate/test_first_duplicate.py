import unittest

from arrays.first_duplicate.first_duplicate import FirstDuplicate


class TestFirstDuplicate(unittest.TestCase):
    def test_if_array_has_duplicate_number(self):
        array = [2, 1, 3, 5, 3, 2]
        isduplicated = FirstDuplicate.first_duplicate(array)
        self.assertIsNot(isduplicated, -1)

    def test_if_array_has_duplicate_number_without_duplicate_number(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        isduplicated = FirstDuplicate.first_duplicate(array)
        self.assertIs(isduplicated,-1)


if __name__ == '_main_':
    unittest.main
