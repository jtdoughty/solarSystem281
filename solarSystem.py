import math
from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import matplotlib
from mpl_toolkits import mplot3d
from Planets import planetList

#https://ssd.jpl.nasa.gov/horizons.cgi#results

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
