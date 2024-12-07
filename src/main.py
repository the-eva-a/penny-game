from game_board import GameBoard
from player import Player
from game import Game

input("Welcome to The Penny Game!\nPress Enter to continue:")
# initalize board
myBoard = GameBoard()
# initalize game
myGame = Game()
myGame.get_numplayers()
myGame.get_numcom()
myGame.create_players()

def basic_roll():
    """
    Simulates a basic turn for the current player, including rolling the dice, 
    dropping a penny, and updating the game board.

    The function performs the following steps:
    1. Rolls a die to determine where to place the penny on the board.
    2. Removes a penny from the current player's hand.
    3. Adds the penny to the appropriate slot on the game board.
    4. Checks if the game board has crashed after the penny is placed.
    5. If no crash occurs, checks if the current player meets the winning condition.
    6. Displays the current state of the game board.

    Parameters:
    None

    Returns:
    None
    """
     # get dice roll 
    roll_result = current_player.player_roll()
    # take penny from player
    current_player.drop_penny()
    # place penny in proper slot
    myBoard.add_penny(roll_result)
    if myBoard.crash == False:
        current_player.check_winner()
     # show board
    myBoard.print_board()

# Set up play order
current_player_num = myGame.who_first()
# Main game loop
while not myGame.game_winner:
    # set current player
    current_player = myGame.players[current_player_num]
    basic_roll()

    # Check for rerolls and crashes
    while (current_player.check_reroll()):
        basic_roll()
        if myBoard.crash: # Exit if a crash occurs
            print("Oh no! There has been a crash!")
            break
    if myBoard.crash:
        player_pennies = myBoard.clear_board()
        print(f"Player {current_player.player_number} picked up {player_pennies}")
        current_player.hand += player_pennies
        print(f"Their new hand size is  {current_player.hand} pennies.")
    else:
        print(f"{current_player_num} has {current_player.hand} pennies remaining")
    if current_player.hand == 0:
        myGame.game_winner = current_player.player_number
    current_player_num = current_player.player_number % myGame.numplayers + 1
myGame.final_scores()
   
    
