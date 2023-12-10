"""
 test quality: FIRST
 F -> fast its often used
 I -> independant every test must be alone
 R -> repeatable I can repeat every time I need
 S -> self validating must be AUTOMATIC
 T -> timely right place right time
"""
import unittest


def power_num(number: float, power: int) -> float:
    """
    Raise the number to the power if number >= 0.
        number (float): the number I find power
        power (int): the power apply to a number

    Returns: the power of number in float type
    """

    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("The number can only be int or float")

    if not isinstance(power, int):
        raise TypeError("The power can only be of int type")

    if number >= 0:
        return round(number ** power, 2)
    raise TypeError("The number can only be >= 0")


class TestPower(unittest.TestCase):
    def test_power_int(self):
        self.assertEqual(power_num(2, 3), 8)

    def test_power_float(self):
        self.assertEqual(power_num(1.5, 2), 2.25)

    def test_for_negative_numbers(self):
        with self.assertRaises(TypeError):
            power_num(-6, 2)

    def test_for_zero_as_number_and_positive_power(self):
        self.assertEqual(power_num(0, 2), 0)

    def test_for_zero_as_number_and_negative_power(self):
        with self.assertRaises(TypeError):
            power_num(0, -2)

    def test_for_zero_as_number_and_negative_power2(self):
        with self.assertRaises(ZeroDivisionError):
            power_num(0, -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
