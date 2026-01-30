import matplotlib.pyplot as plt
import numpy as np

def plot_robotic_arm():
    L1 = 110.00 
    L2 = 140.00 
    lx = np.array([0.0, 0.0, -140.0])
    ly = np.array([0.0, L1, L1]) 

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('white')


    ax.plot([lx[0], lx[1]], [ly[0], ly[1]], color='blue', linewidth=2, label=f'L1 = {L1:.2f} mm')
    ax.plot([lx[1], lx[2]], [ly[1], ly[2]], color='red', linewidth=2, label=f'L2 = {L2:.2f} mm')


    # Joint 1 
    ax.plot(lx[0], ly[0], 'bo', markersize=8, label=f'Joint 1: ({lx[0]:.1f}, {ly[0]:.1f})')
    
    # Joint 2 
    ax.plot(lx[1], ly[1], 'ro', markersize=8, label=f'Joint 2: ({lx[1]:.1f}, {ly[1]:.1f})')
    
    # Joint 3 
    ax.plot(lx[2], ly[2], 'go', markersize=8, label=f'Joint 3: ({lx[2]:.1f}, {ly[2]:.1f})')

    
    ax.set_aspect('equal')
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    
    limit = 200
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    ax.set_title("2D Robotic Arm Layout")
    ax.legend(loc='upper right', fontsize='small')

    plt.show()

if __name__ == "__main__":
    plot_robotic_arm()