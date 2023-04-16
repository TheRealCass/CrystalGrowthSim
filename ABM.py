import random # Import the random module to generate random numbers
import imageio # Import the imageio module to save GIFs
import numpy as np # Import the numpy module for numerical operations
from PIL import Image, ImageDraw # Import the Image and ImageDraw classes from the PIL module to create and draw images

# Step 1: Define the agents and their behavior
class Particle: # Define a class for particles
    def __init__(self, x, y): # Constructor method for the Particle class
        self.x = x # Set the x-coordinate of the particle
        self.y = y # Set the y-coordinate of the particle

    def move(self): # Method to move the particle
        # Brownian motion
        self.x += random.gauss(0, 1) # Update the x-coordinate of the particle by adding a random number from a Gaussian distribution with mean 1 and standard deviation 1
        self.y += random.gauss(0, 1) # Update the y-coordinate of the particle by adding a random number from a Gaussian distribution with mean 1 and standard deviation 1

# Step 2: Define the environment
class Environment: # Define a class for the environment
    def __init__(self, width, height): # Constructor method for the Environment class
        self.width = width # Set the width of the environment
        self.height = height # Set the height of the environment
        self.particles = [] # Initialize an empty list to store particles in the environment
        self.crystal = [] # Initialize an empty list to store particles in the crystal

    def add_particle(self, particle): # Method to add a particle to the environment
        self.particles.append(particle) # Add the particle to the list of particles in the environment

    def add_to_crystal(self, particle): # Method to add a particle to the crystal
        self.crystal.append(particle) # Add the particle to the list of particles in the crystal

    def is_particle_near_crystal(self, particle): # Method to check if a particle is near the crystal
        threshold_distance = 1 # Set a threshold distance for particles to stick to the crystal
        for crystal_particle in self.crystal: # Loop over all particles in the crystal
            dx = crystal_particle.x - particle.x # Calculate the difference in x-coordinates between the crystal particle and the given particle
            dy = crystal_particle.y - particle.y # Calculate the difference in y-coordinates between the crystal particle and the given particle
            distance = np.sqrt(dx*dx + dy*dy) # Calculate the distance between the crystal particle and given particle using Pythagoras' theorem
            if distance <= threshold_distance: # Check if distance is less than threshold distance
                return True # If so, return True (particle is near crystal)
        return False # If no particles in crystal are within threshold distance of given particle, return False (particle is not near crystal)

# Step 3: Define rules for crystal growth (already done in Environment class)

# Step 4: Initialize model
num_particles = 2000 # Set number of particles in environment
width = 100 # Set width of environment (in pixels)
height = 100 # Set height of environment (in pixels)

environment = Environment(width, height) # Create an instance of Environment class with given width and height

# Add particles to environment
for i in range(num_particles): # Loop over number of particles to add to environment
    x = random.uniform(0, width) # Generate a random x-coordinate within environment boundaries
    y = random.uniform(0, height) # Generate a random y-coordinate within environment boundaries
    particle = Particle(x, y) # Create an instance of Particle class with generated coordinates
    environment.add_particle(particle) # Add created particle to environment

# Add seed to environment (initial point for crystal growth)
seed = Particle(width/2, height/2) # Create an instance of Particle class at center of environment (this will be seed for crystal growth)
environment.add_to_crystal(seed) # Add seed to crystal

# Step 5-7: Simulate motion of particles and update crystal
frames = [] # Initialize an empty list to store frames for GIF animation
num_steps = 100 # Set number of time steps for simulation

for step in range(num_steps): # Loop over number of time steps in simulation
    # Create image for this frame
    image = Image.new("RGB", (width, height), "black") # Create a new black image with given width and height (in pixels)
    draw = ImageDraw.Draw(image) # Create an ImageDraw object to draw on the image

    # Draw particles
    for particle in environment.particles: # Loop over all particles in environment
        # Draw an ellipse centered at particle's position with radius 1 and fill color white
        draw.point((particle.x, particle.y), fill="white")

    # Draw crystal
    for particle in environment.crystal: # Loop over all particles in crystal
        # Draw an ellipse centered at particle's position with radius 1 and fill color red
        draw.point((particle.x, particle.y), fill="red")

    # Save frame
    frames.append(image) # Add created image to list of frames for GIF animation

    # Move particles
    for particle in environment.particles: # Loop over all particles in environment
        particle.move() # Move each particle according to its behavior (Brownian motion)

    # Update crystal
    for particle in environment.particles[:]: # Loop over a copy of the list of particles in environment (to avoid modifying list while iterating over it)
        if environment.is_particle_near_crystal(particle): # Check if particle is near crystal
            environment.add_to_crystal(particle) # If so, add particle to crystal
            environment.particles.remove(particle) # And remove particle from environment

     

# Save GIF
imageio.mimsave("ABM_Sim.gif", frames) # Save list of frames as a GIF animation using imageio module