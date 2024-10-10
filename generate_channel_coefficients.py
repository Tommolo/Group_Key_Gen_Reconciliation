import numpy as np
from quantization_by_index import *
from plots import *


# Generate channel coefficient for two nodes topology with Eve the eavesdropper
def generate_channel_coefficients(num_of_samples):
    # Generate a random variable from Rayleigh distribution
    magnitude = np.random.rayleigh(scale=1.0, size=num_of_samples)
    # Generate uniformly distributed phases
    phase = np.random.uniform(0, 2 * np.pi, num_of_samples)

    # Combine amplitude and phase to form complex coefficients
    h_ba = magnitude * np.exp(1j * phase)

    # Generate Gaussian-distributed channel-independent measurement error at Bob
    eps_ab_magnitude = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ab_phase = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ab = eps_ab_magnitude * np.exp(1j * eps_ab_phase)

    # At Eve pov Bob
    eps_ae_magnitude = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ae_phase = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ae = eps_ae_magnitude * np.exp(1j * eps_ae_phase)

    # Generate an array of rho_ab_ba and rho_ab_ae in the range [0.7, 0.9] for each sample
    rho_ab = np.random.uniform(0.8, 1, size=num_of_samples)
    rho_ae = np.random.uniform(0.1, 0.2, size=num_of_samples)

    # Compute the correlated coefficients from Bob's point of view
    h_ab = rho_ab * h_ba + np.sqrt(1 - rho_ab**2) * eps_ab

    # Compute the correlated coefficients from Eve's point of view (Alice to Eve and Bob to Eve)
    h_ae = rho_ae * h_ba + np.sqrt(1 - rho_ae**2) * eps_ae

    return {
        "h_ba": h_ba,
        "h_ab": h_ab,
        "h_ae": h_ae,
        "rho_ab": rho_ab,  # Return the generated rho_ab_ba
        "rho_ae": rho_ae   # Return the generated rho_ab_ae
    }