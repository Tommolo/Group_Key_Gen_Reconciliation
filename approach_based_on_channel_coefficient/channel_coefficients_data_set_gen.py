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
m_ab = 3 # Shape parameter (typically m >= 0.5)
m_ae = 2

Omega_alice_bob = 1  # Scale parameter (mean power)
Omega_alice_eve = 1  # Scale parameter (mean power)

rho = 0.97 # cross correlation 


# Generate h_ba channel coefficient
h_ba = generate_nakagami_m_channel(num_measurements, m_ab, Omega_alice_bob)

# Generate h_ae channel coefficient
h_ae = generate_nakagami_m_channel(num_measurements, m_ae, Omega_alice_eve)

#Gaussian-distributed channel-indipendent measurement error at Bob
eps = np.random.normal(loc=0, scale=1, size=num_measurements)

#Correlation channel coefficient between h_ab and h_ba
h_ab = (rho * h_ba) + (1 - math.pow(rho,2)*eps)**1/2

# Approximation of channel coefficients.
h_ab = np.round(h_ab,2)
h_ba = np.round(h_ba,2)
h_ae = np.round(h_ae,2)


print(h_ab)
print(h_ba)
print(h_ae)

#Set construction for all three channel coefficients
set_ab = set(h_ab)
set_ba = set(h_ba)
set_ae = set(h_ae)

# common coefficient values ab_ba ae_ba
common_values_ba_ab = set_ba.intersection(set_ab)
common_values_ba_ae = set_ba.intersection(set_ae)

print(common_values_ba_ab, len(common_values_ba_ab))
print(common_values_ba_ae, len(common_values_ba_ae))

# Plot channel coefficient values
plt.figure(figsize=(10, 6))
plt.plot(h_ba, label='Alice', color='blue', marker='^')
plt.plot(h_ab, label='Bob', color='green', marker='x')
plt.plot(h_ae, label='Eve', color='red', marker='o')
plt.title('channel coefficient')
plt.xlabel('Sample Index')
plt.ylabel('channel coeffiecients')
plt.legend()
plt.grid(True)
plt.show()


def plot_nakagami_distribution(samples, color, label):
    """Plot histogram of Nakagami samples."""
    plt.hist(samples, bins=30, density=True, color=color, alpha=0.7, label=label)
    plt.title(f'Nakagami-m different distribution ')
    plt.xlabel('Magnitude')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)

samples=[h_ab,h_ba]
plot_nakagami_distribution(h_ab,color='green',label='A2B')
plot_nakagami_distribution(h_ba,color='blue',label='B2A')
plot_nakagami_distribution(h_ae,color='red',label='A2E')



plt.tight_layout()
plt.show()