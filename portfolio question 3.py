
import matplotlib.pyplot as plt
def simulate_bouncing_ball(v0, dt, g, h_surface, epsilon, total_time):
"""
Simulate a bouncing ball motion using a simple hard-sphere model.
v0 Initial velocity magnitude (m/s).
dt Time step size (s).
g Acceleration due to gravity (m/s^2).
h_surface Height of the surface (m).
k Coefficient of restitution (fraction of kinetic energy retained after each
bounce).
total_time : float
Total simulation time (s).
Returns:
t_values : list
List of time values.
y_values : list
List of height values.
"""
t_values = [0.0]
y_values = [h_surface]
v = v0
while t_values[-1] < total_time:
# Update time
t = t_values[-1] + dt
t_values.append(t)
# Update position
y = y_values[-1] + v * dt - 0.5 * g * dt**2
y_values.append(y)
# Check for collision with the surface
if y <= h_surface:
# Ball bounces
y_values[-1] = h_surface
v *= -epsilon # Reverse velocity and lose some energy
# Update velocity
v -= g * dt
# Check if the ball hits the ground and stops bouncing
if y_values[-1] < 0 and v <= 0:
break
return t_values, y_values
# Constants and parameters
g = 9.81 # Acceleration due to gravity (m/s^2)
h_surface = 0.0 # Height of the surface (m)
v0 = 10.0 # Initial velocity magnitude (m/s)
k = 0.9 # fraction of kinetic energy retained after each bounce
total_time = 19 # Total simulation time (s)
dt = 0.001 # Time step size (s)
# Simulate bouncing ball motion
t_values, y_values = simulate_bouncing_ball(v0, dt, g, h_surface, k, total_time)
# Plotting
plt.plot(t_values, y_values)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Bouncing Ball Simulation')
plt.grid(True)
# Set x-axis limits
plt.xlim(0, total_time)
plt.show()
Annotations
