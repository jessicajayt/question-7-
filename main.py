import numpy as np 
import matplotlib.pyplot as plt 

f = open('values.txt', 'r')
f.readline() 

#creating empty lists
radius = []
velocity = []
radius1 = []
velocity1 = []
mass = []
predictedVelocity = []
G = 6.67*(10**-11)

for line in f:
  radius.append(float(line.split('\t')[0]))
  velocity.append(float(line.split('\t')[1]))
  radius1.append((line.split('\t')[2]))
  velocity1.append(float(line.split('\t')[4]))
  mass.append(float(line.split('\t')[4]))
  predictedVelocity.append((float(G))*(float(line.split('\t')[4]))/(float(line.split('\t')[0]))**(0.5))

x = np.array(radius)
y = np.array(velocity)
z = np.array(predictedVelocity)

plt.plot(x,y)
plt.plot(x,z)
plt.ylabel('Velocity(km/h)')
plt.xlabel('Radius (kpc)')
plt.show()