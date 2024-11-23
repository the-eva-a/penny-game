# game_board_test.py
# This file lets me see if the GameBoard class is working properly.

# Author: Eva Anderson

# Dependencies
import io
import os
import sys
import unittest
from contextlib import contextmanager
from unittest.mock import patch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


from player import Player



@contextmanager
def suppress_output():
    """Suppress console output to keep the test console clean."""
    original_stdout = sys.stdout
    try:
        sys.stdout = open(os.devnull, 'w')
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


class BasePlayerTest(unittest.TestCase):
    """
    Base test class for player-related tests.
    Provides a shared setup for creating human and computer players.
    """

    def setUp(self):
        """Shared setup code for initializing human and computer players."""
        Player.player_number = 0  # Reset static variable before each test
        self.human_player = Player(is_human=True)  # Initialize a human player
        self.com_player = Player(is_human=False)  # Initialize a computer player


class TestPlayerCreation(BasePlayerTest):
    """
    Test suite for verifying player creation.
    """

    def test_human_creation(self):
        """
        Test that human players are created with the correct attributes.
        """
        self.assertTrue(
            self.human_player.is_human,
            "Expected human player to be flagged with .is_human",
        )
        self.assertEqual(
            self.human_player.hand,
            20,
            "Expected human player to start with 20 pennies.",
        )
        self.assertEqual(
            self.human_player.player_number,
            1,
            "Expected the first player to be Player 1.",
        )

    def test_com_creation(self):
        """
        Test that computer players are created with the correct attributes.
        """
        self.assertFalse(
            self.com_player.is_human,
            "Expected computer player to not be flagged with .is_human",
        )
        self.assertEqual(
            self.com_player.hand,
            20,
            "Expected computer player to start with 20 pennies.",
        )
        self.assertEqual(
            self.com_player.player_number,
            2,
            "Expected the second player to be Player 2.",
        )


class TestDiceRoll(BasePlayerTest):
    """
    Test suite for verifying dice rolls.
    """

    def test_roll_range(self):
        """
        Test that dice rolls are within the valid range of 1-6.
        """
        rolls = [self.human_player.roll_dice() for _ in range(1000)]
        for roll in rolls:
            self.assertIn(roll, range(1, 7), "Expected dice rolls to be in range 1-6.")
        for number in range(1, 7):
            self.assertIn(number, rolls, f"Expected {number} to appear in dice rolls.")


class TestPlayerRoll(BasePlayerTest):
    """
    Test suite for verifying player rolling behavior.
    """

    @patch("builtins.input", return_value="")
    def test_human_roll(self, mock_input):
        """
        Test that human players can roll the dice and get a valid roll.
        """
        with suppress_output():
            roll = self.human_player.player_roll()
        self.assertIn(roll, range(1, 7), "Expected roll to be between 1 and 6.")

    def test_com_roll(self):
        """
        Test that computer players roll the dice without input and get a valid roll.
        """
        with suppress_output():
            roll = self.com_player.player_roll()
        self.assertIn(roll, range(1, 7), "Expected roll to be between 1 and 6.")


class TestPlayerRollAnnouncement(BasePlayerTest):
    """
    Test suite for verifying roll announcements.
    """

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_announce_roll_output(self, mock_stdout):
        """
        Test that announce_roll outputs the correct message.
        """
        sample_roll = 5
        self.human_player.announce_roll(sample_roll)
        output = mock_stdout.getvalue().strip()
        expected_output = f"Player {self.human_player.player_number} rolled a {sample_roll}!"
        self.assertEqual(output, expected_output, "Roll announcement did not match expected output.")


class TestAddPennies(BasePlayerTest):
    """
    Test suite for verifying the add_pennies method.
    """

    def test_valid_add_pennies(self):
        """
        Test that adding valid numbers of pennies updates the player's hand correctly.
        """
        self.human_player.add_pennies(6)
        self.assertEqual(self.human_player.hand, 26, "Expected hand to increase by 6 pennies.")

        self.com_player.add_pennies(1)
        self.assertEqual(self.com_player.hand, 21, "Expected hand to increase by 1 penny.")

    def test_negative_add_pennies(self):
        """
        Test that adding negative pennies raises a ValueError.
        """
        with self.assertRaises(ValueError, msg="Negative input should raise ValueError."):
            self.human_player.add_pennies(-5)

    def test_non_integer_add_pennies(self):
        """
        Test that non-integer inputs raise a ValueError.
        """
        invalid_inputs = ["four", [1, 2], {"key": "value"}]
        for value in invalid_inputs:
            with self.assertRaises(ValueError, msg=f"Input {value} should raise ValueError."):
                self.human_player.add_pennies(value)


class TestDropPennies(BasePlayerTest):
    """
    Test suite for verifying the drop_penny method.
    """

    def test_drop_penny(self):
        """
        Test that dropping a penny reduces the player's hand by one.
        """
        self.human_player.drop_penny()
        self.assertEqual(self.human_player.hand, 19, "Expected hand to decrease by 1 penny.")

        self.com_player.drop_penny()
        self.assertEqual(self.com_player.hand, 19, "Expected hand to decrease by 1 penny.")


class TestCheckReroll(BasePlayerTest):
    """
    Test suite for verifying the check_reroll method.
    """

    @patch("builtins.input", side_effect=["n"])
    def test_human_reroll_not_winner(self, mock_input):
        """
        Test that a human player with pennies does not win after rerolling.
        """
        self.human_player.check_reroll()
        self.assertFalse(self.human_player.is_winner, "Expected player not to be a winner with pennies left.")

    def test_com_reroll_not_winner(self):
        """
        Test that a computer player with pennies does not win after rerolling.
        """
        self.com_player.check_reroll()
        self.assertFalse(self.com_player.is_winner, "Expected COM player not to be a winner with pennies left.")

    def test_human_reroll_winner(self):
        """
        Test that a human player with no pennies is marked as a winner.
        """
        self.human_player.hand = 0
        self.human_player.check_reroll()
        self.assertTrue(self.human_player.is_winner, "Expected player to be a winner with no pennies.")

    def test_com_reroll_winner(self):
        """
        Test that a computer player with no pennies is marked as a winner.
        """
        self.com_player.hand = 0
        self.com_player.check_reroll()
        self.assertTrue(self.com_player.is_winner, "Expected COM player to be a winner with no pennies.")


if __name__ == "__main__":
    unittest.main()
