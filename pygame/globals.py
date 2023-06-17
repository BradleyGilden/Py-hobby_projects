from pygame import USEREVENT


WIDTH, HEIGHT = 1280, 720  # frame dimensions
SS_H, SS_W = 85, 70  # space ship width and height
VEL = 5  # velocity of ship

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CENTER = (0, 0)
FPS = 60

B_SPEED = 10
MAX_BULLETS = 10000

# COLLISION EVENTS
Y_HIT = USEREVENT + 1
R_HIT = USEREVENT + 2
