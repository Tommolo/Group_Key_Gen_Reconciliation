def map_decimals_to_naturals(decimal_values):
    # Arrotonda ciascun valore decimale all'intero più vicino e ordina i valori
    rounded_values = sorted(map(round, decimal_values))
    
    # Crea un dizionario che mappa ciascun valore arrotondato a un indice univoco
    value_index_map = {value: index for index, value in enumerate(set(rounded_values))}
    
    # Mappa ciascun valore decimale al suo indice nell'insieme degli arrotondati
    mapped_values = [value_index_map[round(value)] for value in decimal_values]
    
    return mapped_values

# Esempio di utilizzo
decimal_values = [3.14, -2.71, 1.618, -0.577, 2.718, -3.14, 4.669, -1.303]
decimal_values2 = [3.14, -2.71, 1.618, -0.577, 2.718, -3.14, 4.669, -1.303]
mapped_values = map_decimals_to_naturals(decimal_values)
mapped_values2 = map_decimals_to_naturals(decimal_values2)

print("Valori mappati:", mapped_values)
print("Valori mappati:", mapped_values2)
