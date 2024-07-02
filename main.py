import matplotlib.pyplot as plt
from all_common_values import *
from probability import *
from other_methods import *
from plots import *

# Simulation parameters
num_of_probes = 200 #the number of signal send from alice to bob and viceversa
m = 3  # Shape parameter (typically m >= 0.5)
Omega = 1  # Scale parameter (mean power)
Pt = 10 # Power in Watts 
alpha = 2  # Path loss exponent normally in the range 2-4
noise_floor = 4*10**-14 # Noise floor in watts
num_dec_values = 2 # Number of the decimal values

# Distances in meters
d_ab = 1  # Distance between Alice and Bob
d_ae = 2  # Distance between Alice and Eve
d_be = 2 # Distance between Bob and Eve

# Correlation coefficients
rho_Alice_Bob = 0.97
rho_Alice_Eve = 0.1
rho_Bob_Eve = 0.1

#number of iterations
iterations = 1000

#Compute all_common_values for each link
all_common_values=compute_rss_common_values(iterations,num_of_probes,m,Omega,rho_Alice_Bob,rho_Alice_Eve,rho_Bob_Eve,Pt,d_ab,d_ae,d_be,alpha,noise_floor,num_dec_values)

# construct all common values for each link
all_common_values_ab_ba = all_common_values.get("all_common_values_ab_ba")
all_common_values_ba_ae = all_common_values.get("all_common_values_ba_ae")
all_common_values_ba_be = all_common_values.get("all_common_values_ba_be")

#Compute the probabilities
probabilities = calculate_probabilities(all_common_values_ab_ba,all_common_values_ba_ae,all_common_values_ba_be)
prob_intersection_ab_ba = probabilities.get("prob_intersection_ab_ba")
prob_intersection_ba_ae = probabilities.get("prob_intersection_ba_ae")
prob_intersection_ba_be = probabilities.get("prob_intersection_ba_be")


#Compute sorted probabilities
sorted_probabilities= sort_probabilities(prob_intersection_ab_ba,prob_intersection_ba_ae,prob_intersection_ba_be)

sorted_lengths_intersection_ab_ba = sorted_probabilities.get("sorted_lengths_intersection_ab_ba")
sorted_probs_intersection_ab_ba = sorted_probabilities.get("sorted_probs_intersection_ab_ba")

sorted_lengths_intersection_ba_ae = sorted_probabilities.get("sorted_lengths_intersection_ba_ae")
sorted_probs_intersection_ba_ae = sorted_probabilities.get("sorted_probs_intersection_ba_ae")

sorted_lengths_intersection_ba_be = sorted_probabilities.get("sorted_lengths_intersection_ba_be")
sorted_probs_intersection_ba_be = sorted_probabilities.get("sorted_probs_intersection_ba_be")


#Create dictionary for alice and eve
dictionary_value_probability_alice = compute_frequency_and_probability(all_common_values_ab_ba)
dictionary_value_probability_eve = compute_frequency_and_probability(all_common_values_ba_ae)

# Compute success probability for alice and eve
alice_dictionary = compute_success_probability(dictionary_value_probability_alice, list(range(2, 100)))
eve_dictionary = compute_success_probability(dictionary_value_probability_eve, list(range(2, 100)))

alice_dictionary = transform_in_degree(alice_dictionary) 
eve_dictionary = transform_in_degree(eve_dictionary)

print(alice_dictionary)
print(eve_dictionary)

plot_common_values_histogram(all_common_values_ab_ba,all_common_values_ba_ae)
plot_probability_distribution(sorted_lengths_intersection_ab_ba,sorted_probs_intersection_ab_ba,sorted_lengths_intersection_ba_ae,sorted_probs_intersection_ba_ae)
plot_success_probability_graph(alice_dictionary,eve_dictionary)


