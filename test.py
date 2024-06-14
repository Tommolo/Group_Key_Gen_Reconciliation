def calcola_somma_precedenti(dizionario, lista):
    nuovo_dizionario = {}
    
    # Ordina le chiavi del dizionario per sicurezza
    chiavi_ordinate = sorted(dizionario.keys())
    
    for l in lista:
        somma_probabilita = 0
        for chiave in chiavi_ordinate:
            if l > chiave:
                somma_probabilita += dizionario[chiave]
        nuovo_dizionario[l] = somma_probabilita
    
    return nuovo_dizionario

# Esempio di utilizzo:
dizionario = {4: 0.001, 5: 0.005, 6: 0.008, 7: 0.014, 8: 0.02, 9: 0.04, 10: 0.061, 11: 0.094, 12: 0.108, 13: 0.116, 14: 0.121, 15: 0.113, 16: 0.105, 17: 0.069, 18: 0.045, 19: 0.035, 20: 0.022, 21: 0.009, 22: 0.01, 23: 0.002, 24: 0.001, 26: 0.001}
lista = list(range(2, 30))
nuovo_dizionario = calcola_somma_precedenti(dizionario, lista)
print(nuovo_dizionario)
