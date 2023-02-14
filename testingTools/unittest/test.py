import unittest
import caps

class TestCap(unittest.TestCase):

    def test_case_one(self):
        text = 'python'
        result = caps.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_case_two(self):
        text = 'python testing'
        result = caps.cap_text(text)
        self.assertEqual(result, 'Python Testing')

if __name__ == "__main__":
    unittest.main()