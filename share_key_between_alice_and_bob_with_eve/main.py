import numpy as np
from all_common_values import *
from probability import *
from other_methods import *
from plots import *

# Correlation coefficients
rho_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.97]

# Initialize an empty list to store the probabilities
all_probabilities_ab_subset_ba = []

delta_max_bob_range = np.arange(0,2,0.1)
number_of_genuine_points = []
delta_min=0
delta_max_min=[]

# Loop through different values of delta_max and delta_min_bob
for delta_max in delta_max_bob_range:
        delta_min +=0.5
        all_time_ab_subset_ba = compute_all_index_in_common(rho_list[9], rho_list[0], rho_list[0], delta_max, delta_min)
        probability = probability_ab_subset_ba(all_time_ab_subset_ba.get("all_times_ab_subset_ba"))
        delta_max_min.append("("+ str(np.round(delta_max,2)) + "," + str(np.round(delta_min,2))+ ")")
        all_probabilities_ab_subset_ba.append(probability)

  
              
print(number_of_genuine_points)

delta_max_bob = 1
delta_min_bob = 3

# Compute common values with fixed Alice and eve rho=0.1
common_vals = compute_all_index_in_common(rho_list[9], rho_list[0], rho_list[0],delta_max_bob,delta_min_bob)

# Compute the probabilities for each common value list
probs = calculate_probabilities(
    common_vals["all_common_values_ab_ba"],
    common_vals["all_common_values_ab_ae"],
    common_vals["all_common_values_ba_be"]
)

# Unpack the probabilities
prob_intersection_ab_ba = probs["prob_intersection_ab_ba"]
prob_intersection_ab_ae = probs["prob_intersection_ab_ae"]
prob_intersection_ba_be = probs["prob_intersection_ba_be"]

#Compute sorted probabilities
sorted_probabilities= sort_probabilities(prob_intersection_ab_ba,prob_intersection_ab_ae,prob_intersection_ba_be)

sorted_lengths_intersection_ab_ba = sorted_probabilities.get("sorted_lengths_intersection_ab_ba")
sorted_probs_intersection_ab_ba = sorted_probabilities.get("sorted_probs_intersection_ab_ba")

sorted_lengths_intersection_ab_ae = sorted_probabilities.get("sorted_lengths_intersection_ab_ae")
sorted_probs_intersection_ab_ae = sorted_probabilities.get("sorted_probs_intersection_ab_ae")

sorted_lengths_intersection_ba_be = sorted_probabilities.get("sorted_lengths_intersection_ba_be")
sorted_probs_intersection_ba_be = sorted_probabilities.get("sorted_probs_intersection_ba_be")


#Create dictionary for alice and eve
dictionary_value_probability_alice = compute_frequency_and_probability(common_vals["all_common_values_ab_ba"])
dictionary_value_probability_eve = compute_frequency_and_probability(common_vals["all_common_values_ba_be"])

# Compute success probability for alice and eve
alice_dictionary = compute_success_probability(dictionary_value_probability_alice, list(range(2, 100)))
eve_dictionary = compute_success_probability(dictionary_value_probability_eve, list(range(2, 100)))

alice_dictionary = transform_in_degree(alice_dictionary) 
eve_dictionary = transform_in_degree(eve_dictionary)

print(alice_dictionary)
print(eve_dictionary)

#plot_of_values_Eve_different_distance(all_common_values_mean_different_distances,distances_string)
#plot_of_values_Eve_different_rho(rho_list,all_common_values_mean_different_rho)
#plot_common_values_histogram(common_vals["all_common_values_ab_ba"],common_vals["all_common_values_ba_be"])
#plot_probabilities_noise_values(probabilities_noise_values,thresholds)
#plot_probability_distribution(sorted_lengths_intersection_ab_ba,sorted_probs_intersection_ab_ba,sorted_lengths_intersection_ba_be,sorted_probs_intersection_ba_be)
print(probability_ab_subset_ba(common_vals["all_times_ab_subset_ba"]))
#plot_success_probability_graph(alice_dictionary,eve_dictionary)
plot_ab_subset_ba_length_guard_band_change(delta_max_min,all_probabilities_ab_subset_ba)




