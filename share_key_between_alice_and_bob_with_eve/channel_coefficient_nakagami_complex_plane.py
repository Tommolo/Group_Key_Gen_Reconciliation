import numpy as np
import random
import matplotlib.pyplot as plt

# Parameters
m = 3
Omega = 1

k = m / 2
tetha = 2 * Omega / m
size = 100

# Define a function to generate signed numbers
def sign_generator(number):
    # Generate a random number with either a positive or negative sign
    return random.choice([-1, 1]) * number

# Generate real and imaginary parts
real_part = sign_generator(np.sqrt(np.random.gamma(k, tetha, size=size)))
imaginary_part = sign_generator(np.sqrt(np.random.gamma(k, tetha, size=size))) * 1j
complex_numbers = real_part + imaginary_part

# Compute magnitudes (absolute values)
magnitudes = np.abs(complex_numbers)

# Plotting the distribution of magnitudes
plt.figure(figsize=(8, 6))
plt.hist(magnitudes, bins=20, edgecolor='black')
plt.title('Distribution of Magnitudes of Complex Numbers')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
