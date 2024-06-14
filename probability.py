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
num_signals = 128

iterations = 1000

common_values_counts = []
probability = []

for _ in range(iterations):
    fading_dB_values_alice_bob = np.random.normal(loc=-10, scale=2, size=num_signals)
    
    rssi_values_node1 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
    rssi_values_node2 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values_alice_bob]
    
    vocabularyA = rssi_values_node1[:-1]
    vocabularyB = rssi_values_node2[:-1]
    
    common_values = [b for b in vocabularyB if b in vocabularyA]

    common_values_counts.append(len(set(common_values)))
    


def calcola_frequenza_e_probabilita(lista):
    dizionario_probabilita = {}
    lunghezza_lista = len(lista)
    
    for valore in sorted(lista):
        if valore not in dizionario_probabilita:
            frequenza = lista.count(valore)
            probabilita = frequenza / lunghezza_lista
            dizionario_probabilita[valore] = probabilita
            
    return dizionario_probabilita

probability_of_success=[]
dictionary_value_probability=calcola_frequenza_e_probabilita(common_values_counts)
print(calcola_frequenza_e_probabilita(common_values_counts))

def compute_success_probability(dizionario, lista):
    nuovo_dizionario = {}
    
    # Ordina le chiavi del dizionario per sicurezza
    chiavi_ordinate = sorted(dizionario.keys())
    
    for l in lista:
        somma_probabilita = 0
        for chiave in chiavi_ordinate:
            if l > chiave:
                somma_probabilita += dizionario[chiave]
        nuovo_dizionario[l-1] = 1 - somma_probabilita
    
    return nuovo_dizionario

nuovo_dizionario = compute_success_probability((dictionary_value_probability),list(range(2,30)))
print(compute_success_probability((dictionary_value_probability),list(range(2,30))))
# Plot the histogram
# Plot the histogram
plt.figure(figsize=(10, 6))
plt.plot(nuovo_dizionario.keys(), nuovo_dizionario.values(), marker='o', linestyle='-', color='b')
plt.title('Probability Graph')
plt.xlabel('Polynomial degree')
plt.ylabel('Success Probability')
plt.grid(True)
plt.show()