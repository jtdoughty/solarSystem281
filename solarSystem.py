import math
from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import matplotlib
from mpl_toolkits import mplot3d
from Planets import planetList

#https://ssd.jpl.nasa.gov/horizons.cgi#results

earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(np.array([0,0,0]), np.array([0,10,0]), np.array([0,0,0]),'Earth', earthMass)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Earth.G*Earth.mass/(satPosition))
Satellite = Particle([satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 50000000000.)
Steve = Particle([-1*satPosition,0,0], [0,-1*satVelocity,0], np.array([0,0,0]), "Steve", 50000000000.)
Hello = Particle([2*satPosition,0,0], [0,-0.7*satVelocity,0], np.array([0,0,0]), "Hello", 25000000000.)

listOfBodies=[Steve,Satellite,Earth,Hello]

planetset = planetList('planetData.csv')
listOfPlanets = planetset.makeList()

class GroupOfParticles:
    """
    Simulates a 2 body system
    """
    def __init__(self, Delta, BodyList, Iterations):
        self.delta = Delta
        self.bodyList = BodyList
        self.iterations = Iterations

    def getAccels(self):
        separationVec = np.array([0,0,0], dtype=float)
        separationMag = 0
        for subjectBody in self.bodyList:            
            subjectBody.acceleration=np.array([0,0,0], dtype=float)
            for objectBody in self.bodyList:
                if(objectBody != subjectBody):
                    separationVec = objectBody.position - subjectBody.position
                    separationMag = np.linalg.norm(separationVec)
                    subjectBody.acceleration += ((Particle.G * objectBody.mass)/(separationMag**3)) * separationVec

    def groupUpdate(self):
        self.getAccels()
        for subjectBody in self.bodyList:
            subjectBody.update(self.delta)
            subjectBody.posx.append(subjectBody.position[0])#
            subjectBody.posy.append(subjectBody.position[1])#'''
            subjectBody.posz.append(subjectBody.position[2])#

    def groupUpdateIterative(self,numberOfIts):
        for i in range(numberOfIts):
            self.groupUpdate()
            
    def plotGraph(self):
        self.groupUpdateIterative(self.iterations)
        ax = plt.axes(projection='3d')
        for body in self.bodyList:
            ax.plot3D(body.posx,body.posy,body.posz,':')
            ax.scatter3D(body.posx[-1],body.posy[-1],body.posz[-1],label=body.Name)
            #plt.plot(body.posx,body.posy,body.posz,label=body.Name)#'''
        plt.legend()
        plt.show()

SolarSystem = GroupOfParticles(6000,listOfPlanets,20000)
SolarSystem.plotGraph()
