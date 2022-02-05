import pygame
from pygame import draw
from math import hypot

def dist(pos, target):
    return abs(hypot(target[0] - pos[0], target[1] - pos[1]))

class manager():
    def __init__(self, display):
        self.display = display
    def refresh(self, organisms):
        for i in organisms:
            draw.circle(self.display, i.rgb_colour, i.position, i.size)
        pygame.display.flip()
