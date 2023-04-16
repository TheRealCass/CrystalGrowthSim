import random
import imageio
import numpy as np

# Define the grid size and number of particles
grid_size = 100
num_particles = 5000

# Define the states
EMPTY = 0
PARTICLE = 1
CRYSTAL = 2

# Initialize the grid
grid = [[EMPTY for x in range(grid_size)] for y in range(grid_size)]

# Scatter particles randomly
for i in range(num_particles):
    x = random.randint(0, grid_size-1)
    y = random.randint(0, grid_size-1)
    grid[x][y] = PARTICLE

# Place the seed
grid[grid_size//2][grid_size//2] = CRYSTAL

# Define the update function
def update(grid):
    # Create a copy of the grid to update
    # This is necessary because we need to update all cells simultaneously
    # If we updated the cells one by one in the original grid, the updates would affect each other
    new_grid = [row[:] for row in grid]
    
    # Loop over all cells in the grid
    for x in range(grid_size):
        for y in range(grid_size):
            # If the cell contains a particle
            if grid[x][y] == PARTICLE:
                # Move particle
                # Choose a random direction to move in (up, down, left, right or diagonally)
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                # Calculate the new position of the particle after moving
                new_x = (x + dx) % grid_size
                new_y = (y + dy) % grid_size
                # If the new cell is empty, move the particle there
                if new_grid[new_x][new_y] == EMPTY:
                    new_grid[new_x][new_y] = PARTICLE
                    new_grid[x][y] = EMPTY
                
                # Check for crystal formation
                # Loop over all neighboring cells
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # Skip the current cell
                        if dx == dy == 0:
                            continue
                        # Calculate the position of the neighboring cell
                        new_x = (x + dx) % grid_size
                        new_y = (y + dy) % grid_size
                        # If a neighboring cell is a crystal, turn this cell into a crystal as well
                        if grid[new_x][new_y] == CRYSTAL:
                            new_grid[x][y] = CRYSTAL
    
    # Return the updated grid
    return new_grid

# Define a function to generate an image from the grid
def generate_image(grid):
    # Create an empty RGB image with the same size as the grid
    image = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)
    # Loop over all cells in the grid
    for x in range(grid_size):
        for y in range(grid_size):
            # If the cell contains a particle, set its color to white in the image
            if grid[x][y] == PARTICLE:
                image[x,y] = [255, 255, 255]
            # If the cell is part of the crystal, set its color to red in the image
            elif grid[x][y] == CRYSTAL:
                image[x,y] = [255, 0, 0]
    return image

# Run the simulation and generate an animated GIF
num_steps = 100
images = []
for step in range(num_steps):
    # Update the grid at each time step
    grid = update(grid)
    # Generate an image of the current state of the grid and add it to the list of images
    image = generate_image(grid)
    images.append(image)

# Save the list of images as an animated GIF using imageio.mimsave()
imageio.mimsave('animation5.gif', images)
