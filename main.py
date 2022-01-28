import time
import components.organisms as organism
import cairo
import random

creatures = []
plants = []

resolution = [1920, 1080]

def spawnCreatures(num_creatures):
    for i in range(num_creatures):
        creatures[i] = organism.Creature(0, 100, [] ,100, random.randint(-resolution[0]/2, resolution[0]/2), random.randint(-resolution[1]/2, resolution[1]/2))


while True:
    for i in creatures:
        try:
            i.tick()
        except:
            print("Creature tick failed")