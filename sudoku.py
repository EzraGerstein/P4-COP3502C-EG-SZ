from board import Board
from cell import Cell
import pygame

def main():

    pygame.init()
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()

    # Start screen
    screen = pygame.display.set_mode((450, 450))

    # Images

    image_start = pygame.image.load("Main Screen.jpeg")
    image_start_scaled = pygame.transform.scale(image_start, (450, 450))

    image_win = pygame.image.load("Game Won with Exit.jpeg")
    image_win_scaled = pygame.transform.scale(image_win, (450, 450))

    image_over = pygame.image.load("Game Over without Restart.jpeg")
    image_over_scaled = pygame.transform.scale(image_over, (450, 450))

    # Values needed for start screen loop
    starting = True
    difficulty_level = 1
    sudoku_board = None
    dont_start = False

    # Start screen loop
    while starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                starting = False
                dont_start = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 100 <= x <= 200 and 250 <= y <= 300:
                    difficulty_level = 1
                    starting = False

                elif 180 <= x <= 320 and 250 <= y <= 300:
                    difficulty_level = 2
                    starting = False

                elif 290 <= x <= 400 and 250 <= y <= 300:
                    difficulty_level = 3
                    starting = False
        screen.fill((0, 0, 0))
        screen.blit(image_start_scaled, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    # Start screen ends
    if not starting:
        sudoku_board = Board(450, 450, screen, difficulty_level)
        sudoku_board.draw()

    # Values needed for sudoku loop
    running = True
    game_state = "RUNNING"
    pos = None
    # Sudoku loop
    while running:
        if dont_start:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 300 and 275 <= y <= 325:
                    if game_state == "OVER":
                        running = False
                    elif game_state == "WON":
                        running = False
                if game_state == "RUNNING":
                    pos = sudoku_board.click(x, y)
                    if pos is not None:
                        selected_row, selected_col = pos
                        sudoku_board.select(selected_row, selected_col)
                        sudoku_board.draw()
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57:
                        sudoku_board.sketch(event.key - pygame.K_0)
                    case pygame.K_RETURN:
                        sudoku_board.place_number(sudoku_board.selected_cell.sketched_value)

                        # Check for win condition
                        if sudoku_board.is_full():
                            if sudoku_board.check_board():
                                game_state = "WON"
                            else:
                                game_state = "OVER"

                    case pygame.K_BACKSPACE:
                        sudoku_board.clear()

        # Check state
        if game_state == "RUNNING":
            sudoku_board.draw()
            sudoku_board.update_board()
        elif game_state == "WON":
            screen.blit(image_win_scaled, (0, 0))
        elif game_state == "OVER":
            screen.blit(image_over_scaled, (0, 0))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()