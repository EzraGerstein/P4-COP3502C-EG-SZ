import pygame
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        """
	    Constructor for the Board class.
	    screen is a window from PyGame.
	    difficulty is a variable to indicate if the user chose easy medium, or hard.
        """
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        """
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	    Draws every cell on this board.
        """
        self.screen.fill('white')
        for x in range(0, self.width, 50):
            if x % 150 == 0:
                pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height), 3)
            else:
                pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height))
        for y in range(0, self.height, 50):
            if y % 150 == 0:
                pygame.draw.line(self.screen, 'black', (0, y), (self.width, y), 3)
            else:
                pygame.draw.line(self.screen, 'black', (0, y), (self.width, y),)
        for x in range(0, self.width, 50):
            for y in range(0, self.height, 50):
                Cell(0, x, y, self.screen).draw()
    def select(self, row, col):
        """
        Marks the cell at (row, col) in the board as the current selected cell.
	    Once a cell has been selected, the user can edit its value or sketched value.
        """

    def click(self, x, y):
        """
        If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None.
        """

    def clear(self):
        """
        Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves.
        """

    def sketch(self, value):
        """
        Sets the sketched value of the current selected cell equal to the user entered value.
	    It will be displayed at the top left corner of the cell using the draw() function.
        """

    def place_number(self, value):
        """
        Sets the value of the current selected cell equal to the user entered value.
        Called when the user presses the Enter key.
        """
    def reset_to_original(self):
        """
        Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit).
        """

    def is_full(self):
        """
        Returns a Boolean value indicating whether the board is full or not.
        """

    def update_board(self):
        """
        Updates the underlying 2D board with the values in all cells.
        """

    def find_empty(self):
        """
        Finds an empty cell and returns its row and col as a tuple (x,y).
        """

    def check_board(self):
        """
        Check whether the Sudoku board is solved correctly.
        """
Board(450, 450, 20, 30)