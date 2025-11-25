from board import Board
from cell import Cell
import pygame

def main():

    pygame.init()
    pygame.display.set_caption("Sudoku")
    sudoku_board = Board(450, 450, pygame.display.set_mode((450, 450)), 3)
    sudoku_board.draw()

    # Blocks User from editing original values
    for row in range(len(sudoku_board.cell_holder)):
        for original_cell in sudoku_board.cell_holder[row]:
            if original_cell.value != 0:
                original_cell.is_original = True

    clock = pygame.time.Clock()
    running = True
    old_positioning = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = sudoku_board.click(event.pos[0], event.pos[1])
                if pos is not None and (old_positioning is None or old_positioning != event.pos):
                    sudoku_board.draw()
                    old_positioning = event.pos
                    selected_row, selected_col = pos
                    sudoku_board.select(selected_row, selected_col)


            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case 1:
                       sudoku_board.sketch(1)
                    case 2:
                        sudoku_board.sketch(2)
                    case 3:
                        sudoku_board.sketch(3)
                    case 4:
                        sudoku_board.sketch(4)
                    case 5:
                        sudoku_board.sketch(5)
                    case 6:
                        sudoku_board.sketch(6)
                    case 7:
                        sudoku_board.sketch(7)
                    case 8:
                        sudoku_board.sketch(8)
                    case 9:
                        sudoku_board.sketch(9)
                    case ENTER:
                        sudoku_board.place_number(14)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()