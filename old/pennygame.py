#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: pennygame.py
Description: This script implements a simple dice game where players aim to get rid of all their chips. Players roll a six-sided die and place chips in slots labeled 1-6. Rolling a number that already has a chip results in the player taking all chips from the board, while rolling a 6 results in a chip being removed from play. The goal is to get rid of all your chips.
Author: Eva Anderson
Email: eanderson01@saintmarys.edu
Created: October 1, 2023
Last Modified: October 31, 2023
License: MIT License
"""

import random

# Helper Functions
def roll_die():
    """Return a random number between 1 and 6, simulating a die roll."""
    return random.randint(1, 6)

def display_roll(player, roll):
    """Display the outcome of a player's roll."""
    print(f"Player {player} rolled a {roll}!")

def print_game_board(board_state):
    """ Display which slots are filled with ○ and any hits with X """
    slot_fill = [" "] * 6
    for idx, value in enumerate(board_state):
        slot_fill[idx] = "○" if value == 1 else ("X" if value == 2 else " ")
    game_board = ", ".join([f"{i+1} ({slot_fill[i]})" for i in range(6)])
    print(game_board)

def display_score(player_scores):
    """ Show how many points each player is from winning."""
    print("Player \t Score")
    for player_num, score in player_scores:
        print(f"{player_num} \t\t   {score}")

def decide_reroll_com(board_state):
    """Determine if the computer player will roll again based on a pseudorandom number and the board layout."""
    print("Roll again?")
    risk = sum(board_state)
    guts = random.random()
    if guts > .16 * risk :
        return True
    return False

def decide_reroll_hum(player_num, player_scores):
    """ Ask human player if they want to roll again, pass, or check the score. If the input does not match they are given further instruction and prompted again"""
    while True:
        user_reroll = input("Roll again? (Y/N) or (S) for score ")
        if user_reroll.lower() in ['yes', 'y']:
            return True
        elif user_reroll.lower() in ['no', 'n']:
            return False
        elif user_reroll.lower() in ['s', 'score']:
            display_score(player_scores)
        else:
            print("Please try again. Input Y/N or Yes/No to take your turn. Input Score/S to see the current score.")

def determine_starting_player(num_players, num_com):
    """Determine which player goes first by simulating a roll for each player."""
    highest_roll = [[0, 0]]
    initial_rolls = [[roll_die(),i + 1] for i in range(0,num_players)]
    while True:
        
        for roll_val, player in initial_rolls:
            if player <= num_players - num_com:
                input(f"Player {player} press Enter to roll:")
            display_roll(player, roll_val)
            if roll_val > highest_roll[0][0]:
                highest_roll = [[roll_val, player]]
            elif roll_val == highest_roll[0][0]:
                highest_roll.append([roll_val, player])
        if len(highest_roll) == 1:
            break
        print(f"There's a tie among players {', '.join(str(p[1]) for p in highest_roll[:-1])} and {highest_roll[-1][1]}!")
        initial_rolls = [[roll_die(),highest_roll[i][1]] for i in range(0,len(highest_roll))]
        highest_roll = [[0,0]]
    print(f"Player {highest_roll[0][1]} will go first!")
    return highest_roll[0][1]

def get_num_players():
    """ Ask the user for the total number of players including number of com/human players."""
    int_list = ["0","1","2","3","4","5","6"]
    str_list = [["zero","none"],"one","two","three","four","five","six"]
    while True:
        num_players = input("How many players? " )
        if num_players in int_list[2:]:
            break
        elif num_players.lower() in str_list[2:]:
            num_players = int_list[str_list.index(num_players.lower())]
            break
        else:
            print("Please try again, you can have between two and six players.")
    num_players = int(num_players)
    while True:
        num_com = input("How many computer players? ")
        if num_com in int_list[:num_players]:
            break
        elif num_com.lower() in str_list[:num_players]:
            num_com = int_list[str_list.index(num_com.lower())]
        else:
            print(f"Please try again, remember you can have up to {num_players - 1} computer players.")
    num_com = int(num_com)
    return num_players, num_com, num_players - num_com

def player_roll():
    """ Prompt human players to roll die, returns result"""
    input("Press Enter to take your turn. ")
    return roll_die()

def update_rolled_values(roll, board_state):
    """ Clears the six slot and updates the board after a player's roll"""
    board_state[5] = 0
    board_state[roll - 1] += 1
    return board_state, board_state[roll - 1] > 1

def update_score(player, hit, board_state, player_scores):
    """ Update the player score both for placing and reciving pennies """
    player_scores[player-1][1] -= 1
    if hit:
        player_scores[player - 1][1] += sum(board_state) 
    return player_scores

# Initialization
total_players, comp_players, human_players = get_num_players()
player_scores = [[i + 1, 10] for i in range(total_players)]
board_state = [0] * 6

# Game Loop
current_player = determine_starting_player(total_players, comp_players)
first_roll = True
reroll_choice = True



while all(score[1] > 0 for score in player_scores):
    # Human Player's Turn
    if current_player <= human_players:
        if first_roll:
            rolled_value = player_roll()
            first_roll = False
            hit = False
        else:
            reroll_choice = decide_reroll_hum(current_player, player_scores)
    # Computer Player's Turn
    else:
        if first_roll:
            hit = False
            first_roll = False
            rolled_value = roll_die()
        else:
            reroll_choice = decide_reroll_com(board_state)

    # Update Board and Scores
    display_roll(current_player, rolled_value)
    board_state, hit = update_rolled_values(rolled_value, board_state)
    print_game_board(board_state)
    update_score(current_player, hit, board_state, player_scores)

    # Next Player or Continue Turn
    # Pass Play
    if not first_roll and not reroll_choice:
        if current_player > human_players:
            print(f"Player {current_player} has passed!")
    # Reset Board if Hit
    if hit:
        board_state = [0] * 6
    current_player = (current_player % total_players) + 1
    first_roll = True

# Determine if there has been a winner
winner = next((player for player, score in player_scores if score <= 0), None)
if winner:
    print(f"Congratulations Player {winner} you win!")
