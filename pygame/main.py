import pygame
from os import path
from globals import WHITE, FPS, WIDTH, HEIGHT, SS_H, SS_W
from keyhandle import handle_keys_red, handle_keys_yellow


# Initializing surfaces
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
Y_SPACESHIP_IMG = pygame.image.load(
    path.join('Assets', 'yellship.png'))
Y_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(Y_SPACESHIP_IMG, (SS_H, SS_W)), 90)
R_SPACESHIP_IMG = pygame.image.load(
    path.join('Assets', 'redship.png'))
R_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(R_SPACESHIP_IMG, (SS_H, SS_W)), 270)

window = pygame.display.set_mode((WIDTH, HEIGHT))

# Load and scale the background image
BACKGROUND = pygame.image.load(
    path.join('Assets', 'background4.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

pygame.display.set_caption("Space Ship Shooter")


def set_window(colour, yellow, red):
    window.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(window, WHITE, BORDER)
    window.blit(Y_SPACESHIP_IMG, (yellow.x, yellow.y))
    window.blit(R_SPACESHIP_IMG, (red.x, red.y))
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
