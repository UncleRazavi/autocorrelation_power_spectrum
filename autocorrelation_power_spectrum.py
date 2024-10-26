import numpy as np
import matplotlib.pyplot as plt

N = 1000
Xn = np.random.uniform(-0.5, 0.5, N)
def autocorrelation(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size // 2:]
autocorr = autocorrelation(Xn)
power_spectrum = np.abs(np.fft.fft(autocorr))

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(autocorr)
plt.title('Autocorrelation')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')

plt.subplot(1, 2, 2)
frequencies = np.fft.fftfreq(len(autocorr))
plt.plot(frequencies[:N//2], power_spectrum[:N//2])  # Plot positive frequencies only
plt.title('Power Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()
plt.show()
