from pygame import KEYDOWN, KEYUP, K_LALT, K_RCTRL, Rect, event
from globals import B_SPEED, Y_HIT, R_HIT


def bullets_setup(Event, yellow, red, y_bullet, r_bullet, bullet):
    r_up = True
    y_up = True
    if Event.type == KEYDOWN:
        if Event.key == K_LALT and y_up is True:
            bullet = Rect(yellow.x + yellow.width,
                          yellow.y + yellow.height//2 - 2, 10, 5)
            y_bullet.append(bullet)
            y_up = False
            print("tapped")
        elif Event.key == K_RCTRL and r_up is True:
            bullet = Rect(red.x, red.y + red.height//2 - 2, 10, 5)
            r_bullet.append(bullet)
            r_up = False

    elif Event.type == KEYUP:
        if Event.key == K_LALT:
            y_up = True
        elif Event.key == K_RCTRL:
            r_up = True


def handle_bullets(y_bullet, r_bullet, yellow, red):
    for bullet in y_bullet:
        bullet.x += B_SPEED
        if red.colliderect(bullet):
            event.post(event.Event(R_HIT))
            y_bullet.remove(bullet)

    for bullet in r_bullet:
        bullet.x -= B_SPEED
        if yellow.colliderect(bullet):
            event.post(event.Event(Y_HIT))
            r_bullet.remove(bullet)
