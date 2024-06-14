import math
import numpy as np
import matplotlib.pyplot as plt
from pybloom_live import BloomFilter
import random
from scipy.stats import rice


def calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB):
    # Speed of light in m/s
    c = 3 * 10**8
    
    # Computation of wavelength
    wavelength_m = c / frequency_Hz
    
    # PathLoss
    path_loss = (4 * math.pi * distance_m / wavelength_m)**2
    path_loss_dB = 10 * math.log10(path_loss)
    
    # Computation RSSI without noise
    P_rx_dBm = P_tx_dBm - path_loss_dB + fading_dB
    
    # Gaussian noise
    noise_dB = np.random.normal(loc=0, scale=noise_std_dB)
    P_rx_dBm_with_noise = P_rx_dBm + noise_dB
    
    return round(P_rx_dBm_with_noise,2) #round(P_rx_dBm_with_noise,2) 

# Parameters
P_tx_dBm = 20        # Transmission power in dBm
distance_m = 10   # Distance
frequency_Hz = 2.4 * 10**9  # Frequency in Hz (2.4 GHz)
noise_std_dB = 2     # standard deviation in dB

# generation of fading for 100 signals
num_signals=128


# Generate Rician fading values
fading_dB_values_alice_bob =  np.random.normal(loc=-10, scale=2, size=num_signals)
fading_dB_values_adversary =  np.random.normal(loc=-10, scale=2, size=num_signals)



# RSSI with noise for node1 and node2
rssi_values_node1 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
rssi_values_node2 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
#rssi_values_adversary = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB)for fading_dB in fading_dB_values_adversary]

vocabularyA = []
vocabularyB = []


# Create Vocabulary for A
for i in range(0,len(rssi_values_node1)-1):
        vocabularyA.append(rssi_values_node1[i])

# create Vocabulary for B 
for i in range(0,len(rssi_values_node2)-1):
         vocabularyB.append(rssi_values_node2[i])

print("SetA: ", sorted(set(vocabularyA)), "Length: ", len(set(vocabularyA)))
print("SetB: ", sorted(set(vocabularyB)), "Length: ", len(set(vocabularyB)))


def generate_random_excluding_range(data_set, lower_bound, upper_bound, num_values):
    # Find min max in the set
    min_value = min(data_set) -2
    max_value = max(data_set) +2
    
    # Check if lower bound and upper bound are correct
    if lower_bound >= upper_bound:
        raise ValueError("The lower_bound must be less than the upper_bound")
    
    if min_value <= lower_bound or max_value >= upper_bound:
        raise ValueError("The range of the set must be within the range [lower_bound, upper_bound]")
    
    random_values = []
    
    while len(random_values) < num_values:
        rand_value = random.uniform(lower_bound, upper_bound)
        
        # Checks whether the random value is outside the range between min_value and max_value
        if rand_value < min_value or rand_value > max_value:
            random_values.append(round(rand_value,2))
    
    return random_values


# set parameters for random points generation
lower_bound = -100
upper_bound = -30
num_values =  100

chaff_points=set(generate_random_excluding_range(set(vocabularyA),lower_bound,upper_bound,num_values))


print("Chaff Points", chaff_points)

# create fuzzy-vault by union chaff points with point in setA
fuzzy_vault = chaff_points.union(set(vocabularyA))

print("Fuzzy Vault:", fuzzy_vault)

bloom_filter = BloomFilter(capacity=1000, error_rate=0.001)
for a in vocabularyA:
    bloom_filter.add(a)

common_values = []
for b in vocabularyB:
    if b in bloom_filter:
      common_values.append(b)

print ("Common values: ", sorted(set(common_values)),"Length: ", len(set(common_values)))


# B checks which values match with his own setB. The matches values are put into setR.
setR=[]
for element in fuzzy_vault:
     for value in set(vocabularyB):
          if (value==element):
               setR.append(value)

print("Matches:", sorted(setR),"Length: ",len(setR))



# Plot of balues for both nodes
plt.figure(figsize=(10, 6))
plt.plot(rssi_values_node1, label='Alice', marker='o')
plt.plot(rssi_values_node2, label='Bob', marker='x')
#plt.plot(rssi_values_adversary,label='Adversary ',color='red', marker='X')
plt.title('RSSi channel Probes')
plt.xlabel('Number of samples')
plt.ylabel('RSSI (dBm)')
plt.legend()
plt.grid(True)
plt.show()

