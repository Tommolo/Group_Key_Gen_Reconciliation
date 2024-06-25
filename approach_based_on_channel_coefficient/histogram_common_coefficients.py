import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
import math

def generate_nakagami_m_channel(num_measurements, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=Omega, size=num_measurements)
    return magnitudes

# Example parameters
num_measurements = 128
m = 3 # Shape parameter (typically m >= 0.5)

Omega_Alice = 1  # Scale parameter (mean power) for alice
Omega_eve = 2  # Scale parameter (mean power) for eve

# Arrays to store the lengths of intersections
intersection_lengths = []
iterations=1000

# Run the code 100 times
for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_measurements, m, Omega_Alice)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_measurements, m, Omega_eve)

    eps = np.random.normal(loc=0, scale=1, size=num_measurements)

    # Compute the cross-correlation
    rho = 0.97 # Example correlation coefficient

    # Update h_ab based on h_ba and eps
    h_ab = (rho * h_ba) + (1 - math.pow(rho,2)*eps)**1/2

    # channel coefficients
    h_ab = np.round(h_ab,2)
    h_ba = np.round(h_ba,2)
    h_ae = np.round(h_ae,2)

    #channel coefficient sets 
    set_ab = set(h_ab)
    set_ba = set(h_ba)
    set_ae = set(h_ae)

    # Find intersections
    intersection_ba_ab = set_ba.intersection(set_ab)
    intersection_ba_ae = set_ba.intersection(set_ae)

    # Store lengths of intersections
    intersection_lengths.append((len(intersection_ba_ab), len(intersection_ba_ae)))

# Separate intersection lengths for plotting
intersection_ba_ab_lengths = [x[0] for x in intersection_lengths]
intersection_ba_ae_lengths = [x[1] for x in intersection_lengths]

print(intersection_ba_ab_lengths)
print(intersection_ba_ae_lengths)
# Plot histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(intersection_ba_ab_lengths, bins=20, color='blue', alpha=0.7,edgecolor='black')
plt.title('Histogram of common values for Alice and Bob')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(intersection_ba_ae_lengths, bins=20, color='red', alpha=0.7, edgecolor='black')
plt.title('Histogram of common values for Alice and Eve')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
