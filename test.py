import unittest

from addition import addition

class TestAddition(unittest.TestCase):
    
     def test_case1(self):
        print("Running test case 1: adding -1 and 5")
        with self.assertRaises(ValueError):
            addition(-1, 5)
        print("Test case 1 passed \n")
        
     def test_case2(self):
        print("Running test case 2: adding 3 and 5")
        result = addition(3, 5)
        self.assertEqual(result, 8)
        print("Test case 2 passed \n")
        
        
        
        
if __name__ == '__main__':
    unittest.main()