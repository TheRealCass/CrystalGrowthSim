# PHYS 2010 [A01] 
## FINAL PROJECT
------------------------

### Answer to Quesion 1

An agent-based model (AVM) is a computational model that simulates the actions and interactions of autonomous agents in order to understand complex systems. To create an agent-based model for this project, I would need to define the agents (in this case, the particles) and their behavior (in this case, performing random walks in continuous space). I would also need to define the rules for how the agents interact with each other and with their environment (in this case, how they stick to the crystal when they get close to it)

--------

To create an agent-based model for crystal growth,

Define the initial seed (impurity) and the initial positions of the particles (agents) in continuous space.
At each time step, update the positions of the particles based on a random distribution that models Brownian motion.
Check if any particle is close enough to the crystal (initial seed or previously stuck particles) to get stuck. If so, update the crystal and remove the particle from the simulation.
Repeat steps 2-3 until the desired crystal size is reached or a maximum number of time steps is reached.
To create a cellular automaton for crystal growth, you could follow these steps: