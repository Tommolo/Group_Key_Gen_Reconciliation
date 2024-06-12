import numpy as np
from sympy import symbols, Poly
import random

# Generare un polinomio casuale rappresentante il segreto
def generate_polynomial(degree, secret):
    x = symbols('x')
    coefficients = [random.randint(1, 100) for _ in range(degree)]
    coefficients.append(secret)
    polynomial = Poly(sum([coefficients[i] * x**i for i in range(len(coefficients))]), x)
    return polynomial

# Creare il vault con i valori RSSI
def create_vault(rssi_values, polynomial, chaff_points=100):
    vault = []
    for rssi in rssi_values:
        y = polynomial.eval(rssi)
        vault.append((rssi, y))
    
    # Aggiungere chaff points
    for _ in range(chaff_points):
        x_chaff = random.randint(min(rssi_values), max(rssi_values))
        y_chaff = random.randint(1, 1000)
        vault.append((x_chaff, y_chaff))
    
    random.shuffle(vault)
    return vault

# Esempio di valori RSSI
rssi_values = [74, -69, -73, -72, -67, -66, -71, -70, -68, -75, -63]

# Generare un polinomio segreto
secret = 12345  # Questo è il segreto che vogliamo proteggere
polynomial = generate_polynomial(degree=3, secret=secret)

# Creare il vault
vault = create_vault(rssi_values, polynomial)

print("Vault creato:", vault)
