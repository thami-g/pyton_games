import unittest
from bagels import *


def find_all_occurrences(string, char):
    """find all occurances of a character or strng"""
    total_count = 0
    index = -1
    while True:
        index = string.find(char, index + 1)
        if index == -1:
            break
        total_count += 1
    return total_count


class TestBagels(unittest.TestCase):

    def test_getSecretNum_len(self):
        output = getSecretNum()
        self.assertEqual(len(output), 3)

    def test_no_duplicate_values(self):
        secret_num = getSecretNum()
        for num in secret_num:
            self.assertEqual(find_all_occurrences(secret_num, num), 1)

    def test_get_clues_bagels(self):
        output = getClues("456", "123")
        self.assertEqual(output, "Bagels")

    def test_get_clues_fermi(self):
        output = getClues("146", "123")
        self.assertEqual(output, "Fermi")

    def test_get_clues_pico(self):
        output = getClues("246", "123")
        self.assertEqual(output, "Pico")


if __name__ == "__main__":
    unittest.main()
