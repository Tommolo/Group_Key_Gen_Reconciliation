import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB):
    # Velocità della luce in m/s
    c = 3 * 10**8
    
    # Calcolare la lunghezza d'onda
    wavelength_m = c / frequency_Hz
    
    # Calcolare la perdita di percorso (path loss) in dB
    path_loss = (4 * math.pi * distance_m / wavelength_m)**2
    path_loss_dB = 10 * math.log10(path_loss)
    
    # Calcolare l'RSSI senza rumore
    P_rx_dBm = P_tx_dBm - path_loss_dB + fading_dB
    
    # Aggiungere il rumore gaussiano
    noise_dB = np.random.normal(loc=0, scale=noise_std_dB)
    P_rx_dBm_with_noise = P_rx_dBm + noise_dB
    
    return P_rx_dBm_with_noise

# Esempio di parametri
P_tx_dBm = 20        # Potenza trasmessa in dBm
distance_m = 100     # Distanza in metri
frequency_Hz = 2.4 * 10**9  # Frequenza in Hz (2.4 GHz)
noise_std_dB = 2     # Deviazione standard del rumore gaussiano in dB

# Generare un set di x valori di fading per entrambi i nodi
num_signals= 10
fading_dB_values = np.random.normal(loc=-10, scale=2, size=num_signals)

# Calcolare l'RSSI con rumore per ciascun segnale per entrambi i nodi
rssi_values_node1 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values]
rssi_values_node2 = [calculate_rssi(P_tx_dBm, distance_m, frequency_Hz, fading_dB, noise_std_dB) for fading_dB in fading_dB_values]

mean1 = np.mean(rssi_values_node1)
mean2 = np.mean(rssi_values_node2)


mean1_qm = mean1-2
mean1_qp = mean1 +1

mean2_qm = mean2-4
mean2_qp = mean2 + 4

setA = []
setB = []


for i in range(0,len(rssi_values_node1)-1):
    if(rssi_values_node1[i]<(mean1_qm) or rssi_values_node1[i]>(mean1_qp)):
        setA.append([i])

for i in range(0,len(rssi_values_node2)-1):
    if(rssi_values_node2[i]<(mean2_qm) or rssi_values_node2[i] > (mean2_qp) ):
         setB.append([i])


 
print("SetA: ", setA, "Length: ", len(setA))
print("SetB: ", setB, "Length: ", len(setB))

differences = []
chaff_points = list(range(0,num_signals))
random_points=[]

for element1 in setA:
    if element1 not in chaff_points:
        random_points.append(element1)

#print("Chaff points: ", random_points)

for element in setB:
    if element not in setA:
        differences.append(element)
    

print("Differences: ", differences, "Length: ", len(differences))


# Plot dei valori RSSI per entrambi i nodi
plt.figure(figsize=(10, 6))
plt.plot(rssi_values_node1, label='Nodo 1', marker='o')
plt.plot(rssi_values_node2, label='Nodo 2', marker='x')

plt.axhline(mean1_qp, color='red', linestyle='--', linewidth=2)
plt.axhline(mean1_qm, color='red', linestyle='--', linewidth=2)

plt.axhline(mean2_qp, color='green', linestyle='--', linewidth=2)
plt.axhline(mean2_qm, color='green', linestyle='--', linewidth=2)

plt.title('RSSi channel Probes')
plt.xlabel('Numero di segnale')
plt.ylabel('RSSI (dBm)')
plt.legend()
plt.grid(True)
plt.show()

