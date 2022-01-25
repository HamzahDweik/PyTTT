import pygame

if __name__ == '__main__':

    # initialize the pygame and create the screen
    pygame.init()
    screen = pygame.display.set_mode((330, 330))

    # set caption and icon, icon created by Prosymbols on Flaticon
    pygame.display.set_caption('Tic-Tac-Toe')
    icon = pygame.image.load('tic-tac-toe.png')
    pygame.display.set_icon(icon)

    # initialize game display components
    board_img = pygame.image.load('board.png')
    boardX = 15
    boardY = 15

    def board():
        screen.blit(board_img,(boardX, boardY))

    # runs the game
    running = True
    while running:
        # handles quit functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # sets the color of the background to white
        screen.fill((255, 255, 255))

        # displays board
        board()
        pygame.display.update()
