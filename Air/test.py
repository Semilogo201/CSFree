import unittest
from no1 import addition
#testing addition function
class testing_add(unittest.TestCase):
    def test_add(self):
        self.assertEqual (4, 3)

if __name__ == '__main__':
    unittest.main()
 