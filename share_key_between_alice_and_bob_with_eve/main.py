from generate_channel_coefficients import generate_channel_coefficients
import numpy as np
import matplotlib.pyplot as plt
from quantization_by_index import *
from utils import *
from plots import *


# Number of iterations
num_iterations = 1
num_of_samples = [10,20,50,100,200,500,1000,2000,5000,8000]
num_of_levels = 6
count_subset = 0


set_ab_length=[]
SI_list_ab = []
SI_list_be = []
rho_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
pr_si_1_ab=[]
pr_si_1_be=[]
pr_setB_greater_than_32 = []

# Generate channel coefficients
channel_coefficients = generate_channel_coefficients(num_of_samples[2], rho_list[8], rho_list[0], rho_list[0])

h_ab = channel_coefficients.get("h_ab")
h_ba = channel_coefficients.get("h_ba")
h_be = channel_coefficients.get("h_be")

# Ensure h_ab and h_ba are numpy arrays or lists
h_ab = np.array(h_ab.real)  # Convert to numpy array
h_ba = np.array(h_ba.real)  # Convert to numpy array
h_be = np.array(h_be.real) 


indexes_A,alpha_A,min_index_A,max_index_A = get_indexes_according_to_alpha_Alice_value(h_ba)
indexes_B,alpha_B,min_index_B,max_index_B= get_indexes_according_to_alpha_Bob_value(h_ab)
indexes_E,alpha_E,min_index_E,max_index_E = get_indexes_according_to_alpha_Bob_value(h_be)

print(f"indexes_Alice: {indexes_A}")
print(f"indexes_Bob: {indexes_B}")
print(f"indexes_Eve: {indexes_E}")

print(f"Alpha_A: {alpha_A}")
print(f"Alpha_B: {alpha_B}")
print(f"Alpha_E: {alpha_E}")

si_ab = compute_si_ab(indexes_A,indexes_B,SI_list_ab,set_ab_length)
print("SI_AB",si_ab)

si_be = compute_si_be(indexes_A,indexes_E,SI_list_be)
print ("SI_BE",si_be)

#Plot channel coefficients 
quantization_plot(h_ba,h_ab,h_be,min_index_A,max_index_A,min_index_B,max_index_B,min_index_E,max_index_E)
all_levels_of_quantization (h_ba)


