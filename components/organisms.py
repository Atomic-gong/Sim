import threading
import creature_components.stomach
import creature_components.heart

class Creature():

    def __init__(self, meat_tendency = 0, plant_tendency = 0 ,components = [], bloodTotal = 100, x = 0, y = 0):
        self.meat_tendency = meat_tendency
        self.plant_tendency = plant_tendency
        self.components = components
        self.bloodTotal = bloodTotal
        self.bloodMinimum = bloodTotal/2
        self.diseases = []
        self.energy = 100

        self.x = x
        self.y = y
    
    def tick(self):
        pass