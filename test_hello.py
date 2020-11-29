import unittest
from hello_world import Addition


class TestAddition(unittest.TestCase):

    def setup(self):
        self.a = 20
        self.b = 30

    def test_addition(self):
        obj = Addition(20, 30)
        res = obj.addition()
        self.assertEqual(res, 50)

if __name__ == '__main__':
    unittest.main()