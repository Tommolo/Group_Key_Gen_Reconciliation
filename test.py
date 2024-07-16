import numpy as np

    # Generate a random variable from rayleigh distirbution
magnitude = np.random.rayleigh(scale=1.0, size=1)
    # Generate uniformly distributed phases
phase = np.random.uniform(0,2*np.pi, 1)

    # Combine amplitude and phase to form complex coefficients
h_ba= magnitude * np.exp(1j * phase) 

real_part = magnitude * np.cos(phase)
imag_part = magnitude * np.sin(phase)


print(h_ba.real)
print(h_ba.imag)
print(imag_part)
print(real_part)
