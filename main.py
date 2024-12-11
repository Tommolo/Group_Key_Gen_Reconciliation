import numpy as np
import matplotlib.pyplot as plt
from generate_channel_coefficients import *
from quantization_by_index import *
from utils import *
from plots import *


# Number of iterations
num_of_samples = [10, 20, 40, 80, 160, 320, 640, 1280]


# Generate channel coefficients
channel_coefficients = generate_channel_coefficients(num_of_samples[4])

h_ab = channel_coefficients.get("h_ab")
h_ba = channel_coefficients.get("h_ba")
h_ae = channel_coefficients.get("h_ae")


# Ensure h_ab and h_ba are numpy arrays or lists
real_part_ab = h_ab.real
imaginary_part_ab = h_ab.imag
h_ab = np.concatenate((real_part_ab, imaginary_part_ab))  # Convert to numpy array


real_part_ba = h_ba.real
imaginary_part_ba = h_ba.imag
h_ba = np.concatenate((real_part_ba, imaginary_part_ba))   # Convert to numpy array

real_part_ae = h_ae.real
imaginary_part_ae = h_ae.imag
h_ae = np.concatenate((real_part_ae, imaginary_part_ae)) 

dict_alpha_indexes_alice = get_dict_alpha_indexes(h_ba)
#adjusting_alpha_value(h_ba,min_index_a,max_index_a)
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

