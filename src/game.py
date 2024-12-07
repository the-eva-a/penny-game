# game.py
# This file contains the Game class, which is responsible for the logic
# concerning general gameplay functions.

# Author: Eva Anderson
# Created:11/10/24
# Last Modified: 12/08/24

# Dependencies:
#   - Player class
#   - GameBoard class

# Usage Example:
# game1 = Game()
# game1.who_first()

from player import Player
from game_board import GameBoard


class Game:
    """
    The Game class manages the gameplay logic and controls the flow of the game.

    Attributes
    ----------
    numplayers: int
        An integer representing the total number of players
    numcom: int
        An integer representing the total number of computer (COM) players.
    players: dict
        A dictionary that stores all of the player objects.
    game_winner: bool
        A flag that indicates whether a player has won the game

    Methods
    -------
    create_players():
        Creates the players dictionary containing all participating human and COM players.
    get_numplayers():
        Prompts the user to enter the number of players.
    get_numcom():
        Prompts the user to enter the number of COM players.
    who_first():
        Determines which player goes first by rolling dice for each player.
        If there is a tie, players with the highest roll will reroll until there is a single winner.
    final_scores():
        Displays the scores of all players.
    """

    def __init__(self):
        """
        Initializes the Game class

        Attributes
        ----------
        numplayers: int
            An integer representing the total number of players
        numcom: int
            An integer representing the total number of computer (COM) players.
        players: dict
            A dictionary that stores all of the player objects.
        game_winner: bool
            A flag that indicates whether a player has won the game
        """
        self.numplayers = 0
        self.numcom = 0
        self.players = {}
        self.game_winner = False

    def create_players(self):
        """
        Creates the players dictionary containing all participating human and COM players.
        """
        # Create players (human and COM)
        for i in range(self.numplayers):
            is_human = i < (self.numplayers - self.numcom)
            self.players[i + 1] = Player(is_human=is_human)

    def get_numplayers(self):
        """
        Prompts the user to input the number of players and sets numplayers to that input.
        """
        while True:
            try:
                numplayers = int(input("Enter the number of players (2-5): "))
                if 2 <= numplayers <= 5:
                    self.numplayers = numplayers
                    break
                else:
                    print("Please enter a number between 2 and 5.")
            except ValueError:
                print("Invalid input. Please enter an integer between 2 and 5.")

    def get_numcom(self):
        """
        Prompts the user to enter the number of COM players and sets numcom to that value.
        """
        while True:
            try:
                num_com = int(
                    input(
                        f"How many COM players would you like? (0-{self.numplayers}): "
                    )
                )
                if 0 <= num_com <= self.numplayers:
                    self.numcom = num_com
                    break
                else:
                    print(f"Please enter a number between 0 and {self.numplayers}.")
            except ValueError:
                print(
                    f"Invalid input. Please enter an integer between 0 and {self.numplayers}."
                )

    def who_first(self):
        """
        Determines which player goes first by rolling dice for each player.
        If there is a tie, players with the highest roll will reroll until there is a single winner.

        Returns:
        --------
        int: The player number who goes first.
        """
        rolls_dict = {key: 0 for key in range(1, self.numplayers + 1)}

        # Initial roll for all players
        for player in rolls_dict.keys():
            rolls_dict[player] = self.players[player].player_roll()

        max_value = max(rolls_dict.values())
        players_with_max_roll = [
            key for key, value in rolls_dict.items() if value == max_value
        ]

        # Handle ties by rerolling
        while len(players_with_max_roll) > 1:
            print(f"Tie detected! Players {players_with_max_roll} will reroll.")
            rolls_dict = {key: 0 for key in players_with_max_roll}
            for player in rolls_dict.keys():
                rolls_dict[player] = self.players[player].player_roll()
            max_value = max(rolls_dict.values())
            players_with_max_roll = [
                key for key, value in rolls_dict.items() if value == max_value
            ]

        winner = players_with_max_roll[0]
        print(f"Player {winner} goes first!")
        return winner

    def final_scores(self):
        """
        Prints the final score of each player.
        """
        sorting_dict = {}
        for player in self.players.values():
            sorting_dict[player.player_number] = player.hand
        sorted_dict = {
            key: value
            for key, value in sorted(sorting_dict.items(), key=lambda item: item[1])
        }

        print("Final Scores")
        print("------------")

        for player_no, hand in sorted_dict.items():
            print(f"   {player_no} : {hand}")
