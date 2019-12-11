import numpy as np
from Planets import planetList
from Particle import Particle
from solarSystem import GroupOfParticles

listname = np.loadtxt('initialise.csv',dtype=str,delimiter=',',usecols=(0))
Delta = np.loadtxt('initialise.csv',delimiter=',',usecols=(1))
Iterations = np.loadtxt('initialise.csv',dtype=int,delimiter=',',usecols=(2))
methodNo = np.loadtxt('initialise.csv',delimiter=',',usecols=(3))

planetset = planetList(listname)
listOfPlanets = planetset.makeList()
Particle().setMethod(methodNo)
SolarSystem = GroupOfParticles(Delta,listOfPlanets,Iterations)
SolarSystem.groupUpdateIterative()
#SolarSystem.plot3dGraph()
SolarSystem.plotEnergies()
SolarSystem.plotVirial()
#SolarSystem.plotLinMomentum()
#SolarSystem.plotAngMomentum()
