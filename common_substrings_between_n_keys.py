import random

def generate_random_string(length):
    return ''.join(random.choice('01') for _ in range(length))

def generate_substrings(string, size):
    substrings = set()
    for i in range(len(string) - size + 1):
        substrings.add(string[i:i+size])
    return substrings

def generate_unique_substrings(strings, size):
    all_substrings = set()
    for s in strings:
        all_substrings |= generate_substrings(s, size)
    
    all_possible_substrings = {bin(i)[2:].zfill(size) for i in range(2 ** size)}
    
    unique_substrings = all_possible_substrings - all_substrings
    return unique_substrings

def find_common_substrings(strings, size):
    common_substrings = set(strings[0][i:i+size] for i in range(len(strings[0]) - size + 1))
    for s in strings[1:]:
        common_substrings &= generate_substrings(s, size)
    return common_substrings

def main():
    # Genera tre stringhe casuali di bit
    group_key = generate_random_string(128)

    string1 = generate_random_string(128)
    string2 = generate_random_string(128)

    string3 = generate_random_string(128)
    string4 = generate_random_string(128)
    
    string5 = generate_random_string(128)
    string6 = generate_random_string(128)
    
    print("String1: ", string1,"\n", "String2: ","\n", string2,"\n", "String3: ", string3, "\n",)

    # Genera un insieme di sottostringhe uniche di 8 bit
    unique_substrings = generate_unique_substrings([string1, string2, string3], 8)
    common_substrings = find_common_substrings([string1, string2, string3], 8)
   
    print("Insieme di sottostringhe uniche di 8 bit:")
    for substring in unique_substrings:
        print(substring)
        
    print("Sottostringhe comuni di 8 bit:")
    for substring in common_substrings:
        print(substring)
    print("Length common_sub: ", len(common_substrings))

if __name__ == "__main__":
    main()
