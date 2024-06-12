import numpy as np

def estimate_packets(N, p, L):
    """
    Stima il numero totale di pacchetti necessari per il protocollo Cascade.
    
    :param N: Numero di bit nella stringa
    :param p: Probabilità di errore per bit
    :param L: Numero di livelli nel protocollo Cascade
    :return: Numero stimato di pacchetti
    """
    B = int(np.sqrt(N))  # Dimensione iniziale del blocco
    total_packets = 0
    
    for level in range(L):
        num_blocks = N // B
        # Pacchetti per parità (2 per blocco)
        packets_parity = num_blocks * 2
        # Pacchetti per correzione errori (stima: p * B * num_blocks)
        packets_correction = num_blocks * p * B
        
        # Somma dei pacchetti per il livello attuale
        total_packets += packets_parity + packets_correction
        
        # Riduzione della dimensione del blocco per il livello successivo
        B = B // 2 if B > 1 else 1
    
    return total_packets

# Parametri di esempio
N = 128  # Lunghezza della stringa in bit
p = 0.01  # Probabilità di errore per bit
L = 3  # Numero di livelli

# Calcolo della stima dei pacchetti
estimated_packets = estimate_packets(N, p, L)
estimated_packets