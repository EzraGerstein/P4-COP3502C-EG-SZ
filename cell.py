import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        """
        Constructor for the Cell class
        """
        self.sketched_value = 0
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.white_square = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.white_square.fill((255, 255, 255))
        self.is_original = False

    def set_cell_value(self, value):
        """
        Setter for this cell’s value
        """
        if self.is_original:
            self.value = value
    def set_sketched_value(self, value):
        """
        Setter for this cell’s sketched value
        """
        if self.is_original:
            self.sketched_value = value
    def draw(self):
        """
        Draws this cell, along with the value inside it.
	    If this cell has a nonzero value, that value is displayed.
	    Otherwise, no value is displayed in the cell.
	    The cell is outlined red if it is currently selected.
        """
        if self.value == 0:
            self.white_square.fill((255, 255, 255))
        else:
            font = pygame.font.SysFont('Arial', 30)
            self.white_square.blit(font.render(str(self.value), True, (0, 0, 0)), (19, 7))