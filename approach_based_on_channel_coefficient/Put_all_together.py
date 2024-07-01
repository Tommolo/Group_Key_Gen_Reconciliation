import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt


import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt

def generate_nakagami_m_channel(num_probes, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=Omega, size=num_probes)
    return magnitudes

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
rho_Alice_Eve = 0.5
rho_Bob_Eve = 0.5

#number of iterations
iterations = 1000

all_common_values_ab_ba = []
all_common_values_ba_ae = []
all_common_values_ba_be = []

for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_of_probes, m, Omega)

    # Generate h_ae and h_be channel coefficients
    eps_ab = np.random.normal(loc=0, scale=1, size=num_of_probes)
    eps_ae = np.random.normal(loc=0, scale=1, size=num_of_probes)
    eps_be = np.random.normal(loc=0, scale=1, size=num_of_probes)

    # Compute the Nakagami coefficients from Bob's point of view (Bob to Alice and vice versa)
    h_ab = rho_Alice_Bob * h_ba + (1 - rho_Alice_Bob**2 * eps_ab)**1/2

    # Compute the Nakagami coefficients from Eve's point of view (Alice to Eve and Bob to Eve)
    h_ae = rho_Alice_Eve * h_ba + (1 - rho_Alice_Eve**2 * eps_ae)**1/2
    h_be = rho_Bob_Eve * h_ba + (1 - rho_Bob_Eve**2 * eps_be)**1/2

    # Compute RSS (Received Signal Strength) samples in dBm for Alice and Bob in dBm
    gamma_ba = 10 * np.log10((Pt * np.abs(h_ba)**2 * d_ab**-alpha) / noise_floor) + 30
    gamma_ab = 10 * np.log10((Pt * np.abs(h_ab)**2 * d_ab**-alpha) / noise_floor) + 30

    # Compute RSS samples in dBm for Alice and Eve and Bob and Eve in dBm
    gamma_ae = 10 * np.log10((Pt * np.abs(h_ae)**2 * d_ae**-alpha) /noise_floor) + 30
    gamma_be = 10 * np.log10((Pt * np.abs(h_be)**2 * d_be**-alpha) / noise_floor) + 30

    # Round the values to two decimal places if needed
    gamma_ab = np.round(gamma_ab, num_dec_values)
    gamma_ba = np.round(gamma_ba, num_dec_values)
    gamma_ae = np.round(gamma_ae, num_dec_values)
    gamma_be = np.round(gamma_be, num_dec_values)

    print("Gamma_AB (dBm):", np.sort(gamma_ab))
    print("Gamma_BA (dBm):", np.sort(gamma_ba))
    print("Gamma_AE (dBm):", gamma_ae)
    print("Gamma_BE (dBm):", gamma_be)

    # Store the lengths of intersections
    all_common_values_ab_ba.append(len(set(gamma_ba).intersection(set(gamma_ab))))
    all_common_values_ba_ae.append(len(set(gamma_ba).intersection(set(gamma_ae))))
    all_common_values_ba_be.append(len(set(gamma_ba).intersection(set(gamma_be))))


# Calculate probabilities length as key and probabilty (number of elements/iterations) as value
prob_intersection = {length: all_common_values_ab_ba.count(length) / iterations for length in set(all_common_values_ab_ba)}
prob_intersection2 = {length: all_common_values_ba_ae.count(length) / iterations for length in set(all_common_values_ba_ae)}
prob_intersection3 = {length: all_common_values_ba_be.count(length) / iterations for length in set(all_common_values_ba_be)}

# Sort probabilities by length for plotting
sorted_lengths_intersection = sorted(prob_intersection.keys())
sorted_probs_intersection = [prob_intersection[length] for length in sorted_lengths_intersection]

sorted_lengths_intersection2 = sorted(prob_intersection2.keys())
sorted_probs_intersection2 = [prob_intersection2[length] for length in sorted_lengths_intersection2]

sorted_lengths_intersection3 = sorted(prob_intersection3.keys())
sorted_probs_intersection3 = [prob_intersection3[length] for length in sorted_lengths_intersection3]

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


def generate_random_excluding_range(start, end, exclude_start, exclude_end, precision=2):
    while True:
        value = round(np.random.uniform(start, end), precision)
        if not (exclude_start <= value <= exclude_end):
            return value



# Plot the histogram
plt.figure(figsize=(10, 6))
plt.plot(alice_dictionary.keys(), alice_dictionary.values(), marker='o', linestyle='-', color='b',label='A2B')
plt.plot(eve_dictionary.keys(), eve_dictionary.values(), marker='^', linestyle='-', color='r',label='A2E')
plt.legend()
plt.title('Probability Graph')
plt.xlabel('Polynomial degree')
plt.ylabel('Success Probability')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(all_common_values_ab_ba, bins=20, color='blue', alpha=0.7,edgecolor='black')
plt.title('Histogram of common values for Alice and Bob')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(all_common_values_ba_ae, bins=20, color='red', alpha=0.7, edgecolor='black')
plt.title('Histogram of common values for Alice and Eve')
plt.xlabel('Number of common values')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(sorted_lengths_intersection, sorted_probs_intersection, color='skyblue', edgecolor='black')
plt.xlabel('Common values')
plt.ylabel('Probability')
plt.title('Probability Distribution for Alice and Bob intersection')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(sorted_lengths_intersection2, sorted_probs_intersection2, color='salmon', edgecolor='black')
plt.xlabel('Common values')
plt.ylabel('Probability')
plt.title('Probability Distribution for Alice and Eve intersection')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot channel coefficient values
plt.figure(figsize=(10, 6))
plt.plot(gamma_ba, label='Alice', color='blue', marker='^')
plt.plot(gamma_ab, label='Bob', color='green', marker='x')
plt.plot(gamma_ae, label='Eve', color='red', marker='o')
plt.plot(gamma_be, label='Eve', color='black', marker='o')
plt.title('Rss channel probes')
plt.xlabel('Sample Index')
plt.ylabel('RSS samples')
plt.legend()
plt.grid(True)
plt.show()
