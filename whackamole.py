import pygame
import random

def draw_grid(screen):
    for i in range(20):
        pygame.draw.line(screen, (0,0,0), ((i+1)*32, 0), ((i+1)*32, 512))
    for i in range(16):
        pygame.draw.line(screen, (0,0,0), (0, (i+1)*32), (640, (i+1)*32))

def initialize_board():
    board =  [["-" for i in range(20)] for i in range(16)]
    board[0][0] = 'm'
    return board

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        current_position = [0, 0]
        board = initialize_board()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // 32
                    row = y // 32
                    if board[row][col] == 'm':
                        board[row][col] = '-'
                        new_row = random.randrange(0, 16)
                        new_col = random.randrange(0, 20)
                        current_position = [new_row, new_col]
                        board[new_row][new_col] = 'm'

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(current_position[1]*32,current_position[0]*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
