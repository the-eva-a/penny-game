# game_board_test.py
# This file lets me see if the GameBoard class is working properly. 

# Author: Eva Anderson
# Created: 10/18/24
# Last Modified: 10/18/24

import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game import Game
from player import Player

class TestGame(unittest.TestCase):

    def test_create_players(self):
        """Test that the game is initalized correctly and that player numbers are correct."""
        game = Game()
        game.numplayers = 4
        game.numcom = 2
        game.create_players()
        
        self.assertEqual(len(game.players), 4)
        self.assertTrue(all(isinstance(player, Player) for player in game.players.values()))
        self.assertEqual(sum(player.is_human for player in game.players.values()), 2)
        self.assertEqual(sum(not player.is_human for player in game.players.values()), 2)

    @patch("builtins.input", side_effect=["3"])
    def test_get_numplayers(self, mock_input):
        """Test that numplayers properly assigns the correct number of players."""
        game = Game()
        game.get_numplayers()
        self.assertEqual(game.numplayers, 3)

    @patch("builtins.input", side_effect=["2"])
    def test_get_numcom(self, mock_input):
        """Test that the number of COM players is properly assigned."""
        game = Game()
        game.numplayers = 3
        game.get_numcom()
        self.assertEqual(game.numcom, 2)

if __name__ == "__main__":
    unittest.main()
