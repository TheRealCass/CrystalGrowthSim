import random
import matplotlib.pyplot as plt

# Constants
GRID_SIZE = 100  # size of the grid
NUM_PARTICLES = 1000  # number of particles to be deposited
EMPTY = 0  # empty cell state
CRYSTAL = 1  # crystal cell state
PARTICLE = 2  # particle cell state

def simulate_crystal_growth(grid):
    # set the seed in the middle of the grid
    grid[GRID_SIZE // 2][GRID_SIZE // 2] = CRYSTAL

    #randomly distribute all the particles
    for i in range (NUM_PARTICLES):
        # select a random location on the grid for the particle
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        
        if (grid[x][y] != CRYSTAL):
            grid[x][y] = PARTICLE



    
    # simulate the deposition of NUM_PARTICLES particles
    for _ in range(NUM_PARTICLES):
        # select a random location on the grid for the particle
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        
        # continue moving the particle in a random direction until it lands next to a crystal cell
        while grid[x][y] != CRYSTAL:
            grid[x][y] = PARTICLE  # set the current cell to a particle cell
            direction = random.randint(0, 3)  # choose a random direction (up, down, left, or right)
            grid[x][y] = EMPTY  # reset the current cell to empty
            
            # move the particle in the selected direction (wrapping around the edges of the grid)
            if direction == 0:
                x = (x + 1) % GRID_SIZE  # move down
            elif direction == 1:
                x = (x - 1 + GRID_SIZE) % GRID_SIZE  # move up
            elif direction == 2:
                y = (y + 1) % GRID_SIZE  # move right
            else:
                y = (y - 1 + GRID_SIZE) % GRID_SIZE  # move left
                
            # if the new cell is adjacent to a crystal cell, it becomes a crystal cell as well
            if is_next_to_crystal(grid, x, y):
                grid[x][y] = CRYSTAL
                break

def is_next_to_crystal(grid, x, y):
    # check if the cell to the right, left, above, or below the given cell is a crystal cell
    return grid[(x + 1) % GRID_SIZE][y] == CRYSTAL or \
           grid[(x - 1 + GRID_SIZE) % GRID_SIZE][y] == CRYSTAL or \
           grid[x][(y + 1) % GRID_SIZE] == CRYSTAL or \
           grid[x][(y - 1 + GRID_SIZE) % GRID_SIZE] == CRYSTAL


# create a GRID_SIZE x GRID_SIZE grid with all cells initialized to EMPTY
grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# run the crystal growth simulation on the grid
simulate_crystal_growth(grid)

# print the final state of the grid
plt.imshow(grid)
plt.show()
