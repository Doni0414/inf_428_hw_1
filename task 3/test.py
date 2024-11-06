import unittest

from cyclic_transformation import time_difference_simple, time_difference_trigonometry
from parameterized import parameterized

funcs_to_test = [time_difference_simple]

class CyclicTransformationTest(unittest.TestCase):
    
    @parameterized.expand(funcs_to_test)
    def test_13minus10(self,func):
        # given
        hour1 = 10
        hour2 = 13

        # when
        actual = func(hour1, hour2)
        # print(func)
        # then
        expected = 3
        self.assertEqual(expected, actual)

    @parameterized.expand(funcs_to_test)
    def test_10minus13(self,func):
        # given
        hour1 = 13
        hour2 = 10

        # when
        actual = func(hour1, hour2)

        # then
        expected = 21
        self.assertEqual(expected, actual)

    @parameterized.expand(funcs_to_test)
    def test_23minus1(self,func):
        # given
        hour1 = 1
        hour2 = 23

        # when
        actual = func(hour1, hour2)

        # then
        expected = 22
        self.assertEqual(expected, actual)
    
    @parameterized.expand(funcs_to_test)
    def test_1minus23(self,func):
        # given
        hour1 = 23
        hour2 = 1

        # when
        actual = func(hour1,hour2)

        # then
        self.assertEqual(2, actual)
    
    @parameterized.expand(funcs_to_test)
    def test_12minus0(self,func):
        # given
        hour1 = 0
        hour2 = 12

        # when
        actual = func(hour1, hour2)

        # then
        self.assertEqual(12, actual)

    @parameterized.expand(funcs_to_test)
    def test_0minus12(self,func):
        # given
        hour1 = 0
        hour2 = 12

        # when
        actual = func(hour1, hour2)

        # then
        self.assertEqual(12, actual)
    
    @parameterized.expand(funcs_to_test)
    def test_12minus12(self, func):
        # given
        hour1 = 12
        hour2 = 12

        # when
        actual = func(hour1, hour2)

        # then
        self.assertEqual(0, actual)
    
    @parameterized.expand(funcs_to_test)
    def test_all_cases(self,func):
        for hour1 in range(24):
            for hour2 in range(24):
                actual = func(hour1, hour2)

                expected = (hour2 - hour1) % 24

                self.assertEqual(expected, actual)