#  must python3 -m pip install numpy
#  must python3 -m pip install matplotlib
# then run python3 test.py

# Import the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the normal distribution
mu = 0  # mean
sigma = 1  # standard deviation

# Generate the data
x = np.random.normal(mu, sigma, 1000)

# Plot the data
plt.plot(x)
plt.show()

# Save the data to a file
np.savetxt("results/normal_distribution.txt", x)