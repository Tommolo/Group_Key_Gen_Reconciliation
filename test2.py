import numpy as np

# Supponiamo di avere i seguenti coefficienti di canale tra Alice e Bob
h = np.random.uniform(0, 1, 1000)  # 1000 campioni casuali tra 0 e 1

# Definiamo il numero di livelli di quantizzazione
L_A = 8  # Livelli di quantizzazione per Alice
L_B = 4  # Livelli di quantizzazione per Bob

# Funzione per quantizzare i coefficienti
def quantize(h, levels):
    # Trova i limiti degli intervalli di quantizzazione
    bins = np.linspace(0, 1, levels + 1)
    # Trova gli indici dei livelli di quantizzazione per ciascun campione
    quantized_indices = np.digitize(h, bins) - 1
    # Mappa gli indici ai valori centrali degli intervalli
    quantized_values = (bins[:-1] + bins[1:]) / 2
    return quantized_values[quantized_indices]

# Quantizzazione per Alice
quantized_h_A = quantize(h, L_A)

# Quantizzazione per Bob
quantized_h_B = quantize(h, L_B)

# Verifica che i livelli di quantizzazione di Bob siano un sottoinsieme di quelli di Alice
print("Quantizzazione per Alice:",quantized_h_A)
print("Quantizzazione per Bob:", quantized_h_B)
