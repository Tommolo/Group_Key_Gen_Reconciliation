import matplotlib.pyplot as plt
import numpy as np


# Plot the success probability graph
def plot_success_probability_graph(alice_dictionary, eve_dictionary):

    plt.figure(figsize=(10, 6))
    plt.plot(list(alice_dictionary.keys()), list(alice_dictionary.values()), marker='o', linestyle='-', color='b', label='B2A')
    plt.plot(list(eve_dictionary.keys()), list(eve_dictionary.values()), marker='^', linestyle='-', color='r', label='B2E')
    plt.legend()
    plt.title('Probability Graph')
    plt.xlabel('Polynomial degree')
    plt.ylabel('Success Probability')
    plt.grid(True)
    plt.show()

# Plot the success probability graph
def plot_channel_coefficients(h_ab, h_ba, h_be, maximum_ba, minimum_ba,maximum_ab,minimum_ab,maximum_be,minimum_be):
    plt.figure(figsize=(10, 6))
    plt.plot(h_ab.real, marker='o', linestyle='-', color='b', label='h_ab')
    plt.plot(h_ba.real, marker='^', linestyle='-', color='g', label='h_ba')
    plt.plot(h_be.real, marker='^', linestyle='-', color='r', label='h_be')

    plt.axhline(maximum_ba.real, color='g', linestyle='--')
    plt.axhline(minimum_ba.real, color='g', linestyle='--')

    plt.axhline(maximum_ab.real, color='b', linestyle='--')
    plt.axhline(minimum_ab.real, color='b', linestyle='--')

    plt.axhline(maximum_be.real, color='r', linestyle='--')
    plt.axhline(minimum_be.real, color='r', linestyle='--')

    plt.legend()
    plt.title('Channel coefficient')
    plt.xlabel('Index')
    plt.ylabel('channel coefficients')
    plt.grid(True)
    plt.show()


# Plot histogram of common values Alice and Bob
def plot_common_values_histogram(all_common_values_ab_ba, all_common_values_ab_ae):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(all_common_values_ab_ba, bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title('Histogram of common values for Alice and Bob')
    plt.xlabel('Number of common values')
    plt.ylabel('Frequency')

    # Plot histogram of common values Alice and Eve
    plt.subplot(1, 2, 2)
    plt.hist(all_common_values_ab_ae, bins=20, color='red', alpha=0.7, edgecolor='black')
    plt.title('Histogram of common values for Alice and Eve')
    plt.xlabel('Number of common values')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()


def plot_probability_distribution(sorted_lengths_intersection_ab_ba, sorted_probs_intersection_ab_ba,
                                  sorted_lengths_intersection_ab_ae, sorted_probs_intersection_ab_ae):
    # Plot histogram of the probability distribution function of common values for Alice and Bob
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.bar(sorted_lengths_intersection_ab_ba, sorted_probs_intersection_ab_ba, color='skyblue', edgecolor='black')
    plt.xlabel('Common values')
    plt.ylabel('Probability')
    plt.title('Probability Distribution for Alice and Bob intersection')
    plt.grid(True)

    # Plot histogram of the probability distribution function of common values for Alice and Eve
    plt.subplot(1, 2, 2)
    plt.bar(sorted_lengths_intersection_ab_ae, sorted_probs_intersection_ab_ae, color='salmon', edgecolor='black')
    plt.xlabel('Common values')
    plt.ylabel('Probability')
    plt.title('Probability Distribution for Alice and Eve intersection')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def plot_ab_subset_ba_length_guard_band_change(delta_max_min,all_probabilities_ab_subset_ba):

    # Plotting
    plt.figure(figsize=(8, 6))  # Adjust figure size as needed
    plt.plot(delta_max_min, all_probabilities_ab_subset_ba, color='blue', marker='o', linestyle='-')
    # Adding labels and title
    plt.xlabel('Delta')
    plt.ylabel('Probabilities')
    plt.title('AB set is subset BA guard band value changing')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
