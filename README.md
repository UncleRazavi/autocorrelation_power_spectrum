# Autocorrelation & Power Spectrum Analysis

This Python script analyzes a random signal by computing its **autocorrelation** and **power spectrum** using NumPy and Matplotlib.

---

##  Overview

- **Autocorrelation**: Measures how similar a signal is to a lagged version of itself, revealing patterns and periodicity.  
- **Power Spectrum**: Shows the distribution of power (signal strength) across frequencies, highlighting dominant components.

---

## ⚙️ How It Works

1. **Generate Signal**  
   Creates a random signal of 1000 values using a uniform distribution.  

2. **Calculate Autocorrelation**  
   The `autocorrelation()` function computes the autocorrelation of the signal.  

3. **Compute Power Spectrum**  
   Uses the **Fast Fourier Transform (FFT)** of the autocorrelation to obtain the power spectrum.  

4. **Plot Results**  
   - **Autocorrelation Plot**: Autocorrelation vs. lag  
   - **Power Spectrum Plot**: Power spectrum vs. frequency (positive frequencies only)  

---

## Dependencies

- [NumPy](https://numpy.org/) — numerical operations and FFT  
- [Matplotlib](https://matplotlib.org/) — plotting and visualization  

---

## ▶ Usage

Run the script directly:

```bash
python autocorrelation_power_spectrum.py
