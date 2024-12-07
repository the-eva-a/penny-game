# game_board_test.py
# This file lets me see if the GameBoard class is working properly. 

# Author: Eva Anderson
# Created: 10/10/24
# Last Modified: 12/18/24

# dependencies
import io
import os
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch
#from unittest.mock import patch


# set path so we can import GameBoard class
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


from game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    
    def setUp(self):
        """
        Create a new GameBoard instance before each test.
        """
        self.board = GameBoard()
    
    def test_initial_state(self):
        """
        Test that the board is initialized correctly with all slots empty and no crash.
        """
        expected_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.assertEqual(
            self.board.state, expected_state,
            f"Expected f{expected_state} instead of f{self.board.state}"
            )
        self.assertFalse(
            self.board.crash,
            "Expected a newly made game board to not be in a crash state.")

    def test_add_penny(self):
        """
        Test that a penny can be added to a slot and that the crash flag is not set.
        """
        self.board.add_penny(2)
        self.assertEqual(
            self.board.state[2], 1,
            f"Expected 1 penny in slot 2 not f{self.board.state[2]}")
        self.assertFalse(
            self.board.crash,
            "Expected board to not crash."
            )

    def test_add_penny_crash(self):
        """
        Test that adding more than one penny to the same slot (1-5) causes a crash.
        """
        self.board.add_penny(3)
        self.board.add_penny(3)
        self.assertTrue(
            self.board.crash,
            "Expected board to be in a crash state.")
        self.assertEqual(
            self.board.state[3], 2,
            )
        self.board.add_penny(2)
        self.assertTrue(
            self.board.crash,
            "Expected board in crash state to remain crashed if an additional penny was added."
            )
        

   
    def test_slot_six_drop(self):
        """
        Test that the sixth slot will not cause a collision and will be removed from 
        the board with the addition of the next penny.
        """
        self.board.add_penny(6)
        self.board.add_penny(6)
        self.board.add_penny(1)
        self.assertEqual(
            self.board.state[6], 0,
            f"Expected slot 6 to be empty not f{self.board.state[6]}")
        self.assertFalse(
            self.board.crash,
            "Expected crash to be False, slot 6 should never trigger a crash."
            )

    def test_add_penny_invalid_slot(self):
        """
        Test that adding a penny to an invalid slot raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.board.add_penny(7)
            self.board.add_penny(-1)
            self.board.add_penny('hello')
            self.board.add_penny([1, 'adff', 4.5])
    

class testClearBoard(TestGameBoard):
    def test_clears_crash(self):
        self.board.crash = True
        self.board.clear_board()
        self.assertFalse(
            self.board.crash,
            "Expected cleared board to not be in a crash state."
        )
    def test_cleared_board_states(self):
        for i in range(1,7):
            for j in range(0,3):
                self.board.add_penny(i)
        
        self.board.clear_board()
        
        non_zero_keys = []
       # check for nonzero keys
        for key, value in self.board.state.items():
            if value != 0: 
                non_zero_keys = key
        self.assertTrue(
        all(value == 0 for value in self.board.state.values()),
        f"Non-zero values found for keys: {non_zero_keys}"
    )

    def test_penny_return(self):
        self.board.state = {1: 6, 2: 4, 3: 3, 4: 2, 5: 1, 6: 0}
        penny_return = self.board.clear_board()
        self.assertEqual(
            penny_return, 16,
            f"Expected 16 pennies to be returned instead of f{penny_return}"
        )





if __name__ == '__main__':
    unittest.main()