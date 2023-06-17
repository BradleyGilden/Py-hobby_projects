from globals import VEL, WIDTH, HEIGHT
from pygame import K_LSHIFT, K_w, K_a, K_d, K_s, K_INSERT
from pygame import K_LEFT, K_RIGHT, K_DOWN, K_UP


def handle_keys_yellow(yellow, key_pressed):
    boost = 1
    if key_pressed[K_LSHIFT]:  # check for boost key
        boost = 3
    if key_pressed[K_w] and key_pressed[K_a]:  # UP/LEFT
        yellow.y -= VEL * boost
        if yellow.y < 0:
            yellow.y = 0
        yellow.x -= VEL * boost
        if yellow.x < 0:
            yellow.x = 0
        return
    elif key_pressed[K_w] and key_pressed[K_d]:  # UP/ RIGHT
        yellow.y -= VEL * boost
        if yellow.y < 0:
            yellow.y = 0
        yellow.x += VEL * boost
        if yellow.x > WIDTH/2 - 75:
            yellow.x = WIDTH/2 - 75
        return
    elif key_pressed[K_s] and key_pressed[K_a]:  # DOWN/LEFT
        yellow.y += VEL * boost
        if yellow.y > HEIGHT - 82:
            yellow.y = HEIGHT - 82
        yellow.x -= VEL * boost
        if yellow.x < 0:
            yellow.x = 0
        return
    elif key_pressed[K_s] and key_pressed[K_d]:  # DOWN/RIGHT
        yellow.y += VEL * boost
        if yellow.y > HEIGHT - 82:
            yellow.y = HEIGHT - 82
        yellow.x += VEL * boost
        if yellow.x > WIDTH/2 - 75:
            yellow.x = WIDTH/2 - 75
        return
    elif key_pressed[K_a]:  # LEFT
        yellow.x -= VEL * boost
        if yellow.x < 0:
            yellow.x = 0
        return
    elif key_pressed[K_w]:  # UP
        yellow.y -= VEL * boost
        if yellow.y < 0:
            yellow.y = 0
        return
    elif key_pressed[K_d]:  # RIGHT
        yellow.x += VEL * boost
        if yellow.x > WIDTH/2 - 75:
            yellow.x = WIDTH/2 - 75
        return
    elif key_pressed[K_s]:  # Down
        yellow.y += VEL * boost
        if yellow.y > HEIGHT - 82:
            yellow.y = HEIGHT - 82
        return


def handle_keys_red(red, key_pressed):
    boost = 1
    if key_pressed[K_INSERT]:  # check for boost key
        boost = 3
    if key_pressed[K_UP] and key_pressed[K_LEFT]:  # UP/LEFT
        red.x -= VEL * boost
        red.y -= VEL * boost
        if red.y < 0:
            red.y = 0
        if red.x < WIDTH/2 + 5:
            red.x = WIDTH/2 + 5
        return
    elif key_pressed[K_UP] and key_pressed[K_RIGHT]:  # UP/RIGHT
        red.y -= VEL * boost
        red.x += VEL * boost
        if red.x > WIDTH-70:
            red.x = WIDTH-70
        if red.y < 0:
            red.y = 0
        return
    elif key_pressed[K_DOWN] and key_pressed[K_LEFT]:  # DOWN/LEFT
        red.y += VEL * boost
        red.x -= VEL * boost
        if red.x < WIDTH/2 + 5:
            red.x = WIDTH/2 + 5
        if red.y > HEIGHT - 82:
            red.y = HEIGHT - 82
        return
    elif key_pressed[K_DOWN] and key_pressed[K_RIGHT]:  # DOWN/RIGHT
        red.y += VEL * boost
        red.x += VEL * boost
        if red.x > WIDTH-70:
            red.x = WIDTH-70
        if red.y > HEIGHT - 82:
            red.y = HEIGHT - 82
        return
    elif key_pressed[K_LEFT]:  # LEFT
        red.x -= VEL * boost
        if red.x < WIDTH/2 + 5:
            red.x = WIDTH/2 + 5
        return
    elif key_pressed[K_UP]:  # UP
        red.y -= VEL * boost
        if red.y < 0:
            red.y = 0
    elif key_pressed[K_RIGHT]:  # RIGHT
        red.x += VEL * boost
        if red.x > WIDTH-70:
            red.x = WIDTH-70
        return
    elif key_pressed[K_DOWN]:  # DOWN
        red.y += VEL * boost
        if red.y > HEIGHT - 82:
            red.y = HEIGHT - 82
        return
