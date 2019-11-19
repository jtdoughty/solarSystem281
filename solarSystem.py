import math
from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np

earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Earth', earthMass)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Earth.G*Earth.mass/(satPosition))
Satellite = Particle([satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 7.34e12)

class SolarSystem:
    """
    Simulates a 2 body system
    """
    def __init__(self,toast=1):
        #huh?
        self.toast=toast
    
    def __repr__(self):
        #where am i?
        return "Something{}".format(self.toast)

    earthx=[]
    earthy=[]
    satx=[]
    saty=[]

    delta = 6
    separationVec = np.array([0,0,0], dtype=float)
    separationMag = 0
    force = 0
    for i in range(200000):
        separationVec = Earth.position - Satellite.position
        separationMag = math.sqrt(separationVec[0]**2 + separationVec[1]**2 + separationVec[2]**2)
        force = (Particle.G * Satellite.mass * Earth.mass)/(separationMag**2)
        Earth.acceleration = ((-1 * force)/(separationMag * Earth.mass)) * separationVec
        Satellite.acceleration = ((force)/(separationMag * Satellite.mass)) * separationVec
        Earth.update(delta)
        Satellite.update(delta)
        #print('Time:',i,', Earth vel:',Earth.velocity,', Earth pos:',Earth.position)
        earthx.append(Earth.position[0])
        earthy.append(Earth.position[1])
        satx.append(Satellite.position[0])
        saty.append(Satellite.position[1])
    plt.plot(earthx,earthy,label='Earth')
    plt.plot(satx,saty,label='Sat')
    plt.legend()
    plt.show()
