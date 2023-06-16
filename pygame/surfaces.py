from pygame import Rect, transform, image, display
from globals import WIDTH, HEIGHT, SS_H, SS_W
from os import path


# Initializing surfaces
BORDER = Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
Y_SPACESHIP_IMG = image.load(
    path.join('Assets', 'yellship.png'))
Y_SPACESHIP_IMG = transform.rotate(
    transform.scale(Y_SPACESHIP_IMG, (SS_H, SS_W)), 90)
R_SPACESHIP_IMG = image.load(
    path.join('Assets', 'redship.png'))
R_SPACESHIP_IMG = transform.rotate(
    transform.scale(R_SPACESHIP_IMG, (SS_H, SS_W)), 270)

M_WINDOW = display.set_mode((WIDTH, HEIGHT))

# Load and scale the background image
BACKGROUND = image.load(
    path.join('Assets', 'background4.jpg'))
BACKGROUND = transform.scale(BACKGROUND, (WIDTH, HEIGHT))
