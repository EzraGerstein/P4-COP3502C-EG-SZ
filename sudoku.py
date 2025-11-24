from board import Board
from cell import Cell
import pygame

def main():
    pygame.init()
    sudoku_board = Board(450, 450, pygame.display.set_caption("Sudoku"), 30)
    sudoku_board.draw()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()