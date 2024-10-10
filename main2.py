import numpy as np
import matplotlib.pyplot as plt
from generate_channel_coefficients import *
from quantization_by_index import *
from utils import *
from plots import *


num_of_iterations=100
num_of_samples = [10,20,50,100,200,320,1000,2000,5000,8000]

dict_alpha_SIs_ab={}
dict_alpha_SIs_ae={}


dict_alpha_probability_SI_equalto1_ab ={}
dict_alpha_probability_SI_equalto1_ae = {}


for _ in range(num_of_iterations):
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

    

    



