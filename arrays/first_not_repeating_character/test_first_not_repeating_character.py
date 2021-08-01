import unittest


class TestFirstNotRepeatingCharacter(unittest.TestCase):
    def find_first_not_repeating_character(self):
        string = "O Rato Roeu A Roupa Do Rei De Roma"
        isrepeating: object = FirstNotRepeating.first_not_repeating_character(string)
        self.assertIsNot(isrepeating, '-')

    def find_first_not_repeating_without_repeating_string(self):
        string = "a,b,c,d,e,f,g,h"
        isrepeating = FirstNotRepeating.first_not_repeating_character(string)
        self.assertIs(isrepeating, '-')
