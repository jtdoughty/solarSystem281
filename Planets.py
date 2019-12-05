import numpy as np
from Particle import Particle

class planetList:
    """
    Creates a set of 'planets' using the Particle class, using the data in the relevant .csv file (as named in the initialise.csv file)
    ------------------------------------
    Parameters:
    > FileName: Name of the data file to be loaded, as string.  The data in the file should be formatted with each row referring to one planet, and each column referring to that planet's name, mass (kg), initial x position, initial y position, initial z position (all in km), initial x velocity, initial y velocity, and initial z velocity (all in km.s^-1), respectively.
    """
    def __init__(self, FileName):
        self.filename=str(FileName)

    def makeList(self):
        planetData = np.loadtxt(self.filename,delimiter=',',usecols=(1,2,3,4,5,6,7))
        planetNames = np.loadtxt(self.filename,dtype=str,delimiter=',',usecols=(0))
        listOfPlanets=[]
        newPlanet=None
        newMass=0
        newX=0
        newY=0
        newZ=0
        newPos = []
        newVx=0
        newVy=0
        newVz=0
        newVel = []
        newName='Ball'
        for i in range(len(planetData)):
            newMass = planetData[i][0]
            newX = planetData[i][1]
            newY = planetData[i][2]
            newZ = planetData[i][3]
            newPos = [newX,newY,newZ]
            newVx = planetData[i][4]
            newVy = planetData[i][5]
            newVz = planetData[i][6]
            newVel = [newVx,newVy,newVz]
            newName = planetNames[i]
            newPlanet = Particle(newPos,newVel,[0,0,0],newName,newMass)
            listOfPlanets.append(newPlanet)
        return listOfPlanets
