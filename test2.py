import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)

def johnson_nyquist_noise(R, T, f_start, f_end, f_points):
    """
    Calculate the Johnson-Nyquist noise power spectral density.
    
    Parameters:
    R (float): Resistance in ohms (Ω)
    T (float): Temperature in kelvin (K)
    f_start (float): Start frequency in Hz
    f_end (float): End frequency in Hz
    f_points (int): Number of frequency points
    
    Returns:
    f (numpy array): Frequency array
    S (numpy array): Power spectral density array
    """
    f = np.linspace(f_start, f_end, f_points)
    S = 4 * k_B * T * R
    return f, S

# Parameters
R = 1000  # Resistance in ohms
T = 300   # Temperature in kelvin
f_start = 1  # Start frequency in Hz
f_end = 1e6  # End frequency in Hz
f_points = 500  # Number of frequency points

# Calculate noise
frequencies, noise_psd = johnson_nyquist_noise(R, T, f_start, f_end, f_points)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(frequencies, noise_psd * np.ones_like(frequencies), label='Johnson-Nyquist Noise')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (W/Hz)')
plt.title('Johnson-Nyquist Noise Power Spectral Density')
plt.legend()
plt.grid(True)
plt.show()
