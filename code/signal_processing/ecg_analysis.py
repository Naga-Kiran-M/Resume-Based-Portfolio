# Real-Time ECG Signal Analysis

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import wfdb  # Import ECG dataset

# Step 1: Load ECG Signal
record = wfdb.rdrecord('assets/datasets/100', sampto=1000)
ecg_signal = record.p_signal[:,0]
fs = record.fs  # Sampling Frequency

# Step 2: Apply Bandpass Filter to Remove Noise
def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

filtered_ecg = bandpass_filter(ecg_signal, 0.5, 45, fs)

# Step 3: Detect Peaks (Heartbeats)
from scipy.signal import find_peaks
peaks, _ = find_peaks(filtered_ecg, height=0.5, distance=fs//2)

# Step 4: Plot the ECG Signal with Detected Peaks
plt.figure(figsize=(10, 5))
plt.plot(ecg_signal, label="Raw ECG Signal", alpha=0.5)
plt.plot(filtered_ecg, label="Filtered ECG Signal", color="red")
plt.scatter(peaks, filtered_ecg[peaks], color='black', marker='o', label="Detected Peaks")
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("ECG Signal Analysis")
plt.show()
