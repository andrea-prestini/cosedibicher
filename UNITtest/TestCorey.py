import unittest


def calcolatore(a: int, b: int):
    return a + b


class Test_calcolatore(unittest.TestCase):
    def setUp(self):
        print("SETUP called...")

        # Arrange
        self.a = 1000
        self.b = 20

    def tearDown(self):
        print("TEARDOWN called...")

    def test_calcolatore(self):
        print("TEST 1 called...")

        # ACT
        result = self.a + self.b

        # Assert
        self.assertLessEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
