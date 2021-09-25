import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)  # Set the seed
print(np.random.rand()) # Generate and print random float
print(np.random.randint(1,7)) # Use randint() to simulate a dice
print(np.random.randint(1,7)) # Use randint() again

# Initialize all_walks to stimulate multiple Walks
all_walks = []

# Simulate random walk 500 times
for i in range(500):
    # Initialize random_walk so as to store the action that is coming out roll of dice via if else loop
    random_walk = [0]
    # A for loop to iterate the throw of dice 100 times
    for i in range(100) :
        step = random_walk[-1]   # Set step: last element in random_walk
        dice =np.random.randint(1,7)  # Roll the dice
        # The If else loop to determine the movement up or down
        if dice <= 2 :
            # As we cannot have negative values so we use the max to make sure step can't go below 0
            step = max(0,step - 1)
        elif dice <=5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
        # Implement clumsiness : There's still something we forgot! You're a bit clumsy and you have a 0.1% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0.
        if np.random.rand() <= 0.001:
            step = 0
        # Append the output from above if else in random_walk
        random_walk.append(step)
    # Append random_walk to all_walks
    all_walks.append(random_walk)

# # Print random_walk
# print(random_walk)
#
# # Print all_walks
# print(all_walks)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()

# # Clear the figure
# plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()