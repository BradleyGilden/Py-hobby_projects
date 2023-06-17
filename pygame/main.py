import pygame
from globals import WHITE, FPS, SS_H, SS_W, CENTER, RED, YELLOW
from keyhandle import handle_keys_red, handle_keys_yellow
from surfaces import M_WINDOW, Y_SPACESHIP_IMG, R_SPACESHIP_IMG
from surfaces import BACKGROUND, BORDER
from projectiles import bullets_setup, handle_bullets


pygame.display.set_caption("Space Ship Shooter")


def set_window(yellow, red, r_bullet, y_bullet):
    M_WINDOW.blit(BACKGROUND, CENTER)
    pygame.draw.rect(M_WINDOW, WHITE, BORDER)
    M_WINDOW.blit(Y_SPACESHIP_IMG, (yellow.x, yellow.y))
    M_WINDOW.blit(R_SPACESHIP_IMG, (red.x, red.y))

    for bullet in r_bullet:
        pygame.draw.rect(M_WINDOW, RED, bullet)
    for bullet in y_bullet:
        pygame.draw.rect(M_WINDOW, YELLOW, bullet)

    pygame.display.update()


def main():
    bullet = []
    y_bullet = []
    r_bullet = []
    yellow = pygame.Rect(200, 200, SS_W, SS_H)
    red = pygame.Rect(700, 200, SS_W, SS_H)
    clock = pygame.time.Clock()
    running = True
    while running:  # program loop
        clock.tick(FPS)  # controls fast the loop is running per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking events in real time
                running = False
        bullets_setup(event, yellow, red, y_bullet, r_bullet, bullet)
        key_pressed = pygame.key.get_pressed()  # get pressed keys from user
        handle_keys_yellow(yellow, key_pressed)
        handle_keys_red(red, key_pressed)
        handle_bullets(y_bullet, r_bullet, yellow, red)
        set_window(yellow, red, y_bullet, r_bullet)
    pygame.quit()


if __name__ == '__main__':
    main()
