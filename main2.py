import numpy as np
import matplotlib.pyplot as plt
from generate_channel_coefficients import *
from quantization_by_index import *
from utils import *
from plots import *

num_of_iterations= 100
num_of_samples = [10, 20, 40, 80, 160, 320, 640, 1280]

dict_alpha_SIs_ab={}
dict_alpha_SIs_ae={}


dict_alpha_probability_SI_equalto1_ab ={}
dict_alpha_probability_SI_equalto1_ae = {}

#P[SI=1] over n iterations#

for _ in range(num_of_iterations):
    # Generate channel coefficients
    channel_coefficients = generate_channel_coefficients(num_of_samples[4])

    h_ab = channel_coefficients.get("h_ab")
    h_ba = channel_coefficients.get("h_ba")
    h_ae = channel_coefficients.get("h_ae")

    half_length = len(h_ba) // 2

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
    dict_alpha_indexes_bob = get_dict_alpha_indexes(h_ab)
    dict_alpha_indexes_eve = get_dict_alpha_indexes(h_ae)

    dict_alphas_SI_ab = get_dict_alphas_SI(dict_alpha_indexes_alice,dict_alpha_indexes_bob)
    dict_alphas_SI_ae = get_dict_alphas_SI(dict_alpha_indexes_alice,dict_alpha_indexes_eve)

    get_dict_alpha_SIs(dict_alpha_SIs_ab,dict_alphas_SI_ab)
    get_dict_alpha_SIs(dict_alpha_SIs_ae,dict_alphas_SI_ae)

for alpha in dict_alpha_SIs_ab.keys():
    pr_si_1 = (dict_alpha_SIs_ab.get(alpha).count(1))/num_of_iterations
    dict_alpha_probability_SI_equalto1_ab[alpha]=pr_si_1

for alpha in dict_alpha_SIs_ae.keys():
    pr_si_1 = (dict_alpha_SIs_ae.get(alpha).count(1))/num_of_iterations
    dict_alpha_probability_SI_equalto1_ae[alpha]=pr_si_1


print(dict_alpha_probability_SI_equalto1_ab)

print(dict_alpha_probability_SI_equalto1_ae)


get_heatmap_alphas_SI(dict_alpha_probability_SI_equalto1_ab,"pr_ab")
get_heatmap_alphas_SI(dict_alpha_probability_SI_equalto1_ae,"pr_ae")

    

    



