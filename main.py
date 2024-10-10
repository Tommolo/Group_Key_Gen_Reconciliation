import numpy as np
import matplotlib.pyplot as plt
from generate_channel_coefficients import *
from quantization_by_index import *
from utils import *
from plots import *


# Number of iterations
num_of_samples = [10,20,50,100,200,320,1000,2000,5000,8000]

# Generate channel coefficients
channel_coefficients = generate_channel_coefficients(num_of_samples[5])

h_ab = channel_coefficients.get("h_ab")
h_ba = channel_coefficients.get("h_ba")
h_ae = channel_coefficients.get("h_ae")

# Ensure h_ab and h_ba are numpy arrays or lists
h_ab = np.array(h_ab.real)  # Convert to numpy array
h_ba = np.array(h_ba.real)  # Convert to numpy array
h_ae = np.array(h_ae.real) 

dict_alpha_indexes_alice = get_dict_alpha_indexes(h_ba)
dict_alpha_indexes_bob = get_dict_alpha_indexes(h_ab)
dict_alpha_indexes_eve = get_dict_alpha_indexes(h_ae)

dict_alphas_SI_ab = get_dict_alphas_SI(dict_alpha_indexes_alice,dict_alpha_indexes_bob)
dict_alphas_SI_ae = get_dict_alphas_SI(dict_alpha_indexes_alice,dict_alpha_indexes_eve)


#print(sorted(dict_alpha_indexes_alice.keys()))
#print(sorted(dict_alpha_indexes_bob.keys()))


#print(compute_si(dict_alpha_indexes_alice.get(0.4),dict_alpha_indexes_bob.get(0.05)))
#print(compute_si(dict_alpha_indexes_alice.get(0.4),dict_alpha_indexes_eve.get(0.05)))

#print("A_B",dict_alphas_SI_ab)
#print("A_E",dict_alphas_SI_ae)

get_heatmap_alphas_SI(dict_alphas_SI_ab,"ab")
get_heatmap_alphas_SI(dict_alphas_SI_ae,"ae")

