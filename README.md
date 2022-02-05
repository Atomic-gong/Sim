### Sim

## Logic

# Sight
Organisms with eyes can see other organisms from up to 10 m away

# Energy
Energy is expended in relation to speed and size:
```py
self.energy -= self.size + (self.speed**2/4)
```

# Consumption
Spectrum of diet (soft to tough foods) affects how well each organism can eat that type of food

Organisms can eat or attempt to eat food that is within 3 m of them

# Genetic IDs, Fears and Predatory Behaviour
organisms can develop genetic fears or predatory instincts towards other creatures by comparing the similarity of a creature's genetic id to a saved one

genetic id format is as follows:
```
<3 digit hue value>||<soft-tough edible spectrum>||<soft-tough flesh spectrum>||<size>||
```

`hsv: 0-359`
`rgb: 0-255`

fears/prey stored as follows:
```py
self.fears = [[dna,intensity], [dna,intensity]]
```

intensity ranges from 0-10