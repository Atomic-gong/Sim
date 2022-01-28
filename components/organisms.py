import threading
#import stomach
#import heart
import time

class Creature():

    def __init__(self, meat_tendency = 0, plant_tendency = 0 ,components = [], blood = 100, x = 0, y = 0):
        self.meat_tendency = meat_tendency
        self.plant_tendency = plant_tendency
        self.components = components
        self.startingComponents = components
        self.blood = blood
        self.bloodMinimum = blood/2
        self.diseases = []
        self.energy = 100
        self.numIntestines = 1

        self.x = x
        self.y = y

        self.unprocessedFood = ["this should fail", [12,0]] # contains numbers dictating the energy gained from each piece of unprocessed food and the time it entered the stomach

        #constants that may become variable
        self.bloodPressure = 1
    
    def buildSelf(self):
        pass

    def calcInternals(self):
        numMissingInternals = len(self.startingComponents) - len(self.components)
        self.blood -= self.bloodPressure * numMissingInternals

        for i in range(self.numIntestines):
            foodToRemove = []
            for i in self.unprocessedFood:
                try:
                    if i[1] >= 4:
                        foodToRemove.append(i)
                        self.energy += i[0]
                    else:
                        i[1] += 1
                except:
                    print(f"[{time.ctime()} | {self}]: Food digestion check failed")
        pass

    def checkComponents(self):
        for i in self.components:
            try:
                testVar = i.isAlive
            except:
                self.components.remove(i)

    def tick(self):
        print(f"[{time.ctime()} | {self}]: Start tick")

        self.calcInternals()

        print(f"[{time.ctime()} | {self}]: End tick")
        pass