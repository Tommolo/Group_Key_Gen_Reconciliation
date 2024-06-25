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
m = 3  # Shape parameter (typically m >= 0.5)
Omega = 2  # Scale parameter (mean power)
Ptx = 10  # Power transmission in dBm
d_ab = 50  # Distance in meters
d_ae = 100  # Distance in meters
alpha = 2  # Path loss exponent

p = 0.95  # Example correlation coefficient
iterations = 100
intersection_lengths = []
intersection2_lengths = []

for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_samples, m, Omega)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_samples, m, Omega)

    eps = np.random.normal(loc=0, scale=1, size=num_samples)

    # Compute the cross-correlation
    h_ab = p * h_ba + (1 - p**2*eps)**1/2  # Update h_ab

    # Calculate RSSI
    gamma_ab = (Ptx + abs(h_ab)**2 * d_ab**-alpha) / 2
    gamma_ba = (Ptx + abs(h_ba)**2 * d_ab**-alpha) / 2

    gamma_ae = (Ptx + abs(h_ae)**2 * d_ae**-alpha) / 2

    # Clean and round RSSI values

    cleaned_numbers_ab = np.round(gamma_ab,4)

    print(cleaned_numbers_ab)

    cleaned_numbers_ba = np.round(gamma_ba,4)
    cleaned_numbers_ae = np.round(gamma_ae,4)

    # Convert to sets
    set1 = set(cleaned_numbers_ab)
    set2 = set(cleaned_numbers_ba)
    set3 = set(cleaned_numbers_ae)

    # Calculate intersections
    intersection = set1.intersection(set2)
    intersection2 = set1.intersection(set3)

    # Store length of intersection and intersection2
    intersection_lengths.append(len(intersection))
    intersection2_lengths.append(len(intersection2))

print(intersection2_lengths)
# Calculate probabilities
prob_intersection = {length: intersection_lengths.count(length) / iterations for length in set(intersection_lengths)}
prob_intersection2 = {length: intersection2_lengths.count(length) / iterations for length in set(intersection2_lengths)}

# Sort probabilities by length for plotting
sorted_lengths_intersection = sorted(prob_intersection.keys())
sorted_probs_intersection = [prob_intersection[length] for length in sorted_lengths_intersection]

sorted_lengths_intersection2 = sorted(prob_intersection2.keys())
sorted_probs_intersection2 = [prob_intersection2[length] for length in sorted_lengths_intersection2]

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(sorted_lengths_intersection, sorted_probs_intersection, color='skyblue', edgecolor='black')
plt.xlabel('Common values')
plt.ylabel('Probability')
plt.title('Probability Distribution for Alice and Bob intersection')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(sorted_lengths_intersection2, sorted_probs_intersection2, color='salmon', edgecolor='black')
plt.xlabel('Common values')
plt.ylabel('Probability')
plt.title('Probability Distribution for Alice and Eve intersection')
plt.grid(True)

plt.tight_layout()
plt.show()

