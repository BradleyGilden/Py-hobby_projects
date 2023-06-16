import pygame
from globals import WHITE, FPS, SS_H, SS_W
from keyhandle import handle_keys_red, handle_keys_yellow
from surfaces import M_WINDOW, Y_SPACESHIP_IMG, R_SPACESHIP_IMG
from surfaces import BACKGROUND, BORDER


pygame.display.set_caption("Space Ship Shooter")


def set_window(colour, yellow, red):
    M_WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(M_WINDOW, WHITE, BORDER)
    M_WINDOW.blit(Y_SPACESHIP_IMG, (yellow.x, yellow.y))
    M_WINDOW.blit(R_SPACESHIP_IMG, (red.x, red.y))
    pygame.display.update()


def main():
    yellow = pygame.Rect(200, 200, SS_W, SS_H)
    red = pygame.Rect(700, 200, SS_W, SS_H)
    clock = pygame.time.Clock()
    running = True
    while running:  # program loop
        clock.tick(FPS)  # controls fast the loop is running per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking events in real time
                running = False
        handle_keys_yellow(yellow)
        handle_keys_red(red)
        set_window(WHITE, yellow, red)
    pygame.quit()


if __name__ == '__main__':
    main()
