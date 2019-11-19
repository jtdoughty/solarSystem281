import numpy as np
from Particle import Particle
import math

earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(np.array([0,0,0]), np.array([0,10,0]), np.array([0,0,0]),'Earth', earthMass)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Particle.G*Earth.mass/(satPosition))
Satellite = Particle([satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 100.)
delta = 6
for i in range(2000):
    Earth.acceleration = []
    Satellite.acceleration # some code here 
    Earth.update(delta)
    Satellite.update(delta)