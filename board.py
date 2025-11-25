import pygame
from cell import Cell
from sudoku_generator import *

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
        self.screen = screen
        self.cell_holder = []
        self.selected_cell = None

        if difficulty == 3:
            self.generator = SudokuGenerator(9, 50)
            self.sudoku_b = generate_sudoku(9, 50)
            self.original_board = [row[:] for row in self.sudoku_b]
        elif difficulty == 2:
            self.generator = SudokuGenerator(9, 40)
            self.sudoku_b = generate_sudoku(9, 40)
            self.original_board = [row[:] for row in self.sudoku_b]
        else:
            self.generator = SudokuGenerator(9, 30)
            self.sudoku_b = generate_sudoku(9, 30)
            self.original_board = [row[:] for row in self.sudoku_b]

    def draw(self):
        """
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	    Draws every cell on this board.
        """
        self.screen.fill('white')

        for row in range(9):
            cell_list = list()
            for col in range(9):
                c = Cell(self.sudoku_b[row][col], row, col, self.screen)
                cell_list.append(c)
                c.draw()
                self.screen.blit(c.white_square, (row * 50, col * 50))
            self.cell_holder.append(cell_list)

        for x in range(0, self.width, 50):
            if x % 150 == 0:
                pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height), 3)
            else:
                pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height))
        for y in range(0, self.height, 50):
            if y % 150 == 0:
                pygame.draw.line(self.screen, 'black', (0, y), (self.width, y), 3)
            else:
                pygame.draw.line(self.screen, 'black', (0, y), (self.width, y))


    def select(self, row, col):

        """
        Marks the cell at (row, col) in the board as the current selected cell.
	    Once a cell has been selected, the user can edit its value or sketched value.
        """
        pygame.draw.rect(self.screen, (255, 0, 0), (row * 50, col * 50, 50, 50), 3)
        self.selected_cell = self.cell_holder[row][col]

    def click(self, x, y):
        """
        If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None.
        """
        for row in range(9):
            for col in range(9):
                if (col * 50) < y < (col * 50) + 50 and (row * 50) < x < (row * 50) + 50:
                    return row, col
        return None


    def clear(self):
        """
        Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves.
        """
        self.selected_cell.set_cell_value(0)
        self.selected_cell.set_sketched_value(0)

    def sketch(self, value):
        """
        Sets the sketched value of the current selected cell equal to the user entered value.
	    It will be displayed at the top left corner of the cell using the draw() function.
        """
        self.selected_cell.set_sketched_value(value)
    def place_number(self, value):
        """
        Sets the value of the current selected cell equal to the user entered value.
        Called when the user presses the Enter key.
        """
        self.selected_cell.set_cell_value(value)
    def reset_to_original(self):
        """
        Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit).
        """
        self.sudoku_b = [row[:] for row in self.original_board]
        #here, rebuild cell constructor so the UI actually updates.
        self.cell_holder = []
        for row in range(9):
            row_cells = []
            for col in range(9):
                c = Cell(self.sudoku_b[row][col], row, col, self.screen)
                row_cells.append(c)
            self.cell_holder.append(row_cells)
        self.draw()

    def is_full(self):
        """
        Returns a Boolean value indicating whether the board is full or not.
        """
        for row in range(9):
            for col in range(9):
                if self.cell_holder[row][col].value == 0:
                    return False
        return True


    def update_board(self):
        """
        Updates the underlying 2D board with the values in all cells.
        """
        for row in range(9):
            for col in range(9):
                self.sudoku_b[row][col].value = self.cell_holder[row][col].value

    def find_empty(self):
        """
        Finds an empty cell and returns its row and col as a tuple (x,y).
        """
        for row in range(9):
            for col in range(9):
                if self.cell_holder[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        """
        Check whether the Sudoku board is solved correctly.
        """
        #The logic > loop over row and col to check for the number and then check for number on each 3 x 3 square.
        self.update_board()
        for row in range(9):
            for col in range(9):
                num = self.cell_holder[row][col].value
                if num == 0:
                    return False
                if not self.generator.is_valid(row, col, num):
                    return False
        return True



