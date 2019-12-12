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
        """
        Calculates the acceleration experienced by each particle, due to each other particle present in the system.
        """
        separationVec = np.array([0,0,0], dtype=float)#Used to represent the vector separation of the two planets concerned in the system.  This points towards the second body, since this is used to calculate an acceleration under a presumed attractive force on the first body
        separationMag = 0#Used to represent the magnitude of the separation vector, separationVec
        potEnergy = 0#Used to represent the potential energy from the force attracting a given mass to the others
        for subjectBody in self.bodyList:#subjectBody represents the body being attracted
            subjectBody.accZero()
            for objectBody in self.bodyList:#objectBody represents the body doing the attracting
                if(objectBody != subjectBody):#Since a body can't attract itself!
                    separationVec = objectBody.position - subjectBody.position
                    separationMag = np.linalg.norm(separationVec)
                    subjectBody.accIncr(((Particle.G * objectBody.mass)/(separationMag**3)) * separationVec)
                    potEnergy += subjectBody.potentialEnergy(objectBody.mass,separationMag)/2
            subjectBody.potEnergyList.append(potEnergy)
            potEnergy = 0
            subjectBody.kinEnergyList.append(subjectBody.KineticEnergy())
            subjectBody.linMomList.append(subjectBody.LinMomentum())
            subjectBody.angMomList.append(subjectBody.AngMomentum())

    def groupUpdate(self):
        """
        Updates the positions of the bodies of the systems, by calling the update method of the Particle class
        """
        self.getAccels()
        for subjectBody in self.bodyList:
            subjectBody.update(self.delta)
            subjectBody.posx.append(subjectBody.position[0])#Appends the position components to a list stored in the Particle class
            subjectBody.posy.append(subjectBody.position[1])
            subjectBody.posz.append(subjectBody.position[2])

    def groupUpdateIterative(self):
        """
        Calls the groupUpdate method repeatedly across the number of iterations given in the initialise.csv file
        """
        time = 0
        self.getAccels()
        for i in range(self.iterations):
            self.groupUpdate()
            Particle().timeList.append(time)#This will create a list of time points, which will be as long as the lists of kinetic energies and momenta
            time += self.delta
            
    def plot3dGraph(self):
        """
        Creates a 3-dimensional plot of the positions of all bodies in this system.
        """
        ax = plt.axes(projection='3d')
        maxList=[]#Lists the largest values (in terms of magnitude) from the x, y and z components from each planet
        for body in self.bodyList:
            ax.plot3D(body.posx,body.posy,body.posz,':')
            ax.scatter3D(body.posx[-1],body.posy[-1],body.posz[-1],label=body.Name)#marks the end of the line with a dot, for ease of presentation
            maxList.append(max(np.absolute(body.posx)))
            maxList.append(max(np.absolute(body.posy)))
            maxList.append(max(np.absolute(body.posz)))
        maxValue=max(maxList)#Finds the largest magnitude value from all position points of all planets used, to better scale the axes
        ax.set_xlabel('km')
        ax.set_ylabel('km')
        ax.set_zlabel('km')
        plt.legend()
        ax.set_xlim3d(-maxValue,maxValue)#Set the axes to the same limits, determined using maxValue
        ax.set_ylim3d(-maxValue,maxValue)
        ax.set_zlim3d(-maxValue,maxValue)
        plt.show()

    def plotXY(self):
        """
        Creates a 2-dimensional plot of all bodies in the system in the X-Y plane
        """
        for body in self.bodyList:
            plt.plot(body.posx,body.posy,':')
            plt.scatter(body.posx[-1],body.posy[-1],label=body.Name)
        plt.legend()
        plt.show()

    def plotXZ(self):
        """
        Creates a 2-dimensional plot of all bodies in the system in the X-Z plane
        """
        for body in self.bodyList:
            plt.plot(body.posx,body.posz,':')
            plt.scatter(body.posx[-1],body.posz[-1],label=body.Name)
        plt.legend()
        plt.show()
    
    def plotYZ(self):
        """
        Creates a 2-dimensional plot of all bodies in the system in the Y-Z plane
        """
        for body in self.bodyList:
            plt.plot(body.posy,body.posz,':')
            plt.scatter(body.posy[-1],body.posz[-1],label=body.Name)
        plt.legend()
        plt.show()

    def plotEnergies(self):
        """
        Plots the kinetic energy, potential energy, and total energy for the set of particles.
        """
        totalKin = [0]*len(self.bodyList[0].kinEnergyList)#Total kinetic energy of the system, T
        totalPot = [0]*len(self.bodyList[0].potEnergyList)#Total potential energy of the system, U
        totalEnr = deepcopy(totalKin)#Total energy of the system, T+U
        for body in self.bodyList:
            for i in range(len(totalKin)):
                totalKin[i] += body.kinEnergyList[i]
                totalPot[i] += body.potEnergyList[i]
                totalEnr[i] = totalKin[i]+totalPot[i]
        plt.plot(Particle().timeList,totalKin,label='Kinetic')
        plt.plot(Particle().timeList,totalPot,label='Potential')
        plt.plot(Particle().timeList,totalEnr,label='Total')
        plt.legend()
        plt.show()

    def plotVirial(self):
        """
        Plots the value 2T-U, twice the total kinetic energy minus the total potential energy, for the system of bodies
        """
        listVirial = [0]*len(self.bodyList[0].kinEnergyList)
        for body in self.bodyList:
            for i in range(len(self.bodyList[0].kinEnergyList)):
                listVirial[i] += (2*body.kinEnergyList[i]+body.potEnergyList[i])
        plt.plot(Particle().timeList,listVirial,label='$2T-U$')
        plt.legend()
        plt.show()

    def plotLinMomentum(self):
        """
        Plots the total linear momentum of the system, as well as the total X, Y and Z components of the momentum.
        """
        totalLMom=[0]*len(self.bodyList[0].linMomList)#The total linear momentum
        totalLMomX=deepcopy(totalLMom)#The total linear momentum in the X direction
        totalLMomY=deepcopy(totalLMom)#The total linear momentum in the Y direction
        totalLMomZ=deepcopy(totalLMom)#The total linear momentum in the Z direction
        for body in self.bodyList:
            for i in range(len(body.linMomList)):
                totalLMom[i]+=body.linMomList[i]
                totalLMomX[i]+=body.linMomList[i][0]
                totalLMomY[i]+=body.linMomList[i][1]
                totalLMomZ[i]+=body.linMomList[i][2]
        for i in range(len(totalLMom)):
            totalLMom[i]=np.linalg.norm(totalLMom[i])
        plt.plot(Particle().timeList,totalLMom,label='Total Linear Momentum')
        plt.plot(Particle().timeList,totalLMomX,label='Total Linear Momentum in x')
        plt.plot(Particle().timeList,totalLMomY,label='Total Linear Momentum in y')
        plt.plot(Particle().timeList,totalLMomZ,label='Total Linear Momentum in z')
        plt.xlabel('Time /s')
        plt.ylabel('Momentum /$\mathrm{kg}\,\mathrm{km}\,\mathrm{s}^{-1}$')
        plt.legend()
        plt.show()

    def plotAngMomentum(self):
        """
        Plots the total angular momentum of the system, as well as the total X, Y and Z components of the momentum.
        """
        totalAMom=[0]*len(self.bodyList[0].angMomList)#The total linear momentum
        totalAMomX=deepcopy(totalAMom)#The total linear momentum in the X direction
        totalAMomY=deepcopy(totalAMom)#The total linear momentum in the Y direction
        totalAMomZ=deepcopy(totalAMom)#The total linear momentum in the Z direction
        for body in self.bodyList:
            for i in range(len(body.angMomList)):
                totalAMom[i]+=body.angMomList[i]
                totalAMomX[i]+=body.angMomList[i][0]
                totalAMomY[i]+=body.angMomList[i][1]
                totalAMomZ[i]+=body.angMomList[i][2]
        for i in range(len(totalAMom)):
            totalAMom[i]=np.linalg.norm(body.angMomList[i])
        plt.plot(Particle().timeList,totalAMom,label='Total Angular Momentum')
        plt.plot(Particle().timeList,totalAMomX,label='Total Angular Momentum in x')
        plt.plot(Particle().timeList,totalAMomY,label='Total Angular Momentum in y')
        plt.plot(Particle().timeList,totalAMomZ,label='Total Angular Momentum in z')
        plt.xlabel('Time /s')
        plt.ylabel('Momentum /$\mathrm{kg}\,\mathrm{km}\,\mathrm{s}^{-1}$')
        plt.legend()
        plt.show()
