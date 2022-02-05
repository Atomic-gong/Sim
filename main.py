import pygame
import difflib
import colorsys
import random
import gamefuncs
import threading
from gamefuncs import dist

pygame.init()

screen_size = (1920,1080)
num_chunks = 8
chunks = []
for i in range(num_chunks):
    chunks.append([])
print(chunks)

ready_chunks = 0

pellets = []

display = pygame.display.set_mode(screen_size)

scr_manager = gamefuncs.manager(display)

class pellet():
    global screen_size, pellets
    def __init__(self):
        pellets.append(self)
        self.age = 0
        self.lifetime = random.randint(10,(screen_size[1]/3)*2)
        self.position = (random.randint(0,screen_size[0]), 0)
        self.rgb_colour = (0.2,1,0.2)
        self.size = 2
    
    def tick(self):
        self.position = (self.position[0]-1, self.position[1])
        self.age += 1
        if self.age > self.lifetime:
            pellets.remove(self)

class organism():
    global num_chunks, chunks, screen_size, pellets
    def __init__(self, position, dna = "137||050||050||5||", fears = [], prey = [], speed = 0):
        self.DNA = dna

        self.fears = fears
        self.prey = prey

        self.edible_toughness = int(self.DNA[6:8])
        self.flesh_toughness = int(self.DNA[11:13])

        self.hsv_colour = (float(self.DNA[:3]), 1, 1)
        self.rgb_colour = (colorsys.hsv_to_rgb(self.hsv_colour[0], self.hsv_colour[1], self.hsv_colour[2]))

        self.speed = speed
        self.size = int(self.DNA[15:len(self.DNA)-2])

        self.position = position
        x_boundaries = screen_size[0] / (num_chunks/2)
        y_boundaries = screen_size[1] / 2
        self.chunk = int(self.position[0]/x_boundaries) * int(self.position[1]/y_boundaries)
        chunks[self.chunk].append(self)

        self.age = 0

        self.energy = 10
    
    def randomise(self):
        self.hsv_colour = (str(random.randint(0,100)/100), str(1), str(1))
        self.rgb_colour = (colorsys.hsv_to_rgb(float(self.hsv_colour[0]), float(self.hsv_colour[1]), float(self.hsv_colour[2]))) * 255

        self.edible_toughness = str(random.randint(0,100))
        self.flesh_toughness = str(random.randint(0,100))

        self.speed = random.randint(0,3)
        self.size = random.randint(3,8)
        
        self.hsv_colour[0] = ("0"*(3-len(self.hsv_colour[0]))) + self.hsv_colour[0]
        self.edible_toughness = ("0"*(3-len(self.edible_toughness))) + self.edible_toughness
        self.flesh_toughness = ("0"*(3-len(self.toughness))) + self.flesh_toughness

        self.DNA = f"{self.hsv_colour[0]}||{self.edible_toughness}||{self.flesh_toughness}||{self.size}"

        self.edible_toughness = int(self.edible_toughness)
        self.flesh_toughness = int(self.flesh_toughness)

        self.update_chunk()

    def update_chunk(self):
        old_chunk = self.chunk
        x_boundaries = screen_size[0] / (num_chunks/2)
        y_boundaries = screen_size[1] / 2
        self.chunk = int(self.position[0]/x_boundaries) * int(self.position[1]/y_boundaries)
        if not self.chunk == old_chunk:
            chunks[old_chunk].remove(self)
            chunks[self.chunk].append(self)

    def tick(self):
        for i in pellets:
            if dist(self.position, i.position) < self.size+5:
                self.energy += 1
                pellets.remove(i)

        for i in chunks[self.chunk]:
            if dist(self.position, i.position) < self.size+5:
                self.energy += i.energy
                chunks[self.chunk].remove(i)

        self.energy -= self.size + (self.speed**2/4)
        if self.energy < 1:
            chunks[self.chunk].remove(self)

def spawn_organisms(count, isRandom = False):
    templist = []
    for i in range(count):
        templist.append(organism((random.randint(0,screen_size[0]), random.randint(0,screen_size[1]))))
    if isRandom:
        for i in templist:
            i.randomise()
    templist = None

def spawn_pellets(count):
    for i in range(count):
        pellets.append(pellet())

def update_pellets():
    for i in pellets:
        i.tick()

def update_organisms(chunk):
    global chunks, scr_manager, ready_chunks
    while True:
        for i in chunks[chunk]:
            i.tick()
        scr_manager.refresh(chunks[chunk])
        ready_chunks += 1
        

def init_threads(num):
    for i in range(num):
        threading.Thread(target=update_organisms, args=(i,)).start()

spawn_organisms(200)
spawn_pellets(300)
init_threads(num_chunks)

while True:
    if ready_chunks == num_chunks + 1:
        display.fill((0,0,0))
        ready_chunks = 0
    update_pellets()
    spawn_pellets(random.randint(0,5))
    scr_manager.refresh(pellets)
    ready_chunks += 1
    #print("tick")