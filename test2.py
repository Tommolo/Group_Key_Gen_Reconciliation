import numpy as np
from scipy.special import gammaincc
from scipy.optimize import root_scalar

# Function Q of Marcum
def Q_m(m, alpha, beta):
    return gammaincc(m, (alpha**2 + beta**2) / 2) * np.exp(-alpha**2 / 2)

# Function to solve inverse CDF for gamma_ab
def inverse_cdf(gamma_ab, gamma_ba, m, rho, gamma, r):
    alpha = np.sqrt(2 * m * rho * gamma_ba / (gamma * (1 - rho)))
    beta = np.sqrt(2 * m * gamma_ab / (gamma * (1 - rho)))
    return Q_m(m, alpha, beta) - (1 - r)

# Parameters
N = 100  # Number of RSS samples
m = 2  # Order of the Marcum-Q function
rho = 0.8  # Correlation coefficient
gamma = 1.0  # Mean value of RSS

# Generate RSS samples for Alice
gamma_ba_samples = np.random.gamma(m, gamma / m, N)

# Generate RSS samples for Bob
gamma_ab_samples = np.zeros(N)
for i in range(N):
    r = np.random.rand()
    try:
        result = root_scalar(inverse_cdf, args=(gamma_ba_samples[i], m, rho, gamma, r), bracket=[0, 10*gamma])
        gamma_ab_samples[i] = result.root
    except ValueError as e:
        print(f"Error in solving equation for i={i}: {e}")
        gamma_ab_samples[i] = np.nan

print(gamma_ba_samples, gamma_ab_samples)
