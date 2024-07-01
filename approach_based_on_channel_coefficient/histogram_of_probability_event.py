import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
import math

def generate_nakagami_m_channel(num_measurements, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=Omega, size=num_measurements)
    return magnitudes


# Example parameters
num_samples = 128
m = 3  # Shape parameter (typically m >= 0.5)

Omega_alice = 1  # Scale parameter (mean power)
Omega_eve = 2  # Scale parameter (mean power)

rho = 0.97  # Example correlation coefficient
iterations = 1000
intersection_ba_ab_lengths = []
intersection_ba_ae_lengths = []

for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_samples, m, Omega_alice)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_samples, m, Omega_eve)

    eps = np.random.normal(loc=0, scale=1, size=num_samples)

    # Compute the cross-correlation
    h_ab = rho * h_ba + (1 - rho**2*eps)**1/2  # Update h_ab

    # take the first two decimal values on channel coefficient values
    h_ba = np.round(h_ba,2)
    h_ab = np.round(h_ab,2)
    h_ae = np.round(h_ae,2)

    # Convert to sets
    set_ba = set(h_ba)
    set_ab = set(h_ab)
    set_ae = set(h_ae)

    # Calculate intersections
    intersection_ba_ab = set_ba.intersection(set_ab)
    intersection_ba_ae = set_ba.intersection(set_ae)

    # Store length of intersection and intersection2
    intersection_ba_ab_lengths.append(len(intersection_ba_ab))
    intersection_ba_ae_lengths.append(len(intersection_ba_ae))

# Calculate probabilities length as key and probabilty (number of elements/iterations) as value
prob_intersection = {length: intersection_ba_ab_lengths.count(length) / iterations for length in set(intersection_ba_ab_lengths)}
prob_intersection2 = {length: intersection_ba_ae_lengths.count(length) / iterations for length in set(intersection_ba_ae_lengths)}

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

