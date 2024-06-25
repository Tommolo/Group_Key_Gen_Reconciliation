import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
import math

def generate_nakagami_m_channel(num_samples, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=np.sqrt(Omega), size=num_samples)
    return magnitudes

# Example parameters
num_samples = 128
m = 3 # Shape parameter (typically m >= 0.5)
Omega = 2  # Scale parameter (mean power)
Ptx = 10 # Power transmission in dBm
d_ab = 50  # Distance in meters
d_ae = 100  # Distance in meters
alpha = 2  # Path loss exponent

# Arrays to store the lengths of intersections
intersection_lengths = []
iterations=100

# Run the code 100 times
for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_samples, m, Omega)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_samples, m, Omega)

    eps = np.random.normal(loc=0, scale=1, size=num_samples)

    # Compute the cross-correlation
    p = 0.95 # Example correlation coefficient

    # Update h_ab based on h_ba and eps
    h_ab = (p * h_ba) + (1 - math.pow(p,2)*eps)**1/2

    # Calculate RSSI for Alice (gamma_ab) and Bob (gamma_ba)
    gamma_ab = (Ptx + abs(h_ab)** 2 * d_ab **-alpha)/2
    gamma_ba = (Ptx + abs(h_ba)** 2 * d_ab **-alpha)/2
    gamma_ae = (Ptx + abs(h_ae)** 2 * d_ae **-alpha)/2

    # Round RSSI values
    cleaned_numbers_ab = np.round(gamma_ab, 4)
    cleaned_numbers_ba = np.round(gamma_ba, 4) 
    cleaned_numbers_ae = np.round(gamma_ae, 4) 

    # Convert to sets
    set1 = set(cleaned_numbers_ab)
    set2 = set(cleaned_numbers_ba)
    set3 = set(cleaned_numbers_ae)

    # Find intersections
    intersection = set1.intersection(set2)
    intersection2 = set1.intersection(set3)

    # Store lengths of intersections
    intersection_lengths.append((len(intersection), len(intersection2)))

# Separate intersection lengths for plotting
intersection1_lengths = [x[0] for x in intersection_lengths]
intersection2_lengths = [x[1] for x in intersection_lengths]

print(intersection1_lengths)
print(intersection2_lengths)
# Plot histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(intersection1_lengths, bins=20, color='blue', alpha=0.7,edgecolor='black')
plt.title('Histogram of common values for Alice and Bob')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(intersection2_lengths, bins=20, color='red', alpha=0.7, edgecolor='black')
plt.title('Histogram of common values for Alice and Eve')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
