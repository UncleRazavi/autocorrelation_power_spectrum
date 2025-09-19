# autocorrelation_power_spectrum
Autocorrelation and Power Spectrum Analysis Script

This Python script performs an analysis of a random signal's autocorrelation and power spectrum using NumPy and Matplotlib.

-Autocorrelation: Measures how similar a signal is with a lagged version of itself, providing insight into patterns and periodicity within the data.
-Power Spectrum: Displays the distribution of power (or signal strength) over frequency, revealing the dominant frequencies in the signal.

How it Works

-Generate Signal: The script generates a random signal of 1000 values using a uniform distribution.
-Calculate Autocorrelation: Using the autocorrelation() function, the autocorrelation of the signal is calculated.
-Compute Power Spectrum: Applies the Fast Fourier Transform (FFT) on the autocorrelation to determine the power spectrum.
Plot Results:
        Autocorrelation Plot: Shows the autocorrelation as a function of lag.
        Power Spectrum Plot: Visualizes the power spectrum against frequency, limited to positive frequencies.

Dependencies

-NumPy: For numerical operations and FFT.
-Matplotlib: For generating visualizations.

Usage

Simply run the script, and it will display the autocorrelation and power spectrum plots.
