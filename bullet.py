import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81  # gravity in m/s^2

# Initial conditions
v0 = 100.0  # initial velocity in m/s
theta = 45  # launch angle in degrees

# Convert angle to radians
theta = np.radians(theta)

# Time of flight
t_flight = 2*v0*np.sin(theta)/g

# Time array from 0 to t_flight
t = np.linspace(0, t_flight, num=500)

# Equations of motion
x = v0*t*np.cos(theta)
y = v0*t*np.sin(theta) - 0.5*g*t**2

# Plot
plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.title('Bullet Trajectory')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()
