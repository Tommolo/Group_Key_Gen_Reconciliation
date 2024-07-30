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

iterations = data['simulation_parameters']['iterations']
num_dec_values = data['simulation_parameters']['num_dec_values']

delta_max_alice = 0
delta_min_alice = 3

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

#Create set of indexes of quantization for ab, ba, ae,be
def make_quantization_for_channel_coefficient(num_of_samples,rho_ab_ba, rho_ab_ae, rho_ba_be,delta_max_bob,delta_min_bob):
    
    channel_coefficients = generate_channel_coefficients(num_of_samples,rho_ab_ba,rho_ab_ae,rho_ba_be)
       
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
                
    return {
        "index_quantization_list_ba": index_quantization_list_ba,
        "index_quantization_list_ab": index_quantization_list_ab,
        "index_quantization_list_be": index_quantization_list_be,
        "index_quantization_list_ae": index_quantization_list_ae,
    }


def statistical_analysis_over_n_iterations(num_of_samples,rho_ab_ba, rho_ab_ae, rho_ba_be,delta_max_bob,delta_min_bob):
     # compute how many times ab is subset of ba
     # Number of element set ab quantized when ab is subset of ba
    length_set_ab = []



    #Similarity of indexes

    similarity_of_indexes_alice_eve =[]
    similarity_of_indexes_alice_bob =[]

    #all number of noisy values over n iterations
    all_noisy_values=[]
    
    for _ in range(iterations):

        quantization_channel_coefficient = make_quantization_for_channel_coefficient(num_of_samples,rho_ab_ba, rho_ab_ae, rho_ba_be,delta_max_bob,delta_min_bob)
        
        #The set of noisy values is the set of all values discarded during the quantization
        noisy_values=set(list(range(0,num_of_samples-1))) - quantization_channel_coefficient.get("index_quantization_list_ba")
        #Append the len of noisy values
        all_noisy_values.append(len(noisy_values))
           
        S_I_ae = len((quantization_channel_coefficient.get("index_quantization_list_ba").intersection(quantization_channel_coefficient.get("index_quantization_list_be"))))/len(quantization_channel_coefficient.get("index_quantization_list_be"))
        S_I_ab = len((quantization_channel_coefficient.get("index_quantization_list_ba").intersection(quantization_channel_coefficient.get("index_quantization_list_ab"))))/len(quantization_channel_coefficient.get("index_quantization_list_ab"))
    

        similarity_of_indexes_alice_eve.append(S_I_ae)
        similarity_of_indexes_alice_bob.append(S_I_ab)
            
        print("SI_ae",similarity_of_indexes_alice_eve)
        print("SI_ab",similarity_of_indexes_alice_bob)
        length_set_ab.append(len(quantization_channel_coefficient.get("index_quantization_list_ab")))


    return{

            "all_noisy_values"  : all_noisy_values,

            "length_set_ab": length_set_ab,

            "similarity_of_indexes_alice_eve" : similarity_of_indexes_alice_eve,

            "similarity_of_indexes_alice_bob" : similarity_of_indexes_alice_bob    
    }