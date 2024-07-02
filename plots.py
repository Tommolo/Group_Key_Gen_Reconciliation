import matplotlib.pyplot as plt

def plot_success_probability_graph(alice_dictionary, eve_dictionary):
    # Plot the success probability graph
    plt.figure(figsize=(10, 6))
    plt.plot(list(alice_dictionary.keys()), list(alice_dictionary.values()), marker='o', linestyle='-', color='b', label='A2B')
    plt.plot(list(eve_dictionary.keys()), list(eve_dictionary.values()), marker='^', linestyle='-', color='r', label='A2E')
    plt.legend()
    plt.title('Probability Graph')
    plt.xlabel('Polynomial degree')
    plt.ylabel('Success Probability')
    plt.grid(True)
    plt.show()


def plot_common_values_histogram(all_common_values_ab_ba, all_common_values_ba_ae):
    # Plot histogram of common values Alice and Bob
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(all_common_values_ab_ba, bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title('Histogram of common values for Alice and Bob')
    plt.xlabel('Number of common values')
    plt.ylabel('Frequency')

    # Plot histogram of common values Alice and Eve
    plt.subplot(1, 2, 2)
    plt.hist(all_common_values_ba_ae, bins=20, color='red', alpha=0.7, edgecolor='black')
    plt.title('Histogram of common values for Alice and Eve')
    plt.xlabel('Number of common values')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()


def plot_probability_distribution(sorted_lengths_intersection_ab_ba, sorted_probs_intersection_ab_ba,
                                  sorted_lengths_intersection_ba_ae, sorted_probs_intersection_ba_ae):
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
    plt.bar(sorted_lengths_intersection_ba_ae, sorted_probs_intersection_ba_ae, color='salmon', edgecolor='black')
    plt.xlabel('Common values')
    plt.ylabel('Probability')
    plt.title('Probability Distribution for Alice and Eve intersection')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()