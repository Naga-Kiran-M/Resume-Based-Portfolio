# Radar Signal Processing for Object Detection

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# Step 1: Generate a Simulated Radar Pulse
fs = 1000  # Sampling Frequency
t = np.linspace(0, 1, fs)  # Time Vector
pulse = chirp(t, f0=100, f1=200, t1=1, method='linear')

# Step 2: Simulate Reflected Signal with Noise
reflection_delay = 0.2  # Object detected at 200ms
received_signal = np.roll(pulse, int(reflection_delay * fs)) + 0.05 * np.random.randn(len(t))

# Step 3: Perform Cross-Correlation to Detect Object
correlation = np.correlate(received_signal, pulse, mode='full')
delay_index = np.argmax(correlation) - len(pulse)

# Step 4: Plot Results
plt.figure(figsize=(12, 6))
plt.subplot(3,1,1)
plt.plot(t, pulse)
plt.title("Transmitted Radar Pulse")

plt.subplot(3,1,2)
plt.plot(t, received_signal)
plt.title("Received Radar Signal (with Object Reflection)")

plt.subplot(3,1,3)
plt.plot(correlation)
plt.axvline(x=delay_index + len(pulse), color='red', linestyle='--', label=f"Object Detected at {delay_index/fs:.2f} s")
plt.title("Cross-Correlation for Object Detection")
plt.legend()
plt.show()
