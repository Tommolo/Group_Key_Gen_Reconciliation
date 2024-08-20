import numpy as np
from quantization_by_index import *
from plots import *


# Generate channel coefficient for two nodes topology with Eve the eavesdropper
def generate_channel_coefficients(num_of_samples,rho_ab_ba, rho_ab_ae, rho_ba_be):

    # Generate a random variable from rayleigh distribution
    magnitude = np.random.rayleigh(scale=1.0, size=num_of_samples)
    # Generate uniformly distributed phases
    phase = np.random.uniform(0,2*np.pi, num_of_samples)

    # Combine amplitude and phase to form complex coefficients
    h_ba= magnitude * np.exp(1j * phase) 

    # Generate Gaussian-distributed channel-indipendent measurement error at Bob
    eps_ab_magnitude = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ab_phase= np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ab = eps_ab_magnitude * np.exp(1j * eps_ab_phase) 

    #at eve pov alice
    eps_ae_magnitude = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ae_phase= np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ae = eps_ae_magnitude * np.exp(1j * eps_ae_phase)

    #at eve pov bob
    eps_be_magnitude = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_be_phase= np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_be = eps_be_magnitude * np.exp(1j * eps_be_phase)

   
    # Compute the correlated coefficients from Bob's point of view 
    h_ab = rho_ab_ba * h_ba + np.sqrt(1 - rho_ab_ba**2)  * eps_ab

    # Compute the correlated coefficients from Eve's point of view (Alice to Eve and Bob to Eve)
    h_ae = rho_ab_ae * h_ab + np.sqrt(1 - rho_ab_ae**2)  * eps_ae
    h_be = rho_ba_be * h_ba + np.sqrt(1 - rho_ba_be**2)  * eps_be


    return {"h_ba": h_ba,
            "h_ab": h_ab,
            "h_ae": h_ae,
            "h_be": h_be
            }

