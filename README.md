# P4-COP3502C-EG-SZ

This was a project in COP3502C Programming Fundamentals 1 at the University of Florida. The assignment was to build a Python Sudoku application with a Pygame graphical user interface. The project structure and features are documented below.

## Sudoku Game Project

### Overview
Sudoku is a logic-based number placement puzzle on a 9x9 grid divided into nine 3x3 subgrids. Each row, column, and 3x3 box must contain the digits 1 through 9 without repetition.

In this project, you implement a playable Python and Pygame Sudoku game featuring puzzle generation across multiple difficulty tiers, interactive cell navigation and entry, board state management, and win/loss evaluation.

### Core Responsibilities
- Encapsulate board state, cell properties, and puzzle logic cleanly across modules.
- Generate valid Sudoku boards with selectable difficulty levels and solvable configurations.
- Handle mouse and keyboard events to navigate cells, enter/clear values, and trigger game actions.
- Validate completed boards and display clear game states for welcome, active play, and end screens.

### Gameplay Interface & Functionality

| Action / Control | Input / Trigger | Description & Behavior |
| :--- | :--- | :--- |
| Difficulty Selection | Welcome screen click | Chooses puzzle difficulty (Easy: 30 cells removed, Medium: 40 cells removed, Hard: 50 cells removed) and starts a new board. |
| Navigate Board | Mouse click or Arrow keys | Moves active selection across the 9x9 grid with visual highlight feedback. |
| Enter Number | Keys `1`–`9` | Writes a candidate digit into a non-fixed cell. |
| Clear Cell | `Backspace` (or delete key) | Removes a user-entered digit from the selected cell; does not alter fixed clues. |
| Reset | Reset button | Clears all user-entered values while preserving initial puzzle clues. |
| Restart | Restart button | Returns to the difficulty selection screen to start a fresh game. |
| Exit | Exit button | Closes the Pygame window and terminates the application. |
| Board Completion | Automatic when full | Evaluates the completed 9x9 grid against solution rules and transitions to a win or loss screen. |

### Constraints & Rules
- **Fixed vs. User Cells**: Initial puzzle clues are fixed and distinguished visually from user-entered numbers; user entries can be edited or cleared until submission/completion.
- **Grid Bounds**: All row and column indices stay within the 9x9 board (`0` through `8`) and nine 3x3 blocks.
- **Game State Transitions**: Transitions cleanly between menu/difficulty selection, active gameplay, and win/loss screens.

### Technical Specifications
- **Language**: Python 3.x
- **GUI Library**: Pygame
- **Core Concepts**: Object-Oriented Programming (OOP), event-driven event loops, 2D lists/grids, backtracking, and modular file organization.
- **Repository**: `https://github.com/EzraGerstein/P4-COP3502C-EG-SZ`

### Getting Started

#### Prerequisites
- Python 3.x
- `pygame` (`pip install pygame`)

#### Setup & Execution
```bash
git clone [https://github.com/EzraGerstein/P4-COP3502C-EG-SZ.git](https://github.com/EzraGerstein/P4-COP3502C-EG-SZ.git)
cd P4-COP3502C-EG-SZ
pip install pygame
python sudoku.py
