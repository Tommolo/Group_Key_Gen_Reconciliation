import numpy as np
from all_common_values import *
from probability import *
from other_methods import *
from plots import *

# Correlation coefficients
rho_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.97]

# Initialize an empty list to store the probabilities
all_probabilities_ab_subset_ba = []

delta_max_bob_range = np.arange(0,1.1,0.1)
similarity_of_indexes_ab_mean = []
similarity_of_indexes_ae_mean = []

delta_min=0
delta_max_min=[]

average_of_noisy_values = []

num_of_samples=[200,300,400,500,600,700,800,900,1000]

delta_max_min_pr_1=[]


# Loop through different values of delta_max and delta_min_bob
for delta_max in delta_max_bob_range:
        delta_min +=0.5
        statistycal_analysis = statistical_analysis_over_n_iterations(num_of_samples[0],rho_list[9], rho_list[0], rho_list[0], delta_max, delta_min)
        delta_max_min.append("("+ str(np.round(delta_max,2)) + "," + str(np.round(delta_min,2))+ ")")
        similarity_of_indexes_ab_mean.append(np.mean(statistycal_analysis.get("similarity_of_indexes_alice_bob")))
        similarity_of_indexes_ae_mean.append(np.mean(statistycal_analysis.get("similarity_of_indexes_alice_eve")))

# Compute common values with fixed Alice and eve rho=0.1
delta_max_bob=1
delta_min_bob=5.5

genuine_points=[]


#number of genuine points when SI=1 but number of samples change.
for samples in num_of_samples:
        statistical_analysis = make_quantization_for_channel_coefficient(samples,rho_list[9], rho_list[0], rho_list[0],delta_max_bob,delta_min_bob)
        genuine_points.append(len(statistical_analysis.get("index_quantization_list_ab")))

#plot_of_values_Eve_different_distance(all_common_values_mean_different_distances,distances_string)
#plot_of_values_Eve_different_rho(rho_list,all_common_values_mean_different_rho)
#plot_common_values_histogram(common_vals["all_common_values_ab_ba"],common_vals["all_common_values_ba_be"])
#plot_probabilities_noise_values(probabilities_noise_values,thresholds)
#plot_probability_distribution(sorted_lengths_intersection_ab_ba,sorted_probs_intersection_ab_ba,sorted_lengths_intersection_ba_be,sorted_probs_intersection_ba_be)
#plot_success_probability_graph(alice_dictionary,eve_dictionary)
#plot_noisy_values_ab_subset_ba_num_of_samples_changes(num_of_samples,average_of_noisy_values)
plot_similarity_of_indexes_guard_band_change(delta_max_min,similarity_of_indexes_ab_mean,similarity_of_indexes_ae_mean)
plot_genuine_points_different_channel_coefficients(num_of_samples,genuine_points)



