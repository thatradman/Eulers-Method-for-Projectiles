

import numpy as np
import matplotlib.pyplot as plt
# Constants and parameters
g = 9.81 # Acceleration due to gravity (m/s^2)
total_time = 5 # Total simulation time (s)
dt = 0.01 # Time step size (s)
v0 = 10 # Initial velocity (m/s)
theta = 60 # Launch angle in degrees
def euler_projectile_motion(v0, theta, dt, g, total_time):
"""
Simulate projectile motion using Euler's method.
Arguments:
v0 : float
Initial velocity magnitude (m/s).
theta : float
Launch angle in degrees.
dt : float
Time step size (s).
g : float
Acceleration due to gravity (m/s^2).
total_time : float
Total simulation time (s).
Returns:
x_values : list
List of x-coordinates of the projectile trajectory.
y_values : list
List of y-coordinates of the projectile trajectory.
"""
# Convert angle from degrees to radians
theta = np.radians(theta)
# Calculate initial velocity components
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
# Initialize position
x = 0.0
y = 0.0
# Lists to store trajectory points
x_values = [x]
y_values = [y]
# Simulation loop
while y >= 0.0:
# Update position using Euler's method
x += vx * dt
y += vy * dt - 0.5 * g * dt**2
# Update velocity components
vy -= g * dt
# Append new position to lists
x_values.append(x)
y_values.append(y)
return x_values, y_values
# Analytical Method
def analytical_projectile_motion(v0, theta, dt, g, total_time):
"""Calculate projectile motion analytically.
v0 Initial velocity magnitude (m/s).
theta Launch angle in degrees.
dt Time step size (s).
g : float
Acceleration due to gravity (m/s^2).
total_time : float
Total simulation time (s).
Returns:
x_values Array of x-coordinates of the projectile trajectory.
y_values Array of y-coordinates of the projectile trajectory."""
# Convert angle from degrees to radians
theta = np.radians(theta)
# Calculate time array
t = np.arange(0, total_time, dt)
# Calculate acceleration in the y direction
a_y1 = -g
# Calculate x and y positions
x = v0 * t * np.cos(theta)
y = t * v0 * np.sin(theta) + (1/2) * a_y1 * t**2
return x, y
# Create time array
t = np.arange(0, total_time, dt)
# Analytical method trajectory
x_a, y_a = analytical_projectile_motion(v0, theta, dt, g, total_time)
# Determine when the height becomes negative for the analytical method
whenneg = np.argmax(y_a < 0)
# Slice the arrays to include only positive heights
x_a = x_a[:whenneg]
y_a = y_a[:whenneg]
# Euler's method trajectory
x_e, y_e = euler_projectile_motion(v0, theta, dt, g, total_time)
# Create a larger figure
plt.figure(figsize=(10, 6))
# Plot trajectories
plt.plot(x_a, y_a, label='Analytical Method')
plt.plot(x_e, y_e, label="Euler's Method")
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion Comparison')
plt.legend()
plt.grid(True)
plt.show()
Annotations
