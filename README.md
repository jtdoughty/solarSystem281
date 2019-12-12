# solarSystem281
A project designed to model an n-body system, written in Python.
Required modules are math, numpy, matplotlib.pyplot, deepcopy, mpl_toolkits.mplot3d
To generate a simulation, run the 'runSimulation.py' file.  The planetary data is to be stored in a .csv file, formatted as follows:
name, mass, x-position, y-position, z-position, x-velocity, y-velocity, z-velocity, x-acceleration, y-acceleration, z-acceleration
All masses should be in kg, positions in km, velocity in km/s, acceleration in km/s^2.
To edit the parameters of the simulation, edit the file 'initialise.csv'.  This is formatted as follows:
planetDataFile, timestep, iterations, method
planetDataFile: the name of the .csv file containing the planetary data
timestep: the amount of time between iterations (should be a number)
iterations: the number of timeteps desired (should be a number)
method: the numerical integration method to be used.  Allowed values are 1 (Euler), 2 (Euler-Cromer), 3 (Verlet)
