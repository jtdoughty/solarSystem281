import numpy as np

class Particle:
    """
    Class defining a massive particle with initial conditions, with an associated position and velocity updater.
    -------------------------------------
    Parameters:
    > Position: Initial position in space, as float array [x,y,z] (default [0,0,0] at origin)\n
    > Velocity: Initial velocity, as float array [x,y,z] (default [0,0,0] immobile)\n
    > Acceleration: Initial acceleration, as float array [x,y,z] (default [0,0,0] not accelerating)\n
    > Name: Name label of particle (default 'Ball')\n
    > Mass: Mass of particle (default 1.0)\n
    -------------------------------------
    Methods:
    > setMethod(method): Changes the update method\n
    > setName(name): Changes the name\n
    > setPosition(position): Changes the position
    """
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), name='Ball', Mass=1.0):
        self.position=np.array(Position, dtype=float)
        self.velocity=np.array(Velocity, dtype=float)
        self.acceleration=np.array(Acceleration, dtype=float)
        self.Name=str(name)
        self.mass=float(Mass)
        self.setMethod(2)
        self.posx=[]#these three lists are use to store the position data at a given time step
        self.posy=[]
        self.posz=[]
        self.kinEnergyList=[]#these four lists store the kinetic energy, potential energy, linear momentum, and angular momentum at a given time step
        self.potEnergyList=[]
        self.linMomList=[]
        self.angMomList=[]

    G=6.67408E-20#in km^3.kg^-1.s^-2
    timeList=[]#this is a global list of the time steps, and is the same length as the other seven lists for each particle

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def setMethod(self, method):
        if method == 1:
            self.update = self.euler
        elif method == 2:
            self.update = self.eulerCromer
        #elif method == 3:
        #    self.update = self.crect
        else:
            raise ValueError(
                "Unrecognised integration method. Method must be 1 \n(Euler) or 2 (Euler-Cromer)."
            )
    
    def setPosition(self, Position):
        self.position = np.array(Position, dtype=float)

    def setName(self,Name):
        self.Name = str(Name)

    def euler(self, deltaT):
        """
        Updates position and velocity over a time increment, assuming constant acceleration, updating position using velocity before incrementing.
        --------------------------------
        Parameters:
        > deltaT: Time increment (no default)
        """
        self.position += self.velocity*deltaT
        self.velocity += self.acceleration*deltaT

    def eulerCromer(self, deltaT):
        """
        Updates position and velocity over a time increment, assuming constant acceleration, updating position using velocity after incrementing.
        --------------------------------
        Parameters:
        > deltaT: Time increment (no default)
        """
        self.velocity += self.acceleration*deltaT
        self.position += self.velocity*deltaT

    def KineticEnergy(self):
        return(0.5 * self.mass * np.dot(self.velocity,self.velocity))
    
    def potentialEnergy(self,obmass,separation):
        return((self.G*self.mass*obmass)/(separation**2))
    
    def LinMomentum(self):
        return(self.mass * self.velocity)

    def AngMomentum(self):
        linMomentum = self.LinMomentum()
        return(np.cross(self.position, linMomentum))


