import numpy as np
from scipy.stats import nakagami
import json
from quantization_by_index import *
from plots import *


# Specify the path to your JSON file
file_path = r'C:\Users\pieru\Documents\Python\Group_Key_Gen_Reconciliation\share_key_between_alice_and_bob_with_eve\parameters.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

num_of_samples = data['simulation_parameters']['num_of_samples']
iterations = data['simulation_parameters']['iterations']
num_dec_values = data['simulation_parameters']['num_dec_values']

delta_max_alice = 0
delta_min_alice = 0.5

delta_max_bob = 1
delta_min_bob = 2


# Generate channel coefficient for tow nodes topology with Eve the eavesdropper
def generate_channel_coefficients(rho_ab_ba, rho_ab_ae, rho_ba_be):

    # Generate a random variable from rayleigh distirbution
    magnitude = np.random.rayleigh(scale=1.0, size=num_of_samples)
    # Generate uniformly distributed phases
    phase = np.random.uniform(0,2*np.pi, num_of_samples)

    # Combine amplitude and phase to form complex coefficients
    h_ba= magnitude * np.exp(1j * phase) 

    # Generate Gaussian-distributed channel-indipendent measurement error at Bob
    eps_ab = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_ae = np.random.normal(loc=0, scale=1, size=num_of_samples)
    eps_be = np.random.normal(loc=0, scale=1, size=num_of_samples)

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

def compute_all_index_in_common(rho_ab_ba, rho_ab_ae, rho_ba_be,delta_max_bob,delta_min_bob):
    # Initialize lists to store all common index value between (alice and bob), (alice and eve) and (bob and eve)
    all_common_values_ab_ba = []
    all_common_values_ab_ae = []
    all_common_values_ba_be = []

    # Initialize list to store how many times h_ab.issubest(h_ba)
    all_times_ab_subset_ba = []
    
    for _ in range(iterations):
            
        channel_coefficients = generate_channel_coefficients(rho_ab_ba,rho_ab_ae,rho_ba_be)
       
        # Compute the Rayleigh coefficients from Bob's POV (Bob to Alice and vice versa)
        h_ba = channel_coefficients.get("h_ba")
        h_ab = channel_coefficients.get("h_ab")

        # Compute the Rayleigh coefficients from Eve's POV (Alice to Eve and Bob to Eve)
        h_ae = channel_coefficients.get("h_ae")
        h_be = channel_coefficients.get("h_be")


        # Make a quantization by index for all channels
        index_quantization_list_ba = set(index_quantization(h_ba.real,delta_max_alice,delta_min_alice))
        index_quantization_list_ab = set(index_quantization(h_ab.real,delta_max_bob,delta_min_bob))
        index_quantization_list_be = set(index_quantization(h_be.real,delta_max_bob,delta_min_bob))
        index_quantization_list_ae = set(index_quantization(h_ae.real,delta_max_bob,delta_min_bob))

        #Plot channel coefficient probes 
        #plot_channel_coefficients(h_ab,h_ba,h_be,get_max(h_ba,delta_max_alice),get_min(h_ba,delta_max_alice,delta_min_alice),get_max(h_ab,delta_max_bob),get_min(h_ab,delta_max_bob,delta_min_bob),get_max(h_be,delta_max_bob),get_min(h_ba,delta_max_bob,delta_min_alice))

        # compute how many times ab is subset of ba
        all_times_ab_subset_ba.append(index_quantization_list_ab.issubset(index_quantization_list_ba))

        
        # Save the all common values only if ab is subset of ba the other cases are not considered
        if(set(index_quantization_list_ab).issubset(set(index_quantization_list_ba))):
            all_common_values_ab_ba.append(len(index_quantization_list_ab))
            all_common_values_ab_ae.append(len(index_quantization_list_ae.intersection(index_quantization_list_ba)))
            all_common_values_ba_be.append(len(index_quantization_list_be.intersection(index_quantization_list_ba)))
    
    return {
        "all_times_ab_subset_ba" : all_times_ab_subset_ba,
        "all_common_values_ab_ba": all_common_values_ab_ba,
        "all_common_values_ab_ae": all_common_values_ab_ae,
        "all_common_values_ba_be": all_common_values_ba_be
    }

