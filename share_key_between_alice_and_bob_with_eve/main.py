import numpy as np
from share_key_between_alice_and_bob_with_eve.all_common_values import *
from share_key_between_alice_and_bob_with_eve.probability import *
from share_key_between_alice_and_bob_with_eve.other_methods import *
from share_key_between_alice_and_bob_with_eve.plots import *

# Distances in meters
d_ab = 1 # Distance between Alice and Bob
distances = [d_ab,2*d_ab,3*d_ab,4*d_ab]

# Correlation coefficients
rho_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


all_common_values_mean_different_distances=[]
#Compute all_common_values for each link when distance changes
for dist in distances:
    common_values = compute_rss_common_values(rho_list[8], rho_list[0], rho_list[0], d_ab, dist, dist).get("all_common_values_ba_ae")
    all_common_values_mean_different_distances.append(np.mean(common_values))


all_common_values_mean_different_rho=[]
#Compute all_common_values for each link when rho changes but distance is fixed
for rho in rho_list:
    common_values = compute_rss_common_values(rho_list[8], rho, rho, d_ab, distances[3], distances[3] ).get("all_common_values_ba_ae")
    all_common_values_mean_different_rho.append(np.mean(common_values))


# Compute rss values with fixed distance and fixed rho=0.1
common_vals = compute_rss_common_values(rho_list[8], rho_list[0], rho_list[0], d_ab, distances[0], distances[0])

# Compute the probabilities for each common value lists
probs = calculate_probabilities(
    common_vals["all_common_values_ab_ba"],
    common_vals["all_common_values_ba_ae"],
    common_vals["all_common_values_ba_be"]
)

# Unpack the probabilities
prob_intersection_ab_ba = probs["prob_intersection_ab_ba"]
prob_intersection_ba_ae = probs["prob_intersection_ba_ae"]
prob_intersection_ba_be = probs["prob_intersection_ba_be"]


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

#plot_of_values_Eve_different_distance(distances,all_common_values_mean_different_distances)
plot_of_values_Eve_different_rho(rho_list,all_common_values_mean_different_rho)
#plot_common_values_histogram(all_common_values_ab_ba,all_common_values_ba_ae)
#plot_probability_distribution(sorted_lengths_intersection_ab_ba,sorted_probs_intersection_ab_ba,sorted_lengths_intersection_ba_ae,sorted_probs_intersection_ba_ae)
#plot_success_probability_graph(alice_dictionary,eve_dictionary)




