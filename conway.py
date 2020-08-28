import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

# grid of N*N random values
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N,N)

ugrid = grid.copy()

def grid_update(data):
    global grid 

    for i in range(N):
        for j in range(N):
        # 8 neighbor sum 
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    ugrid[i, j] = OFF
            else:
                if total == 3:
                    ugrid[i, j] = ON

    # data update
    mat.set_data(ugrid)
    grid = ugrid
    return [mat]

# basic animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, grid_update, interval=50,
                              save_count=50)
plt.show()