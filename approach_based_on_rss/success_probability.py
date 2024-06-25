import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
import math

def generate_nakagami_m_channel(num_samples, m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=np.sqrt(Omega), size=num_samples)
    return magnitudes

# Example parameters
num_samples = 128
m = 3  # Shape parameter (typically m >= 0.5)
Omega = 2  # Scale parameter (mean power)
Ptx = 10  # Power transmission in dBm
d_ab = 50 # Distance in meters
d_ae = 100  # Distance in meters
alpha = 2  # Path loss exponent

p = 0.97  # Example correlation coefficient

iterations = 100
intersection_lengths = []
intersection2_lengths = []

for _ in range(iterations):
    # Generate h_ba channel coefficient
    h_ba = generate_nakagami_m_channel(num_samples, m, Omega)

    # Generate h_ae channel coefficient
    h_ae = generate_nakagami_m_channel(num_samples, m, Omega)

    eps = np.random.normal(loc=0, scale=1, size=num_samples)

    # Compute the cross-correlation
    h_ab = p * h_ba + (1 - p**2*eps)**1/2  # Update h_ab

    # Calculate RSSI
    gamma_ab = (Ptx + abs(h_ab)**2 * d_ab**-alpha) / 2
    gamma_ba = (Ptx + abs(h_ba)**2 * d_ab**-alpha) / 2

    gamma_ae = (Ptx + abs(h_ae)**2 * d_ae**-alpha) / 2

    # Clean and round RSSI values
    cleaned_numbers_ab = np.round(gamma_ab,4)
    cleaned_numbers_ba = np.round(gamma_ba,4)
    cleaned_numbers_ae = np.round(gamma_ae,4)

    # Convert to sets
    set1 = set(cleaned_numbers_ab)
    set2 = set(cleaned_numbers_ba)
    set3 = set(cleaned_numbers_ae)

    # Calculate intersections
    intersection = set1.intersection(set2)
    intersection2 = set1.intersection(set3)

    # Store length of intersection and intersection2
    intersection_lengths.append(len(intersection))
    intersection2_lengths.append(len(intersection2))

print(intersection_lengths)
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
dictionary_value_probability_alice=calcola_frequenza_e_probabilita(intersection_lengths)
dictionary_value_probability_eve=calcola_frequenza_e_probabilita(intersection2_lengths)
print(calcola_frequenza_e_probabilita(intersection_lengths))

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

alice_dictionary = compute_success_probability((dictionary_value_probability_alice),list(range(2,30)))
eve_dictionary = compute_success_probability((dictionary_value_probability_eve),list(range(2,30)))

print(compute_success_probability((dictionary_value_probability_alice),list(range(2,30))))

# Plot the histogram
# Plot the histogram
plt.figure(figsize=(10, 6))
plt.plot(alice_dictionary.keys(), alice_dictionary.values(), marker='o', linestyle='-', color='b')
plt.plot(eve_dictionary.keys(),eve_dictionary.values(), marker= '^',linestyle ='-',color='r')
plt.title('Probability Graph')
plt.xlabel('Polynomial degree')
plt.ylabel('Success Probability')
plt.grid(True)
plt.show()