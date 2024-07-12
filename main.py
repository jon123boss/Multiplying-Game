import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 182, 193)
RADIUS = 10
PADDING = 20
NUM_ROWS = 5
NUM_COLS = 5

square_width = (SCREEN_WIDTH - (NUM_COLS + 1) * PADDING) // NUM_COLS
square_height = (SCREEN_HEIGHT - (NUM_ROWS + 1) * PADDING) // NUM_ROWS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiplying game")

blob_size = min(square_width, square_height) / 2
blob_color = LIGHT_BLUE
turn = 0
player_turn = 0

blobs = [[None for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
dots = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for row in range(NUM_ROWS):
                for col in range(NUM_COLS):
                    x = PADDING + col * (square_width + PADDING)
                    y = PADDING + row * (square_height + PADDING)
                    if x <= mouse_x <= x + square_width and y <= mouse_y <= y + square_height:
                        if blobs[row][col] is None:
                            if player_turn == turn % 2:
                                blobs[row][col] = turn % 2
                                turn += 1
                                player_turn = 1 - player_turn
                        elif blobs[row][col] == turn % 2 and dots[row][col] < 3:
                            dots[row][col] += 1

    if turn % 2 == 0:
        screen.fill(LIGHT_BLUE)
    else:
        screen.fill(LIGHT_RED)

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = PADDING + col * (square_width + PADDING)
            y = PADDING + row * (square_height + PADDING)

            pygame.draw.rect(screen, GRAY, (x, y, square_width, square_height), border_radius=RADIUS)

            if blobs[row][col] is not None:
                blob_color = LIGHT_BLUE if blobs[row][col] == 0 else LIGHT_RED
                blob_x = x + square_width // 2 - blob_size // 2
                blob_y = y + square_height // 2 - blob_size // 2
                pygame.draw.rect(screen, blob_color, (blob_x, blob_y, blob_size, blob_size), border_radius=RADIUS)

                for dot in range(dots[row][col]):
                    dot_x = blob_x + blob_size // 2
                    dot_y = blob_y + blob_size // 2 - (dots[row][col] - 1) * 5 + dot * 10
                    pygame.draw.circle(screen, WHITE, (dot_x, dot_y), 5)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()