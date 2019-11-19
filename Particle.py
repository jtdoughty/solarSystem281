import numpy as np

class Particle:
    """
    Class defining a massive particle with initial conditions, with an associated position and velocity updater.
    ###############################
    Parameters:
    > Position: Initial position in space, as float array [x,y,z] (default [0,0,0] at origin)
    > Velocity: Initial velocity, as float array [x,y,z] (default [0,0,0] immobile)
    > Acceleration: Initial acceleration, as float array [x,y,z] (default [0,-10,0] earth gravity)
    > Name: Name label of particle (default 'Ball')
    > Mass: Mass of particle (default 1.0) (unused)
    """
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0, G=6.67408E-11):
        self.position=np.array(Position, dtype=float)
        self.velocity=np.array(Velocity, dtype=float)
        self.acceleration=np.array(Acceleration, dtype=float)
        self.Name=Name
        self.mass=Mass
        self.G=G

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update(self, deltaT):
        """
        Updates position and velocity over a time increment, assuming constant acceleration
        #############################
        Parameters:
        > deltaT: Time increment (no default)
        """
        self.position += self.velocity*deltaT
        self.velocity += self.acceleration*deltaT