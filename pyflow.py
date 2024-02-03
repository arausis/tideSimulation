import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL
import numpy as np
DIR = "/media/ansel/Windows/Users/araus/Programming/WINTER2024/Modeling/heatmaps/eflowcropped.png"
DIR2= "/media/ansel/Windows/Users/araus/Programming/WINTER2024/Modeling/heatmaps/nflowcropped.png"
#DIR = "/media/ansel/Windows/Users/araus/Programming/WINTER2024/Modeling/heatmaps/test.png"
#DIR2= "/media/ansel/Windows/Users/araus/Programming/WINTER2024/Modeling/heatmaps/test.png"

def colorscale(r):
    return ((r * 0.012465) - 1.27)

def get_tides(d):
    flow1 = Image.open(DIR) 
    flow2 = Image.open(DIR2) 
      
    # Extracting pixel map: 
    pixels1 = flow1.load()
    pixels2 = flow2.load()
      
    # Extracting the width and height  
    # of the image: 
    width, height = flow1.size 
    width = int(width * d)
    height = int(height * d)

    retx = np.zeros((width, height))
    rety = np.zeros((width, height))

    for i in range(1,width): 
        for j in range(1,height): 
                r1, g1, b1 = flow1.getpixel((int(i / d), int(j / d))) 
                r2, g2, b2 = flow2.getpixel((int(i/ d), int(j / d)))
                if not (r1 ==255 and g1 == 0 and b1 == 0):
                    retx[i,j] = colorscale(r1)
                if not (r2 ==255 and g2 == 0 and b2 == 0):
                    rety[i,j] = colorscale(r2)
    return retx, rety

# use input_image.show() to see the image on the 
# output screen. 


def simulate_flow(start_x, start_y, u, v, num_steps, dt):
    trajectories = []
    x, y = start_x, start_y

    for _ in range(num_steps):
        trajectories.append((x, y))
        x_new = x + u[int(y), int(x)] * dt
        y_new = y + v[int(y), int(x)] * dt

        # Clip the coordinates to stay within the flow field boundaries
        x = np.clip(x_new, 0, width - 1)
        y = np.clip(y_new, 0, height - 1)

    return np.array(trajectories)

def plot_flow_field_with_trajectories(x, y, u, v, trajectories):
    plt.figure(figsize=(8, 10))
    plt.quiver(x, y, u, v, scale=50, color='blue', width=0.0005)
    plt.plot(trajectories[:, 0], trajectories[:, 1], 'ro-', markersize=0.1, label='Trajectory')
    plt.axis('off')
    plt.gca().set_aspect('equal')
    plt.tight_layout()
    plt.margins(x=0)
    plt.margins(y=0)
    plt.title('')
    plt.show()

def main():
    # The point : pixel ratio for performance
    definition = 1

    # Calculates x and y components of slope fields based in m/s
    xvecs, yvecs = get_tides(definition)

    # Makes sure that the map is oriented north
    xvecs = np.rot90(xvecs, 1)
    yvecs = np.rot90(yvecs, 1)

    # Doesn't do much of anything, good commonpractice
    global width, height;
    width, height = yvecs.shape 
    spacing = 1

    # Starting point for the trajectory
    start_x = 260
    start_y = 180

    # Simulation parameters
    num_steps = 10000
    dt = 3
    # Note: 1 pixel = 2049 m

    trajectories = simulate_flow(start_x, start_y, xvecs, yvecs , num_steps, dt)
    plot_flow_field_with_trajectories(range(0, height), range(0, width), xvecs, yvecs , trajectories)

if __name__ == "__main__":
    main()
