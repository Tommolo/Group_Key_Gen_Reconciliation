import math
import numpy as np
import matplotlib.pyplot as plt
from pybloom_live import BloomFilter

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
    
    return round(P_rx_dBm_with_noise,2)

# Parameters
P_tx_dBm = 20        # Transmission power in dBm
distance_m = 100     # Distance
frequency_Hz = 2.4 * 10**9  # Frequency in Hz (2.4 GHz)
noise_std_dB = 2     # standard deviation in dB

# generation of fading for 100 signals
num_signals= 100
fading_dB_values = np.random.normal(loc=-10, scale=2, size=num_signals)

# RSSI with noise for node1 and node2
rssi_values_node1 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values]
rssi_values_node2 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values]


setA = []
setB = []


# Create Vocabulary for A
for i in range(0,len(rssi_values_node1)-1):
        setA.append(rssi_values_node1[i])

# create Vocabulary for B 
for i in range(0,len(rssi_values_node2)-1):
         setB.append(rssi_values_node2[i])

print("SetA: ", setA, "Length: ", len(setA))
print("SetB: ", setB, "Length: ", len(setB))

bloom_filter = BloomFilter(capacity=1000, error_rate=0.001)
for a in setA:
    bloom_filter.add(a)

common_values = []
for b in setB:
    if b in bloom_filter:
      common_values.append(b)

print("Common values: ", common_values)

# Plot of balues for both nodes
plt.figure(figsize=(10, 6))
plt.plot(rssi_values_node1, label='Node 1', marker='o')
plt.plot(rssi_values_node2, label='Node 2', marker='x')
plt.title('RSSi channel Probes')
plt.xlabel('Numero of signals')
plt.ylabel('RSSI (dBm)')
plt.legend()
plt.grid(True)
plt.show()

