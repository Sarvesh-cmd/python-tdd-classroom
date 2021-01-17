import unittest
from src.exercises import reverse_list, count_digits


class TestExercise(unittest.TestCase):

    def setUp(self):
        
        def reverse_list(ls):
            new_lst = ls[::-1]
            return new_lst

    def test_reverse_list(self):
        expected = [5, 4, 3, 2, 1]
        actual = [1,2,3,4,5]
        actual.reverse()
        self.assertEqual(expected,actual)

        expected = [6, 5, 4, 3, 2, 1]
        actuall = [1, 2, 3, 4, 5, 6]
        actuall.reverse()
        self.assertEqual(expected, actuall) 

    def test_count_digits(self):
        number = 123
        expected = 3
        actual=0
        while(number>0):
            number=number//10
            actual = actual + 1

        self.assertEqual(expected, actual)

    def tearDown(self):
        pass   # If needed, do final unstubbing/unmocking here, like calling unittest.unstub()
