import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        """
        Constructor for the Cell class
        """
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        """
        Setter for this cell’s value
        """
        self.value = value
    def set_sketched_value(self, value):
        """
        Setter for this cell’s sketched value
        """
        self.value = value
    def draw(self):
        """
        Draws this cell, along with the value inside it.
	    If this cell has a nonzero value, that value is displayed.
	    Otherwise, no value is displayed in the cell.
	    The cell is outlined red if it is currently selected.
        """
        if self.value == 0:
            font = pygame.font.SysFont('Arial', 30)
            self.screen.blit(font.render('', True, (0, 0, 0)), (self.row, self.col))
        else:
            font = pygame.font.SysFont('Arial', 30)
            self.screen.blit(font.render('str(self.value)', True, (0, 0, 0)), (self.row, self.col))
