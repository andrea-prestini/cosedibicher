import unittest


def sum(a, b):
    return a + b


class TestSum(unittest.TestCase):

    def setUp(self):
        print("SETUP called...")

        # Arrange isolation and instancing
        self.a = 10
        self.b = 20

    def tearDown(self):
        print("TEARDOWN called...")

    def test_sum1(self):
        print("TEST 1 called...")

        # ACT input data
        result = sum(self.a, self.b)

        # Assert assertion my function test return
        self.assertEqual(result, self.a + self.b)

    def test_sum2(self):
        print("TEST 2 called...")

        result = sum(self.a, self.b)

        self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
    unittest.main()
