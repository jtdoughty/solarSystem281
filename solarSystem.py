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
    Class for taking a list of particles (from the planetList class) and producing an n-body system in which the bodies interact.
    -------------------------------------
    Parameters:
    > Delta: Size of one time step, as float\n
    > Bodylist: A list of particles, as list (see planetList)\n
    > Iterations: The number of timesteps to be used, as int\n
    Note: All of these are to be supplied in the runSimulation.py file from the initialise.csv file
    """
    def __init__(self, Delta, BodyList, Iterations):
        self.delta = Delta
        self.bodyList = BodyList
        self.iterations = Iterations

    def getAccels(self):
        separationVec = np.array([0,0,0], dtype=float)
        separationMag = 0
        potEnergy = 0
        for subjectBody in self.bodyList:            
            subjectBody.acceleration=np.array([0,0,0], dtype=float)
            for objectBody in self.bodyList:
                if(objectBody != subjectBody):
                    separationVec = objectBody.position - subjectBody.position
                    separationMag = np.linalg.norm(separationVec)
                    subjectBody.acceleration += ((Particle.G * objectBody.mass)/(separationMag**3)) * separationVec
                    potEnergy += subjectBody.potentialEnergy(objectBody.mass,separationMag)
            subjectBody.potEnergyList.append(potEnergy)
            potEnergy = 0
            subjectBody.kinEnergyList.append(subjectBody.KineticEnergy())
            subjectBody.linMomList.append(subjectBody.LinMomentum())
            subjectBody.angMomList.append(subjectBody.AngMomentum())

    def groupUpdate(self):
        self.getAccels()
        for subjectBody in self.bodyList:
            subjectBody.update(self.delta)
            subjectBody.posx.append(subjectBody.position[0])#
            subjectBody.posy.append(subjectBody.position[1])#'''
            subjectBody.posz.append(subjectBody.position[2])#

    def groupUpdateIterative(self,numberOfIts):
        time = 0
        for i in range(numberOfIts):
            self.groupUpdate()
            Particle().timeList.append(time)
            time += self.delta
            
    def plot3dGraph(self):
        self.groupUpdateIterative(self.iterations)
        ax = plt.axes(projection='3d')
        #ax.set_aspect('equal')
        for body in self.bodyList:
            ax.plot3D(body.posx,body.posy,body.posz,':')
            ax.scatter3D(body.posx[-1],body.posy[-1],body.posz[-1],label=body.Name)#marks the end of the line with a dot, for ease of presentation
        plt.legend()
        plt.show()

    def plotXY(self):
        self.groupUpdateIterative(self.iterations)
        for body in self.bodyList:
            plt.plot(body.posx,body.posy,':')
            plt.scatter(body.posx[-1],body.posy[-1],label=body.Name)
        plt.legend()
        plt.show()

    def plotXZ(self):
        self.groupUpdateIterative(self.iterations)
        for body in self.bodyList:
            plt.plot(body.posx,body.posz,':')
            plt.scatter(body.posx[-1],body.posz[-1],label=body.Name)
        plt.legend()
        plt.show()
    
    def plotYZ(self):
        self.groupUpdateIterative(self.iterations)
        for body in self.bodyList:
            plt.plot(body.posy,body.posz,':')
            plt.scatter(body.posy[-1],body.posz[-1],label=body.Name)
        plt.legend()
        plt.show()

    def plotEnergies(self):
        self.groupUpdateIterative(self.iterations)
        totalKin = [0]*len(self.bodyList[0].kinEnergyList)
        totalPot = [0]*len(self.bodyList[0].potEnergyList)
        for body in self.bodyList:
            for i in range(len(totalKin)):
                totalKin[i] += body.kinEnergyList[i]
                totalPot[i] += body.potEnergyList[i]
        plt.plot(Particle().timeList,totalKin,label='Kinetic')
        #plt.plot(Particle().timeList,totalPot,label='Potential')
        plt.legend()
        plt.show()
