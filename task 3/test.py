import unittest

from cyclic_transformation import time_difference_simple, time_difference_trigonometry
from parameterized import parameterized

class CyclicTransformationTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.funcs_to_test = [time_difference_simple, time_difference_trigonometry]
    
    # @parameterized.expand([
    #     time_difference_simple,
    #     time_difference_trigonometry
    # ])
    def test_13minus10(self):
        # given
        hour1 = 10
        hour2 = 13

        # when
        actual = time_difference_trigonometry(hour1, hour2)
        # print(func)
        # then
        expected = 3
        self.assertEqual(expected, actual)

    # @parameterized.expand([
    #     time_difference_simple,
    #     time_difference_trigonometry
    # ])
    def test_10minus13(self):
        # given
        hour1 = 13
        hour2 = 10

        # when
        actual = time_difference_trigonometry(hour1, hour2)

        # then
        expected = 21
        self.assertEqual(expected, actual)