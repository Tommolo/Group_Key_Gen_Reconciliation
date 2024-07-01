import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt


def generate_nakagami_m_channel(num_measurements, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=Omega, size=num_measurements)
    return magnitudes

# Example parameters
num_measurements = 128
m = 3  # Shape parameter (typically m >= 0.5)

Omega_alice = 1  # Scale parameter (mean power) for Alice
Omega_eve = 2 # Scale parameter (mean power) for Eve

rho = 0.97  # Example correlation coefficient

iterations = 1000
all_common_values_ab_ba = []
all_common_values_ba_ae = []

for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_measurements, m, Omega_alice)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_measurements, m, Omega_eve)

    eps = np.random.normal(loc=0, scale=1, size=num_measurements)

    # Compute the cross-correlation
    h_ab = rho * h_ba + (1 - rho**2 * eps)**1/2  # Update h_ab

    # Store the first two decimal values
    h_ab = np.round(h_ab, 2)
    h_ba = np.round(h_ba, 2)
    h_ae = np.round(h_ae, 2)

    # Convert to sets
    set_ab = set(h_ab)
    set_ba = set(h_ba)
    set_ae = set(h_ae)

    # Calculate intersections
    common_values_ba_ab = set_ba.intersection(set_ab)
    common_values_ba_ae = set_ba.intersection(set_ae)

    # Store length of intersections the length=number_of_common_values
    all_common_values_ab_ba.append(len(common_values_ba_ab))
    all_common_values_ba_ae.append(len(common_values_ba_ae))


#  Create a dictionary common_value:probability
def compute_frequency_and_probability(list):
    prob_dictionary = {}
    length_list = len(list)  

    for value in sorted(list):
        if value not in prob_dictionary:
            frequency = list.count(value) # count number of times this value is in the list
            probability = frequency / length_list 
            prob_dictionary[value] = probability
            
    return prob_dictionary

probability_of_success = []
dictionary_value_probability_alice = compute_frequency_and_probability(all_common_values_ab_ba)
dictionary_value_probability_eve = compute_frequency_and_probability(all_common_values_ba_ae)


# We consider the success probability the capability to reconstruct a polynomial of grade k 
def compute_success_probability(dictionary, list):
    new_dictionary = {}
    
    # Sort the keys of the dictionary for safety
    sorted_keys = sorted(dictionary.keys())
    
    for l in list:
        probability_sum = 0
        for key in sorted_keys:
            if l > key:
                probability_sum += dictionary[key]
        new_dictionary[l] = 1 - probability_sum
    
    return new_dictionary

alice_dictionary = compute_success_probability(dictionary_value_probability_alice, list(range(2, 100)))
eve_dictionary = compute_success_probability(dictionary_value_probability_eve, list(range(2, 100)))

# Transform number of points (k) in degree of polynomial (k-1)
def transform_in_degree(dictionary):
    new_dictionary = {}
    
    for key in dictionary:
        new_key = key - 1
        new_dictionary[new_key] = dictionary[key]
    
    return new_dictionary

alice_dictionary = transform_in_degree(alice_dictionary) 
eve_dictionary = transform_in_degree(eve_dictionary)

print(alice_dictionary)
print(eve_dictionary)

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.plot(alice_dictionary.keys(), alice_dictionary.values(), marker='o', linestyle='-', color='b')
plt.plot(eve_dictionary.keys(), eve_dictionary.values(), marker='^', linestyle='-', color='r')
plt.title('Probability Graph')
plt.xlabel('Polynomial degree')
plt.ylabel('Success Probability')
plt.grid(True)
plt.show()
