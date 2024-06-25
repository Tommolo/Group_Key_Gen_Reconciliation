import math
import numpy as np
import matplotlib.pyplot as plt

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
    
    return round(P_rx_dBm_with_noise, 2)

# Parameters
P_tx_dBm = 20
distance_m = 10
frequency_Hz = 2.4 * 10**9
noise_std_dB = 2
num_signals = 100
iterations = 1000

common_values_counts = []

for _ in range(iterations):
    fading_dB_values_alice_bob = np.random.normal(loc=-10, scale=2, size=num_signals)
    
    rssi_values_node1 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
    rssi_values_node2 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
    
    vocabularyA = rssi_values_node1[:-1]
    vocabularyB = rssi_values_node2[:-1]
    
    common_values = [b for b in vocabularyB if b in vocabularyA]
    print(common_values)
    common_values_counts.append(len(set(common_values)))

   

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(common_values_counts, bins=range(min(common_values_counts), max(common_values_counts) + 1, 1), edgecolor='black')
plt.title('Histogram of Common Values Count Over 1000 Iterations')
plt.xlabel('Number of Common Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
