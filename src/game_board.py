# game_board.py
# This file contains the GameBoard class, which is responsible for managing the game board
# where pennies are added, checked for crashes, and the board can be reset.

# Author: Eva Anderson
# Created: 10/01/24
# Last Modified: 11/22/24

# Dependencies:
# - No external dependencies

# Usage Example:
# board = GameBoard()
# board.add_penny(3)
# board.print_board()


# Class Responsibilities:
# - Track the game board state using slots 1 to 6.
# - Handle adding pennies to slots and checking for penny collisions.
# - Print the current state of the board and reset the board when needed.

class GameBoard:
    """
    The GameBoard class manages the virtual 6-slot game board.
    It tracks the state of each slot, checks for crashes (instances where more than one 
    penny is added to the same slot), and provides methods to update and reset the board.
    
    Attributes:
    ----------
    state: dict
        A dictionary representing the current state of the board. Keys are slot numbers
        (1 to 6), and values are 0 (empty), 1 (occupied), or >1 (crashed).
    crash: bool
        A flag that indicates whether a crash (penny collision) has occured

    Methods:
    ---------
    print_board():
        Prints a visual representation of the current board state.

    add_penny(slot):
        Adds a penny to the specified slot. If a penny is already in that slot,
        it sets the crash flag to True.

    clear_board():
        Resets the board and returns the number of pennies collected from all slots.
    """
    def __init__(self):
        """
        Initializes the GameBoard with six empty slots and sets the crash flag to False.

        Attributes:
        -----------
        state: dict
            Initalizes all slots (1-6) with a value of 0 (empty)
        crash: bool
            Initalizes the crash flag to False
        """
        self.state = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} # Sets all slots as empty
        self.crash = False # There is no penny collision
    
    def print_board(self):
        """
        Prints a visual representation of the current state of the game board.

        Each slot number is displayed next to its corresponding value:
        ( ) for empty, (O) for one penny, (X) for a crash
        """
        board_string = ""
        for key, value in self.state.items():
            if value == 0:
                board_string += f"{key} ( ) "
            elif value == 1:
                board_string += f"{key} (O) "
            else:
                board_string += f"{key} (X) "
        print(board_string)

    def add_penny(self, slot):
        """
        Adds a penny to the specified slot on the board. 

        Attributes:
        -----------
        slot: int
            The slot number (1-6) where the penny is to be added

        Raises:
        -------
        ValueError: If the slot number is outside the range from 1 to 6
        """
        if slot not in self.state:
            raise ValueError("Slot number must be between 1 and 6.")
    
        self.state[6] = 0 # The sixth slot resets to empty
        self.state[slot] += 1
        if self.state[slot] > 1:
            self.crash = True
    
    def clear_board(self):
        """
        Resets the board by clearing all pennies and resetting the crash flag.

        Returns:
        --------
        penny_return: int
            The total number of pennies collected from all slots before the board was reset. 
        """
        penny_return = sum(self.state.values())
        self.state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # Reset all slots to empty
        self.crash = False
        return penny_return
    