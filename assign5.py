import matplotlib.pyplot as plt
import numpy as np

# 1. Create the base 'S' curve coordinates
t = np.linspace(-2, 2, 50)
x_base = t
y_base = np.sin(t) 

plt.figure(figsize=(7,7))

# 2. Rotation Loop (The Rotation Principle)
num_rotations = 60
for i in range(num_rotations):
    # Calculate the angle in radians (6 degrees each step)
    theta = np.radians(i * (360 / num_rotations))
    
    # APPLY THE ROTATION FORMULA
    x_rotated = x_base * np.cos(theta) - y_base * np.sin(theta)
    y_rotated = x_base * np.sin(theta) + y_base * np.cos(theta)
    
    # Plot the result
    plt.plot(x_rotated, y_rotated, color="deeppink", linewidth=0.8)

# Formatting the output
plt.axis('equal')
plt.axis('off')
plt.title("S-Curve Pattern using Rotation Principle")
plt.show()