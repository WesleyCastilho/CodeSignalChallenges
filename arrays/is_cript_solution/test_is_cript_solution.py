import unittest

from arrays.is_cript_solution.is_crypt_solution import is_cript_solution


class TestIsCriptSolution(unittest.TestCase):
    def TestIsCriptSolution(self):
        crypt = ["SEND", "MORE", "MONEY"]
        solution = [['O', '0'],
                    ['M', '1'],
                    ['Y', '2'],
                    ['E', '5'],
                    ['N', '6'],
                    ['D', '7'],
                    ['R', '8'],
                    ['S', '9']]
        resolve = is_cript_solution(crypt, solution)
        print(resolve)
        self.assertTrue(resolve)