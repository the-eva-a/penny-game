import random


class Player:
    """
    The Player class manages the virtual players. 
    It tracks each player's hand, determines if they are a human player, and 
    manages dice rolling and reroll choices.

    Attributes:
    -----------
    player_number: int
        Tracks the player number in sequence.
    hand: int
        The number of pennies each player has in their hand.
    is_human: bool
        Whether the player is human or a computer.
    is_winner: bool
        Indicates if the player has won the game.
    
    Methods:
    --------
    roll_dice(): 
        Rolls a virtual die and returns an integer in [1, 6].
    announce_roll(roll: int):
        Announces the player's roll value.
    player_roll():
        Handles the dice roll process based on the player's type (human or computer).
    add_pennies(number: int):
        Adds a specified number of pennies to the player's hand.
    drop_penny():
        Removes a single penny from the player's hand.
    check_reroll(input_method='default'):
        Determines if the player will reroll the dice or pass their turn.
    """
    player_number = 0

    def __init__(self, is_human=False):
        """
        Initializes the Player class with the provided parameters.

        Parameters:
        -----------
        is_human: bool
            Determines if the player is human or a computer (default: False).
        """
        Player.player_number += 1
        self.player_number = Player.player_number
        self.hand = 20
        self.is_human = is_human
        self.is_winner = False

    def announce_hand(self):
        """
        Announces the number of pennies the player has, with correct grammar.

        Example:
        --------
        Player 1 has 1 penny.
        Player 2 has 5 pennies.
        """
        penny_label = "penny" if self.hand == 1 else "pennies"
        print(f"Player {self.player_number} has {self.hand} {penny_label}.")

    def roll_dice(self):
        """
        Simulates a dice roll and returns the rolled value.

        Returns:
        --------
        int
            A random integer from 1 to 6, inclusive.
        """
        return random.randint(1, 6)

    def announce_roll(self, roll):
        """
        Prints the result of the dice roll.

        Parameters:
        -----------
        roll: int
            The rolled value, an integer in [1, 6].
        """
        print(f"Player {self.player_number} rolled a {roll}!") 

    def player_roll(self):
        """
        Handles the dice rolling process for both human and computer players.

        Returns:
        --------
        int
            The result of the dice roll.
        """
        print(f"Player {self.player_number}, it's your turn.")
        if self.is_human:
            input("Press Enter to roll.")
        roll = self.roll_dice()
        self.announce_roll(roll)
        return roll

    def add_pennies(self, number):
        """
        Adds a specified number of pennies to the player's hand.

        Parameters:
        -----------
        number: int
            The number of pennies to add.

        Raises:
        -------
        ValueError:
            If the input is not a positive integer.
        """
        if not isinstance(number, int) or number < 1:
            raise ValueError(f"Invalid input value: {number}. Must be a positive integer.")
        self.hand += number

    def drop_penny(self):
        """
        Removes a single penny from the player's hand.

        Raises:
        -------
        ValueError:
            If there are no pennies left to drop.
        """
        if self.hand <= 0:
            raise ValueError("Cannot drop a penny. Player has no pennies left.")
        self.hand -= 1

    def check_reroll(self, input_method='default'):
        """
        Determines if the player wants to reroll the dice.

        Parameters:
        -----------
        input_method: str or callable
            The method to get input for human players. Defaults to 'default'.

        Returns:
        --------
        bool
            True if the player wants to reroll, False otherwise.
        """
        if self.hand == 0:
            self.is_winner = True
            return False

        if self.is_human:
            user_reroll = input_method if input_method != 'default' else input(
                f"Player {self.player_number}, would you like to roll again? (y/n): "
            )
            if user_reroll.lower() in {"y", "yes"}:
                return True
            if user_reroll.lower() in {"n", "no"}:
                return False
            print(f"{user_reroll} is not valid. Please answer 'yes' or 'no'.")
        else:
            # Simulate computer's choice (can be adjusted with game logic)
            return random.random() > 0.3
