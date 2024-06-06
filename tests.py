import unittest
from logics import get_number_from_index, is_zero_in_mas, get_index_from_number, get_empty_list, pretty_print

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_3(self):
        mas = [
            [0, 1, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)


