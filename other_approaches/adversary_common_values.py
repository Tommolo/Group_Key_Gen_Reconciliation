import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB):
    # Velocità della luce in m/s
    c = 3 * 10**8
    
    # Calcolo della lunghezza d'onda
    wavelength_m = c / frequency_Hz
    
    # Perdita di percorso
    path_loss = (4 * math.pi * distance_m / wavelength_m)**2
    path_loss_dB = 10 * math.log10(path_loss)
    
    # Calcolo RSSI senza rumore
    P_rx_dBm = P_tx_dBm - path_loss_dB + fading_dB
    
    # Rumore gaussiano
    noise_dB = np.random.normal(loc=0, scale=noise_std_dB)
    P_rx_dBm_with_noise = P_rx_dBm + noise_dB
    
    return round(P_rx_dBm_with_noise, 2)

# Parametri
P_tx_dBm = 20
distance_alice_bob = 100
distance_alice_eve = 200
frequency_Hz = 2.4 * 10**9
noise_std_dB_alice_bob = 2
noise_std_dB_alice_eve = 2
num_signals = 128
iterations = 100


fading_dB_values_alice_bob = np.random.normal(loc=-10, scale=2, size=num_signals)
fading_dB_values_alice_eve = np.random.normal(loc=-5, scale=2, size=num_signals)
    
rssi_values_alice = [calculate_rssi(P_tx_dBm, distance_alice_bob, frequency_Hz, fading_dB, noise_std_dB_alice_bob) for fading_dB in fading_dB_values_alice_bob]
rssi_values_bob = [calculate_rssi(P_tx_dBm, distance_alice_bob, frequency_Hz, fading_dB, noise_std_dB_alice_bob) for fading_dB in fading_dB_values_alice_bob]
rssi_values_eve = [calculate_rssi(P_tx_dBm, distance_alice_eve, frequency_Hz, fading_dB, noise_std_dB_alice_eve) for fading_dB in fading_dB_values_alice_eve]

vocabularyA = rssi_values_alice
vocabularyB = rssi_values_bob
vocabularyE = rssi_values_eve

common_values_alice_bob = set([b for b in vocabularyB if b in vocabularyA])
common_values_alice_eve = set([e for e in vocabularyE if e in vocabularyA])

print(common_values_alice_bob, "Length: ",len(common_values_alice_bob))
print(common_values_alice_eve, "Length: ", len(common_values_alice_eve))



# Plot del grafico a linee
plt.figure(figsize=(10, 6))
plt.plot(vocabularyA, label='Alice-Bob', color='blue')
plt.plot(vocabularyE, label='Alice-Eve', color='red')
plt.title('Rssi probes values')
plt.xlabel('Probes values')
plt.ylabel('rssi')
plt.legend()
plt.grid(True)
plt.show()
