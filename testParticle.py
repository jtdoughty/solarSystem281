from Particle import Particle 
import matplotlib.pyplot as plt 
import math
import numpy as np


Ball = Particle(np.array([0,100,0]), np.array([20,50,0]), np.array([0,-10,0]),'Ball', 500.)
print(Ball)

time = 0
deltaT = 1e-3 

x = []
y = [] 

while (Ball.position[1]>0):
    time += deltaT
    Ball.update(deltaT)
    #print("Time: %6.3f, %s"%(time,Ball))
    x.append(time)
    y.append(Ball.position[1])


#print(data)

print(max(x))
print(max(y))
print(len(x))
corners = [0,math.trunc(max(x))+1,0, math.trunc(max(y))+10]
plt.axis(corners)
plt.plot(x,y,'r-',label='trajectory')
plt.xlabel('time (s)')
plt.ylabel('y-position (m)')
plt.legend()
plt.show() 
