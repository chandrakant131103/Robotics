import numpy as np
import matplotlib.pyplot as plt


x_original = [40, 50, 50, 45, 40, 40]
y_original = [10, 10, 30, 40, 20, 10]

# Angle to rotate
theta_deg = 45
theta_rad = np.radians(theta_deg)

# --- 2. PERFORM ROTATION (Showing the Math) ---
x_rotated = []
y_rotated = []

# Loop through every point and calculate the new position
for i in range(len(x_original)):
    x = x_original[i]
    y = y_original[i]

    # Rotation Formula about Origin (0,0)
    # x' = x*cos(t) - y*sin(t)
    # y' = x*sin(t) + y*cos(t)
    new_x = x * np.cos(theta_rad) - y * np.sin(theta_rad)
    new_y = x * np.sin(theta_rad) + y * np.cos(theta_rad)

    x_rotated.append(new_x)
    y_rotated.append(new_y)

# --- 3. PLOTTING ---
plt.figure(figsize=(6, 6))

# Plot Original (Blue Dashed)
plt.plot(x_original, y_original, 'b--', label='Original', linewidth=2)

# Plot Rotated (Red Solid)
plt.plot(x_rotated, y_rotated, 'r-', label=f'Rotated {theta_deg}°', linewidth=2)

# Graph cosmetics
plt.plot(0, 0, 'ko', label='Origin (0,0)') # Mark the center
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--')
plt.legend()
plt.title(f"Absolute Rotation of Hut ({theta_deg}°)")
plt.axis('equal') # Important: keeps the shape from looking squashed
plt.show()

# --- 4. PRINT COORDINATES ---
print(f"--- Coordinates after {theta_deg}° Rotation ---")
labels = ["Bottom Left", "Bottom Right", "Top Right", "Peak", "Top Left"]
for i in range(5):
    print(f"{labels[i]}: ({x_rotated[i]:.2f}, {y_rotated[i]:.2f})")