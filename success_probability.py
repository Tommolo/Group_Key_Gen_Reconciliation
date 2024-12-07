import math

# Compute the binomial coefficient function
def binom(n, k):
    return math.comb(n, k)

# Function to calculate probability of success
def compute_p_success(n_genuine, k_genuine, n_total, k_total):
    return binom(n_genuine, k_genuine) / binom(n_total, k_total)

# Values for total points, chaff points, and the number of points to select
k_genuine = 32
n_total = 320
k_total = 32

# Case 1: 128 genuine points
n_genuine = 320
P_success = compute_p_success(n_genuine, k_genuine, n_total, k_total)
print(f"P_success with {n_genuine} genuine points: {P_success}")

