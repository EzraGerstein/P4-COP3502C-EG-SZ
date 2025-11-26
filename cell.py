import pygame

class Cell:
    def __init__(self, value, row, col, screen, large_font, small_font):
        """
        Constructor for the Cell class
        """
        self.sketched_value = 0
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.white_square = pygame.Surface((50, 50))
        self.white_square.fill((255, 255, 255))
        self.is_original = False
        self.is_selected = False
        self.large_font = large_font
        self.small_font = small_font

    def set_cell_value(self, value):
        """
        Setter for this cell’s value
        """
        if not self.is_original:
            self.value = value
            self.sketched_value = 0
            self.draw()
    def set_sketched_value(self, value):
        """
        Setter for this cell’s sketched value
        """
        if not self.is_original and self.value == 0:
            self.sketched_value = value
            self.draw()
    def draw(self):
        """
        Draws this cell, along with the value inside it.
	    If this cell has a nonzero value, that value is displayed.
	    Otherwise, no value is displayed in the cell.
	    The cell is outlined red if it is currently selected.
        """
        self.white_square.fill((255, 255, 255))
        if self.is_selected:
            pygame.draw.rect(self.white_square, (255, 0, 0), (0, 0, 50, 50), 3)
        if self.value != 0:
            font = pygame.font.SysFont('Arial', 30)
            self.white_square.blit(self.large_font.render(str(self.value), True, (0, 0, 0)), (19, 7))

        elif self.sketched_value != 0:
            font = pygame.font.SysFont('Arial', 15)
            self.white_square.blit(self.small_font.render(str(self.sketched_value), True, (128, 128, 128)), (5, 5))
