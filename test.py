from pybloom_live import BloomFilter

# Creazione di un Bloom filter con dimensioni iniziali
bloom_filter = BloomFilter(capacity=1000, error_rate=0.001)

# Inserimento degli elementi di A nel Bloom filter
A = {1, 2, 3, 4, 5}
for a in A:
    bloom_filter.add(a)


# Verifica degli elementi di B
B = list(range(0,100))
missing_in_A = []
for b in B:
    if b not in bloom_filter:
        missing_in_A.append(b)

print("Elementi di B mancanti in A:", missing_in_A)
