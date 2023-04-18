###############################################################################################################################
# NAME: Rubait Ul Ahamed
# STUDENT NUMBER: 7876180
# COURSE: PHYS 2010, SECTION: A01
# INSTRUCTOR: Jesko Sirkir
# FINAL PROJECT
# 
# REMARKS: Simulates the groth of a crystal given a impurity in the middle of the enviournment. This simulation uses
#       Agent-Based Model (ABM) to achieve it's final result
# 
###############################################################################################################################


import random as dealer # Import the dealer module to generate dealer numbers
from imageio import mimsave as save_video  # Import the imageio module to save GIFs
import numpy as math_library # Import the numpy module for numerical operations
# Import the Image and ImageDraw classes from the PIL module to create and draw images 
from PIL import Image
from PIL import ImageDraw as artist 

#constants
WIDTH_OF_BEAKER = 100
HEIGHT_OF_BEAKER = 100
RUN_CYCLE = 120
DENSITY = 0.75
THRUSHOLD_DISTANCE = 1
MAX_VELOCITY = 1
LIQUID_MOLICULE_COLOUR = "white" # color representing molicule
CRYSTAL_MOLICULE_COLOUR = "red" # colour representing crystal
OUTPUT_FILE = "ABM_Sim" # name of the output gif file to be created









# Classes needed for the simulation (Particle and Enviournment class)
###############################################################################################################################


class Particle:
    """
    Define a class for particles
    """



    def __init__(self, x, y):
        """
        Constructor method for the Particle class
        
        Args:
            x: loaction data in the x plane
            y: location data in the y plane
        """

        self.x = x # Set the x-coordinate of the particle
        self.y = y # Set the y-coordinate of the particle




    def  move(self):
        """
        Method to move the particle with a random velocity
        """

        # Brownian motion using random interger generator
        self.x += dealer.randint(-MAX_VELOCITY, MAX_VELOCITY)
        self.y += dealer.randint(-MAX_VELOCITY, MAX_VELOCITY)


#--------------------------------------------------------------------------------------------------------------------------


class Environment:
    """
    Define a class for the environment
    """




    def __init__(self, width, height):
        """
        Constructor method for the Environment class

        Args:
            width: width of the enviournment
            height: height of the enviournment
        """

        self.width = width # Set the width of the environment
        self.height = height # Set the height of the environment
        self.particles = [] # Initialize an empty list to store particles in the environment
        self.crystal = [] # Initialize an empty list to store particles in the crystal




    def add_particle(self, particle):
        """
        Method to add a particle to the environment

        Args:
            particle: particle to add to the enviournment
        """

        self.particles.append(particle)




    def add_to_crystal(self, particle):
        """
        Method to add a particle to the crystal

        Args:
            particle: particle to add to the crystal formation
        """

        self.crystal.append(particle)




    def is_particle_near_crystal(self, particle):
        """
        Method to check if a particle is near the crystal

        Args:
            particle: particle to check

        Returns:
            True is particle is close to a crystal molicule, false if not
        """

        for crystal_particle in self.crystal: # Loop over all particles in the crystal
            # Calculate the difference in x & y coordinates between the crystal particle and the given particle
            dx = crystal_particle.x - particle.x 
            dy = crystal_particle.y - particle.y 

            # Calculate the distance between the crystal particle and given particle using Pythagoras' theorem
            distance = math_library.sqrt(dx*dx + dy*dy)

            if (distance <= THRUSHOLD_DISTANCE): # Check if distance is less than threshold distance
                return True # If so, return True (particle is near crystal)
        
        # If no particles in crystal are within threshold distance of given particle, return False (particle is not near crystal)
        return False 
    

###############################################################################################################################








def generate_enviournmnet(width, height):
    """
    generates a enviournmnent given the width & height

    Args:
        width: width of the enviournment
        height: height of the enviournment

    Returns:
        an Enviournment obj with the width and height that was requested
    """
    
    # find the number of total particleas in the enviournment
    total_spots = width * height
    num_particles = int((total_spots * DENSITY)) 

    environment = Environment(width, height) # Create an instance of Environment class with given width and height

    # add particles at random location throught the enviournment
    for i in range(num_particles):
        # get random location to initiate the particle
        x = dealer.uniform(0, width)
        y = dealer.uniform(0, height)

        #initiate and add the particle to the enviournment
        particle = Particle(x, y) 
        environment.add_particle(particle)

    # Create and add a seed to environment at the cenetrpoint (initial point for crystal growth)
    seed = Particle(width/2, height/2) 
    environment.add_to_crystal(seed)

    # return the fully set-up enviournment
    return environment




def save_grid_state(enviournmnent):
    """
    Convers the location data of the molicules in a single snapshot in time as a image object

    Args:
        enviournment: the enviournment the molicules are in
    
    Returns:
        image object that represent the current location of all the molicules in current
        snapshot of time
    """

    # Create image for this frame
    image = Image.new("RGB", (enviournmnent.width, enviournmnent.height), "black") # setting backgroung colour to black
    canvas = artist.Draw(image) # Create an ImageDraw object to draw on the image

    # Loop over all particles in environment to draw them as a point
    for particle in enviournmnent.particles: 
        canvas.point((particle.x, particle.y), fill = LIQUID_MOLICULE_COLOUR)

    #  Loop over all particles in crystal to draw them
    for particle in enviournmnent.crystal:
        canvas.point((particle.x, particle.y), fill = CRYSTAL_MOLICULE_COLOUR)

    # return the drawn image object
    return image




def update_molicules(enviournmnent):
    """
    Updates the loaction of the molicule in some random direction
    Also, checks if any molicule is close to a crystal molicule, and if
    so, it sticks to it

    Args:
        enviournment: Enviournnmnet the molicules are in
    """
    
    # Loop over all particles in environment to move them
    for particle in enviournmnent.particles:
        particle.move()

    # Update crystal
    # Loop over a copy of the list of particles in environment (to avoid modifying list while iterating over it)
    for particle in enviournmnent.particles[:]:
        if enviournmnent.is_particle_near_crystal(particle): # if particle is near crystal
            enviournmnent.add_to_crystal(particle) # add particle to crystal
            enviournmnent.particles.remove(particle) # remove particle from environment



def simulate(run_cycle):
    """
    Simulates the growth of crystal from imitial seed in the middle in a solution that is in a beaker
    
    Args:
        run_cycle: number of time steps you want the simulation to run
        width: width of the beaker
        height: height of the beaker
    """

    beaker = generate_enviournmnet(WIDTH_OF_BEAKER, HEIGHT_OF_BEAKER)
    
    # Initialize an empty list to store frames for GIF animation
    frames = []

    for step in range(run_cycle): # Loop over number of time steps in simulation

        # get image obj for this frame and append it to to array keeping track of images in each frame of time
        snapshot_in_time = save_grid_state(beaker)
        frames.append(snapshot_in_time) 

        #updates the location and type of the molicules based on the rules of the AVM
        update_molicules(beaker)      

    # Save GIF
    save_video(OUTPUT_FILE + ".gif", frames) # Save list of frames as a GIF animation using imageio module




###############################################################################################################################

# finally run the simulation
simulate(RUN_CYCLE)

###############################################################################################################################