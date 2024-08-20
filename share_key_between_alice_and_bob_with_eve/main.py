from generate_channel_coefficients import generate_channel_coefficients
import numpy as np
import matplotlib.pyplot as plt
from quantization_by_index import *
from other_methods import *
from plots import *


# Number of iterations
num_iterations = 100
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




for rho in rho_list:
    for _ in range(num_iterations):
        # Generate channel coefficients
        channel_coefficients = generate_channel_coefficients(num_of_samples[3], rho, rho_list[0], rho_list[0])

        h_ab = channel_coefficients.get("h_ab")
        h_ba = channel_coefficients.get("h_ba")
        h_be = channel_coefficients.get("h_be")

        # Ensure h_ab and h_ba are numpy arrays or lists
        h_ab = np.array(h_ab.real)  # Convert to numpy array
        h_ba = np.array(h_ba.real)  # Convert to numpy array
        h_be = np.array(h_be.real) 
        # Determine the minimum and maximum values of the array
        min_val_ba = h_ba.min()
        max_val_ba = h_ba.max()

        min_val_ab = h_ab.min()
        max_val_ab = h_ab.max()

        min_val_be = h_be.min()
        max_val_be = h_be.max()

        # Calculate the quantization intervals
        quantization_intervals_ba = np.linspace(min_val_ba, max_val_ba, num_of_levels)
        quantization_intervals_ab = np.linspace(min_val_ab, max_val_ab, num_of_levels)
        quantization_intervals_be = np.linspace(min_val_be, max_val_be, num_of_levels)


        indexes_ba = quantization_by_indexes_alice(h_ba,quantization_intervals_ba)
        indexes_ab = quantization_by_indexes_bob(h_ab,quantization_intervals_ab)
        indexes_be = quantization_by_indexes_bob(h_be,quantization_intervals_be)

        print(indexes_ba,len(indexes_ba))
        print(indexes_ab)
        print(indexes_be)

        SI_ab = compute_si_ab(indexes_ba,indexes_ab,SI_list_ab,set_ab_length)
        SI_be = compute_si_be(indexes_be,indexes_ba,SI_list_be)


    Pr_si_ab_1=SI_list_ab.count(1)/num_iterations
    pr_si_1_ab.append(Pr_si_ab_1)
    
    Pr_si_be_1=SI_list_be.count(1)/num_iterations

    print("SI_ab",SI_ab)
    print("SI_be",SI_be)
    print("Pr(SI_ab=1)",Pr_si_ab_1)
    print("Pr(SI_be=1)",Pr_si_be_1)
    print("Pr(SI=1) when rho change",pr_si_1_ab)

    count_when_is_greater_than_32 = len([num for num in set_ab_length if num >= 32])

    print("Pr(|setB|>=32)",count_when_is_greater_than_32/num_iterations)
    SI_list_ab.clear()
    SI_list_be.clear()
    set_ab_length.clear()

for samples in num_of_samples:
    for _ in range(num_iterations):
        # Generate channel coefficients
        channel_coefficients = generate_channel_coefficients(samples, 0.9, 0.1, 0.1)

        h_ab = channel_coefficients.get("h_ab")
        h_ba = channel_coefficients.get("h_ba")
        h_be = channel_coefficients.get("h_be")

        # Ensure h_ab and h_ba are numpy arrays or lists
        h_ab = np.array(h_ab.real)  # Convert to numpy array
        h_ba = np.array(h_ba.real)  # Convert to numpy array
        h_be = np.array(h_be.real) 
        # Determine the minimum and maximum values of the array
        min_val_ba = h_ba.min()
        max_val_ba = h_ba.max()

        min_val_ab = h_ab.min()
        max_val_ab = h_ab.max()

        min_val_be = h_be.min()
        max_val_be = h_be.max()

        # Calculate the quantization intervals
        quantization_intervals_ba = np.linspace(min_val_ba, max_val_ba, num_of_levels)
        quantization_intervals_ab = np.linspace(min_val_ab, max_val_ab, num_of_levels)
        quantization_intervals_be = np.linspace(min_val_be, max_val_be, num_of_levels)


        indexes_ba = quantization_by_indexes_alice(h_ba,quantization_intervals_ba)
        indexes_ab = quantization_by_indexes_bob(h_ab,quantization_intervals_ab)
        indexes_be = quantization_by_indexes_bob(h_be,quantization_intervals_be)

        print(indexes_ba,len(indexes_ba))
        print(indexes_ab)
        print(indexes_be)

        SI_ab = compute_si_ab(indexes_ba,indexes_ab,SI_list_ab,set_ab_length)
        SI_be = compute_si_be(indexes_be,indexes_ba,SI_list_be)


    Pr_si_ab_1=SI_list_ab.count(1)/num_iterations
   
    
    Pr_si_be_1=SI_list_be.count(1)/num_iterations
    pr_si_1_be.append(Pr_si_be_1)

    print("SI_ab",SI_ab)
    print("SI_be",SI_be)
    print("Pr(SI_ab=1)",Pr_si_ab_1)
    print("Pr(SI_be=1)",Pr_si_be_1)
    print("Pr(SI=1) when rho change",pr_si_1_ab)

    count_when_is_greater_than_32 = len([num for num in set_ab_length if num >= 32])
    Pr_setB_greater_than_32 = count_when_is_greater_than_32/num_iterations
    pr_setB_greater_than_32.append(Pr_setB_greater_than_32)

    print("Pr(|setB|>=32)",pr_setB_greater_than_32)
    
    SI_list_ab.clear()
    SI_list_be.clear()
    set_ab_length.clear()


#Plots:
plot_pr_si_1_when_rho_changes(rho_list,pr_si_1_ab)
plot_pr_si_1_when_num_samples_changes(num_of_samples,pr_si_1_be)
plot_pr_setB_is_greatereq_32(num_of_samples,pr_setB_greater_than_32)