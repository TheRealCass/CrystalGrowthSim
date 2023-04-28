###############################################################################################################################
# AUTHOR: Rubait Ul Ahamed
# 
# REMARKS: Simulates the groth of a crystal given a impurity in the middle of the enviournment. This simulation uses
#       Cellular Atomaton (CA) to achieve it's final result
# 
###############################################################################################################################

import random as dealer  # Import the random module to generate random numbers
from imageio import mimsave as save_video  # Import the imageio module to save GIFs
import numpy as math_library # Import the numpy module for numerical operations


# Define the states
EMPTY = 0
PARTICLE = 1
CRYSTAL = 2

# other constats 
TOTAL_SPOTS = 10000 # number of total spaces that molicules can occupy
DENSITY = 0.25 # percentage of molicule to empty space in the solution
MAX_VELOCITY = 1 # maximum velocity a molicule. Related to the energy a molicule has
RUN_CYCLE = 120 # total number to time passed after the start of the simulation
LIQUID_MOLICULE_COLOUR = [255, 255, 255] # color representing molicule
CRYSTAL_MOLICULE_COLOUR = [255, 0, 0] # colour representing crystal
OUTPUT_FILE = "CA_Sim" # name of the output gif file to be created






###############################################################################################################################


def simulate (run_cycle):
    """
    Simultes the movement of the liquid at each point in time
    """

    images = [] # array to save easch snapshopt in time
    grid = create_grid(TOTAL_SPOTS, DENSITY) #creating grid to represent our vessel

    for step in range(run_cycle):
        # Update the grid at each time step
        grid = update(grid)
        # Generate an image of the current state of the grid and add it to the list of images
        image = generate_image(grid)
        images.append(image) # add each snapshopt in time to the images array

    # Save the list of images as an animated GIF using imageio.mimsave()
    save_video(OUTPUT_FILE + ".gif", images)




def create_grid(total_spots, density):
    """
    creates a grid that represents the enviournemnt the liquid is in

    Args:
        total_spots: total possible dinstinct loaction any one molicule ca be at
        density: the ratio of the number of molicules to the amount of free space in the vessel

    Returns:
        a 2D grid that 1) has the number of total spots that was passed in
                       2) molicules scatered in this enviournment randomly based on the density
                       3) a seed (impurity) that has been placed in the middle 
    """
    
    # Define the grid size and number of particles
    grid_size = int(math_library.sqrt(total_spots))
    num_particles = int(grid_size * density) * 100

    # Initialize the grid by filling it with empty space
    grid = [[EMPTY for x in range(grid_size)] for y in range(grid_size)]

    # Scatter particles randomly
    for i in range(num_particles):
        x = dealer.randint(0, grid_size-1)
        y = dealer.randint(0, grid_size-1)
        grid[x][y] = PARTICLE

    # Place the seed in the middle
    grid[grid_size//2][grid_size//2] = CRYSTAL

    #return created grid
    return grid




def update(grid):
    """
    updaats the grid according to the rules of the ABM

    Args:
        grid: the 2D array that represents the enviournment

    Returns:
        the updates grid after one step of time has passed. The updated
        grid reflects teh rules of the ABM
    """


    # Create a copy of the grid to update. This is necessary because we need to
    # update all cells simultaneously. If we updated the cells one by one in the
    # original grid, the updates would affect each other
    grid_size = len(grid)
    new_grid = [row[:] for row in grid]
    
    # Loop over all cells in the grid
    for x in range(grid_size):
        for y in range(grid_size):
            # If the cell contains a particle
            if grid[x][y] == PARTICLE:
                # Move particle
                # Choose a random direction to move in (up, down, left, right or diagonally)
                dx = dealer.randint(-MAX_VELOCITY, MAX_VELOCITY)
                dy = dealer.randint(-MAX_VELOCITY, MAX_VELOCITY)
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




def generate_image(grid):
    """
    generates Image object for each snapshot in time

    Returns:
        an image abject for that snapshot
    """

    #get the grid size
    grid_size = len(grid)
    # Create an empty RGB image with the same size as the grid
    image = math_library.zeros((grid_size, grid_size, 3), dtype = math_library.uint8)
    # Loop over all cells in the grid
    for x in range(grid_size):
        for y in range(grid_size):
            # If the cell contains a particle, set its color to white in the image
            if grid[x][y] == PARTICLE:
                image[x,y] = LIQUID_MOLICULE_COLOUR
            # If the cell is part of the crystal, set its color to red in the image
            elif grid[x][y] == CRYSTAL:
                image[x,y] = CRYSTAL_MOLICULE_COLOUR
    return image

###############################################################################################################################


# FINALLY, run the simulation
simulate(RUN_CYCLE)


###############################################################################################################################