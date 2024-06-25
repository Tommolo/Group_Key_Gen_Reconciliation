import numpy as np
import scipy.special as sp
import scipy.optimize
import matplotlib.pyplot as plt
import marcumq
from scipy.special import gammainccinv
from scipy.optimize import fsolve
# Parameters
m = 2  # Nakagami fading parameter
rho = 0.97 # Correlation coefficient
Pt = 100 # Transmit power in dBm
d_ab = 10  # Distance between Alice and Bob in meters
d_ae = 30  # Distance between Alice and Eve in meters
path_loss_exponent = 2  # Path-loss exponent
N = 128  # Number of samples (probes)

# Function to generate RSS samples at Alice
def generate_rss_alice(m, Pt, d_ab, path_loss_exponent, N):
    gamma_bar = Pt * (d_ab ** -path_loss_exponent)
    VAlice = np.random.gamma(m, gamma_bar / m, N)
    return VAlice

# Function to solve the RSS value for Bob
def solve_rss(r, VAlice_i, m, rho, Pt, d_ab, path_loss_exponent):
    gamma_bar = Pt *(d_ab ** -path_loss_exponent)
    def equation(gamma_ab):
        return r - (1 - marcumq.marcumq(m, np.sqrt((2 * m * rho * VAlice_i) / (gamma_bar * (1 - rho))), np.sqrt((2 * m * gamma_ab) / (gamma_bar * (1 - rho)))))
    gamma_ab = scipy.optimize.fsolve(equation, VAlice_i)[0]
    return gamma_ab

# Function to generate correlated RSS samples at Bob
def generate_rss_bob(VAlice, m, rho, Pt, d_ab, path_loss_exponent, N):
    VBob = np.zeros(N)
    for i in range(N):
        r = np.random.rand()
        VBob[i] = solve_rss(r, VAlice[i], m, rho, Pt, d_ab, path_loss_exponent)
    return VBob

# Function to generate independent RSS samples for Eve
def generate_rss_eve(m, Pt, d_ae, path_loss_exponent, N):
    gamma_bar = Pt * (d_ae ** -path_loss_exponent)
    VEve = np.random.gamma(m, gamma_bar / m, N)
    return VEve

# Generate RSS samples
VAlice = generate_rss_alice(m, Pt, d_ab, path_loss_exponent, N)
VBob = generate_rss_bob(VAlice, m, rho, Pt, d_ab, path_loss_exponent, N)
VEve = generate_rss_eve(m, Pt, d_ae, path_loss_exponent, N)

# Clean and round the RSS samples
VAlice_formatted = np.round(VAlice, 4)
VBob_formatted = np.round(VBob,4)
VEve_formatted = np.round(VEve,4)

print(VAlice)
print(VEve)
print(VAlice_formatted)
# Convert lists to sets for intersection
set1 = set(VAlice_formatted)
set2 = set(VBob_formatted)
set3 = set(VEve_formatted)

# Calculate intersections
intersection_ba_ab = set1.intersection(set2)
intersection_ba_ae = set1.intersection(set3)


# Output the generated samples
print(set1)
print(set2)

print("Intersection_ba_ab: ", intersection_ba_ab, "Length: ", len(intersection_ba_ab))
print("Intersection_ba_ae: ", intersection_ba_ae, "Length: ", len(intersection_ba_ae))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(VAlice, label='Alice', marker='o', linestyle='None')
plt.plot(VBob, label='Bob', marker='x', linestyle='None')
plt.plot(VEve, label='Eve', marker='s', linestyle='None')
plt.xlabel('Probe Index')
plt.ylabel('RSS Value')
plt.title('RSS Samples for Alice, Bob, and Eve')
plt.legend()
plt.grid(True)
plt.show()
