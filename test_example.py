import unittest


class TestExample(unittest.TestCase):
    
    def test_addition(self):
        """This test will pass"""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_failing_example(self):
        """This test will now pass"""
        result = 5 + 5
        self.assertEqual(result, 10, "Expected 10")
    
    def test_subtraction(self):
        """This test will pass"""
        result = 10 - 3
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
