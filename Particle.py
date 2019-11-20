import numpy as np

class Particle:
    """
    Class defining a massive particle with initial conditions, with an associated position and velocity updater.
    -------------------------------------
    Parameters:
    > Position: Initial position in space, as float array [x,y,z] (default [0,0,0] at origin)
    > Velocity: Initial velocity, as float array [x,y,z] (default [0,0,0] immobile)
    > Acceleration: Initial acceleration, as float array [x,y,z] (default [0,-10,0] earth gravity)
    > Name: Name label of particle (default 'Ball')
    > Mass: Mass of particle (default 1.0) (unused)
    """
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), name='Ball', Mass=1.0, method=1):
        self.position=np.array(Position, dtype=float)
        self.velocity=np.array(Velocity, dtype=float)
        self.acceleration=np.array(Acceleration, dtype=float)
        self.name=str(name)
        self.mass=float(Mass)
        self.setMethod(method)

    G=6.67408E-11

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.name,self.mass,self.position, self.velocity,self.acceleration)

    def setMethod(self, method):
        if method == 1:
            self.update = self.euler
        elif method == 2:
            self.update = self.eulerCromer
        #elif method == 3:
        #    self.update = self.crect
        else:
            raise ValueError(
                "Unrecognised integration method. Method must be 1 \n(trapezoid), 2 (left rectangle), or 3 (centre rectangle)."
            )

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
