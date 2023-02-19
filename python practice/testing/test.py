import unittest
import script

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_par = 10
        result = script.do_stuff(test_par)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_par = "hsau"
        result = script.do_stuff(test_par)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_par = None
        result = script.do_stuff(test_par)
        self.assertEqual(result,'Please enter number')

    def test_do_stuff4(self):
        result = script.do_stuff()
        self.assertEqual(result,5)


if(__name__=='__main__'):
    unittest.main()