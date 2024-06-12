import random

def generate_bitstrings(length, bdr):
    # Genera una stringa di bit casuale per Alice
    alice_bits = [random.randint(0, 1) for _ in range(length)]
    
    # Genera la stringa di bit di Bob con un BDR specificato rispetto a quella di Alice
    bob_bits = alice_bits[:]
    for i in range(length):
        if random.random() < bdr:
            bob_bits[i] = 1 - bob_bits[i]  # Flip bit to introduce an error
    
    return alice_bits, bob_bits

def parity(bits):
    return sum(bits) % 2

def correct_bits(alice_bits, bob_bits, indices, packet_count):
    packet_count[0] += 1  # Incrementa il contatore dei pacchetti
    a_parity = parity([alice_bits[i] for i in indices])
    b_parity = parity([bob_bits[i] for i in indices])
    
    if a_parity != b_parity:
        if len(indices) == 1:
            # We've isolated the error bit
            bob_bits[indices[0]] = alice_bits[indices[0]]
        else:
            mid = len(indices) // 2
            correct_bits(alice_bits, bob_bits, indices[:mid], packet_count)
            correct_bits(alice_bits, bob_bits, indices[mid:], packet_count)

def cascade_algorithm(alice_bits, bob_bits):
    length = len(alice_bits)
    block_size = 4  # Example initial block size
    packet_count = [0]  # Contatore dei pacchetti, usiamo una lista per mutabilità

    while block_size <= length:
        for start in range(0, length, block_size):
            end = min(start + block_size, length)
            indices = list(range(start, end))
            correct_bits(alice_bits, bob_bits, indices, packet_count)
        block_size *= 2  # Double the block size

    return bob_bits, packet_count[0]

# Parametri
bit_length = 128
bdr = 0.05

# Generazione delle stringhe di bit
alice_bits, bob_bits = generate_bitstrings(bit_length, bdr)

print("Stringa di bit di Alice: ", alice_bits)
print("Stringa di bit di Bob (con errori): ", bob_bits)

# Esecuzione del Cascade Algorithm
corrected_bob_bits, packet_count = cascade_algorithm(alice_bits, bob_bits)

print("Stringa di bit di Bob (corretta): ", corrected_bob_bits)
print("Correzione riuscita:", alice_bits == corrected_bob_bits)
print("Numero di pacchetti inviati:", packet_count)
