Python CLI Minesweeper Game



A command-line interface (CLI) implementation of the classic Minesweeper puzzle game.



Features

&nbsp;- Core Game Logic: Implements bomb placement, adjacent bomb counting, marking/flagging, and game-over/win states.

&nbsp;- Boundary Checking: Includes logic to ensure all checks for adjacent tiles remain within the 10x10 board limits.

&nbsp;- Auto-Reveal Logic: Includes the flood-fill algorithm to automatically uncover empty adjacent squares and their numerical neighbors.

&nbsp;- Terminal Interface: Simple, text-based interface for displaying the 10x10 grid and managing player input (e.g., `0a` to dig at coordinate 0, a).



Installation

This game requires standard Python libraries (`time`, `random`).



1\.  Clone the Repository:

&nbsp;   ```bash

&nbsp;   git clone https://github.com/zbyszekwicher/python-cli-minesweeper-game.git

&nbsp;   cd python-cli-minesweeper-game

&nbsp;   ```



2\.  Run the Game:

&nbsp;   ```bash

&nbsp;   python cli_minesweeper.py

&nbsp;   ```

