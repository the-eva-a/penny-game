# The Penny Game

The Penny Game is a simple Python-based game inspired by the real-life game [Penny Drop](https://www.creativecrafthouse.com/penny-drop-premium-version-fun-family-or-bar-game.html), which I play with my family every Thanksgiving.

## Table of Contents
- [Description](#description)
- [How to Play](#how-to-play)
- [The Evolution of The Penny Game](#the-evolution-of-the-penny-game)
- [Features](#features)
- [Testing](#testing)
- [Issues](#issues)
- [Next Steps](#next-steps)
- [Feedback and Contribution](#feedback-and-contribution)

---

## Description
The Penny Game is a game of chance for two to six players, with at least one human player required. Other players can be human or computer players using simple AI logic. The game is designed to mimic the physical version of Penny Drop, complete with rules for rolling, placing pennies, and interacting with a slot-based board.

![A wooden box with six slots on top; each slot corresponds to a number from one to six. There is a wooden penny and die on top of the box for scale](https://www.creativecrafthouse.com/mm5/graphics/00000001/2/0/20200313_141125_clipped_rev_1_480x270.jpeg)

---

## How to Play
1. Enter the total number of players and the number of computer players.
2. Roll the dice to determine the starting player (ties are rerolled).
3. Players take turns rolling and placing pennies in the corresponding slots:
   - Slot 6 is always open, allowing pennies to drop through.
   - If a slot is occupied, all pennies in that slot are collected by the roller.
4. Players decide whether to roll again or pass their turn to the next player.
5. The game ends when a player places all their pennies on the board.

**Reading the Screen**  
After each roll, the board configuration is displayed:  
![Program output showing an example board configuration 1 (X), 2 (○), 3 (○), 4 ( ), 5 (○), 6 ( )](https://github.com/the-eva-a/petting-zoo/assets/149191168/6f866e45-f66c-435a-a549-50fbd6474e61)

---

## The Evolution of The Penny Game

This project originally started as a simple procedural implementation of the Penny Game, designed to focus on basic gameplay mechanics. Over time, I’ve restructured the project into a more modular, class-based version. Below is a comparison of the old and new versions:

### Old Version
- **Structure**:
  - Used procedural programming with global variables and functions.
  - Gameplay logic was tightly coupled, making it harder to test or modify individual components.
- **Strengths**:
  - Straightforward implementation for quick prototyping.
  - Allowed me to experiment with core mechanics and Python basics.
- **Limitations**:
  - Difficult to extend or debug as the project grew.
  - Lacked clear separation of concerns between player management, board mechanics, and gameplay flow.

### New Version
- **Structure**:
  - Built around an object-oriented approach using the `Player` class.
  - Each player is an independent object that tracks their state (e.g., hand size, player number, human vs. computer).
  - Improved separation of concerns with a modular design that will allow for future integration with a `GameBoard` class.
- **Improvements**:
  - **Readability**: Code is easier to understand with clear, reusable methods and descriptive docstrings.
  - **Testability**: Comprehensive unit tests now validate individual behaviors (e.g., dice rolling, penny management).
  - **Scalability**: The class structure lays a foundation for adding new features, like advanced AI or a graphical interface.

---

## Features
### **Code Updates**
- **`Player` Class**:
  - Tracks player attributes like hand size, type (human or COM), and player number.
  - Handles dice rolls, penny management (adding/removing), and reroll decisions.
  - Modular, scalable design for integration with additional components like `GameBoard`.
  
- **Improved Code Quality**:
  - Readable and modular structure with clear, descriptive method names and docstrings.
  - Input validation to handle edge cases like invalid or non-numeric inputs.

### **New Testing Framework**
- Comprehensive unit testing with `unittest` ensures reliability:
  - Tests for player creation, dice rolling, penny management, and reroll decisions.
  - Extensive edge case coverage (e.g., invalid inputs, boundary conditions).
  - Clear separation of test cases for easy debugging.

---

## Testing
To run all tests, use Python's `unittest` module:
```bash
python -m unittest discover
``` 
### Key Areas Tested:
- **Player Creation**: Ensures human and COM players are initialized correctly.
- **Dice Rolling**: Confirms rolls are within the range of 1-6.
- **Penny Management**: Tests adding/removing pennies with valid and invalid inputs.
- **Reroll Logic**: Verifies reroll behavior and winner detection for both human and COM players.

Example Test Output:
``` 
...
Ran 25 tests in 0.012s

OK
```

## Known Issues and Areas for Improvement
### Known Issues and Areas for Improvement
1. **Incomplete Functionality**  
   - The game lacks a functioning game loop, advanced error handling, and full test coverage for interactions between classes.

2. **No User Interface or Deployment**  
   - There is no user interface (text-based or graphical) or deployment options, limiting accessibility for non-developers.

3. **Documentation Gaps**  
   - Rules, usage examples, and contribution guidelines are minimal or missing. Licensing information is not included.

## Next Steps

### Short-Term
1. **Complete Code and Tests for `GameBoard` Class**  
   - Finalize the implementation of the `GameBoard` class to manage the game board, including functionality for adding pennies, checking for crashes, and resetting the board. Write thorough unit tests to ensure reliability.

2. **Finalize Code for `Game` Class**  
   - Implement the `Game` class to handle core gameplay logic, including interactions with the `Player` and `GameBoard` classes.

3. **Set Up the Game Loop**  
   - Develop a functioning game loop that ties together all components (`Player`, `GameBoard`, and `Game`) to simulate a full round of gameplay.

4. **Enhance Documentation and Examples**  
   - Update the README with usage examples for both the `GameBoard` and `Game` classes, and ensure the rules of the game are clearly explained.

---

### Long-Term
1. **Add a User Interface**  
   - Design a text-based or graphical user interface to make the game accessible to a broader audience.

2. **Expand Features and Scalability**  
   - Introduce new gameplay features, such as enhanced player mechanics, multiplayer support, and a scoring system.

3. **Package and Deploy**  
   - Package the game for distribution as a CLI tool or lightweight application.

4. **Visualize Game Data**  
   - Add basic data visualizations, such as gameplay statistics or win rates, for an analytical edge.


5. **Enhance README**  
   - Add a game loop overview or flowchart.
   - Expand game rules for clarity.
   - Include contribution guidelines.
   - Add a license section.
---

## Feedback and Contribution
I welcome feedback and contributions! Whether it’s a suggestion for a feature or improvements to the existing code, feel free to open an issue or submit a pull request.

Contributions are welcome! Please ensure any pull requests include descriptive commit messages and follow the project structure.

Please keep feedback constructive and respectful—this project is a learning experience, and I'm always working to improve. Thank you for your kindness and support!

