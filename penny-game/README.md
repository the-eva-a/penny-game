# The Penny Game

The Penny Game is a simple Python-based game based on the game [Penny Drop](https://www.creativecrafthouse.com/penny-drop-premium-version-fun-family-or-bar-game.html) that I play with my family every Thanksgiving. 

## Table of Contents
- [Description](#description)
- [How to Play](#how-to-play)
- [Issues](#issues)
- [Contributing](#contributing)
- [License](#license)
- [Things I'm Happy About](#things-i'm-happy-about)

## Description
The Penny Game is a simple game of chance for two to six players. There must be at least one human player, but the rest can be human or computer players running simple logic. In real life, the game looks like this,
![A wooden box with six slots on top; each slot corresponds to a number from one to six. There is a wooden penny and die on top of the box for scale](https://www.creativecrafthouse.com/mm5/graphics/00000001/2/0/20200313_141125_clipped_rev_1_480x270.jpeg)

**Gameplay**
1. **Setup**: Each player begins with a collection of 12 pennies
2. **Turn Sequence**: Players roll a die; highest roll goes first
3. **Penny Placement**: Following a roll, the player must place one of their pennies into the slot that corresponds to the rolled number
   * **The Exception**: Slot 6 is open at the bottom, pennies fall through and it is always open
4. **Occupied Slot**: If the slot already holds a penny, the roller takes all pennies from the slots and adds them to their stash
5. **Decision Time**: If the slot is otherwise unoccupied, the player may choose to roll again or pass their turn to the next player
7. 

## How to Play
1. The user will be prompted to enter the total number of players and the number of computer players.
2. All players will be prompted to roll for who goes first; ties will be rerolled
3. Computer players will take their turns automatically
4. Human players will be prompted to roll (or pass if possible). They can also check their score with 's'
5. After each roll, points are added or deduced
6. The game ends once a player gets rid of all of their pennies

## Issues
As the program is still being developed, many things could go wrong; here are a few
- Sometimes, scoring does not update properly, and you end up with more pennies than you started with
- I am trying to fine-tune the delay after computer players make their moves, but it can be quite fast or slow
- It's not very good to look at

## Contributing

Feel free to fork the project. All contributions are welcome, especially notes on things not working as they should.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Key Features I'm Happy About
Here are a few things this project let me practice:
* I learned a lot about getting and handling user input, including redundancies for unwanted inputs
* I am working hard on creating good function and variable names as well as providing well-commented code
* This is a very fun warm-up in Python project
