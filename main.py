import time
import components.organisms as organism
import random
import pygame

pygame.init()

creatures = []
plants = []

resolution = (1920, 1080)

screen = pygame.display.set_mode((resolution))

def spawnCreatures(num_creatures):
    for i in range(num_creatures):
        creatures.append(organism.Creature(0, 100, [] ,100, random.randint(0, resolution[0]), random.randint(0,resolution[1])))

def organism_updates():
    for i in creatures:
        try:
            i.tick()
        except:
            print("Creature tick failed")

def render_updates():
    screen.fill((0,0,0))
    
    for i in creatures:
        try:
            pygame.draw.circle(screen, (255,255,255), (i.x, i.y), 3)
        except:
            print("Creature draw failed")

    pygame.display.flip()
    pass


spawnCreatures(12)

while True:
    organism_updates()
    render_updates()