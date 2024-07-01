import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nakagami

def generate_nakagami_samples(m, Omega, size=1000):
    """Generate samples from Nakagami distribution."""
    return nakagami.rvs(m, scale=Omega, size=size)

def plot_nakagami_distribution(samples, m, Omega, color, label):
    """Plot histogram of Nakagami samples."""
    plt.hist(samples, bins=30, density=True, color=color, alpha=0.7, label=label)
    plt.title(f'Nakagami-m different distribution ')
    plt.xlabel('Magnitude')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)

# Parameters for the two Nakagami distributions
params = [
    {'m': 3, 'Omega': 1, 'color': 'blue', 'label': 'm=3, Omega=1'},
    {'m': 3, 'Omega': 2, 'color': 'green', 'label': 'm=3, Omega=2'}
  
]

# Generate samples for each distribution
samples = [generate_nakagami_samples(param['m'], param['Omega']) for param in params]


# Plot the distributions
plt.figure(figsize=(12, 6))
for param, sample in zip(params, samples):
    plot_nakagami_distribution(sample, param['m'], param['Omega'], param['color'], param['label'])

plt.tight_layout()
plt.show()
