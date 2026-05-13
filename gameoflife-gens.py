import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import argparse

'''
This is an implementation of Conway's Game of Life. The grid is visualized using a 4-phase color scheme:
- Phase 0: Current generation cells are shown in yellow. This is the initial state of the grid. (This uses a 20 t0 80 ratio of ON to OFF cells.)
- Phase 1: Current generation cells are shown in red. This is the second phase where we highlight the current generation.
- Phase 2: Both current generation (red) and next generation (yellow) cells are shown. This phase allows us to see the transition from the current generation to the next generation.
- Phase 3: The next generation becomes the current generation, and only the new current generation cells are shown in yellow. This phase finalizes the transition to the next generation.
'''
ON = 1
OFF = 0

phase = 0
current_gen = None
next_gen = None

def randomGrid(N):
    return np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

def get_next_generation(grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] 
                         + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] 
                         + grid[(i-1)%N, (j+1)%N] +grid[(i+1)%N, (j-1)%N] 
                         + grid[(i+1)%N, (j+1)%N]))
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    return newGrid



def update(frameNum, img, N):
    global phase, current_gen, next_gen
    
    display_grid = np.zeros((N, N))
    
    if phase == 0:
        display_grid[current_gen == ON] = 1 
    elif phase == 1:
        display_grid[current_gen == ON] = 2
    elif phase == 2:
        next_gen = get_next_generation(current_gen, N)
        display_grid[current_gen == ON] = 2
        display_grid[next_gen == ON] = 1
    elif phase == 3:
        current_gen = next_gen.copy()
        display_grid[current_gen == ON] = 1
    
    img.set_data(display_grid)
    phase = (phase + 1) % 4
    return img,

def main():
    global current_gen
    
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life with 4-phase color visualization.")
    parser.add_argument('--grid-size', dest='N', type=int, default=10)
    parser.add_argument('--interval', dest='interval', type=int, default=1000)
    args = parser.parse_args()
    
    N = args.N
    interval = args.interval
    
    current_gen = randomGrid(N)
    
    fig, ax = plt.subplots()
    cmap = ListedColormap(['black', 'yellow', 'red'])
    
    img = ax.imshow(current_gen, interpolation='nearest', cmap=cmap, vmin=0, vmax=2)
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, N), interval=interval, cache_frame_data=False)
    plt.show()

if __name__ == '__main__':
    main()