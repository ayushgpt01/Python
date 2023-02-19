import unittest
import terminal_game

class TestMain(unittest.TestCase):
    def test_game(self):
        test_par1 = 1
        test_par2 = 1
        result = terminal_game.run_guess(test_par1,test_par2)
        self.assertFalse(result)

    def test_game1(self):
        test_par1 = 1
        test_par2 = 4
        result = terminal_game.run_guess(test_par1,test_par2)
        self.assertTrue(result)

    def test_game2(self):
        test_par1 = "a"
        test_par2 = 4
        result = terminal_game.run_guess(test_par1,test_par2)
        self.assertTrue(result)


if(__name__=='__main__'):
    unittest.main()