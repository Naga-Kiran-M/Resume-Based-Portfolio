# 🚀 E;ectronics & Signal Processing Projects

This repository contains implementations of various **Machine Learning, Signal Processing, and Embedded Systems** projects. These projects cover **adaptive noise cancellation, image restoration, speaker verification, sound source localization, and real-time heartbeat monitoring using a microcontroller**.

---

## 📌 **1. Adaptive Noise Cancellation using a DSP Board**
### 🛠 Technologies: **MATLAB, Digital Signal Processing (DSP)**

**Overview:**
- Implemented an **Adaptive Noise Cancellation** algorithm using **Visual DSP + 5.1**.
- Utilized the **Least Mean Squares (LMS)** adaptive filter for real-time noise reduction.

**Key Features:**
- Simulates a noisy signal and applies adaptive filtering.
- Adjusts the filter coefficients dynamically based on error minimization.

🔗 **Code:** [`adaptive_noise_cancellation.m`](adaptive_noise_cancellation.m)

---

## 📌 **2. Image Restoration and Enhancement**
### 🛠 Technologies: **MATLAB, Image Processing**

**Overview:**
- Restored an image distorted due to an **imperfect lens and CCD noise**.
- Implemented **Wiener filtering** and **Histogram Equalization** for enhancement.

**Key Features:**
- Simulates motion blur and Gaussian noise.
- Restores the image using **deconvolution and adaptive filtering**.

🔗 **Code:** [`image_restoration.m`](image_restoration.m)

---

## 📌 **3. Speaker Verification using Cross-Correlation**
### 🛠 Technologies: **MATLAB, Audio Processing**

**Overview:**
- Developed a **Speaker Verification System** using **Cross-Correlation techniques**.
- Verified English-speaking speakers based on their voice characteristics.

**Key Features:**
- Computes cross-correlation between test and reference speech signals.
- Uses a similarity threshold to classify whether the speaker is verified.

🔗 **Code:** [`speaker_verification.m`](speaker_verification.m)

---

## 📌 **4. Sound Source Localization using TDOA**
### 🛠 Technologies: **MATLAB, Time Difference of Arrival (TDOA)**

**Overview:**
- Implemented **Time Delay Estimation (TDE)** to **localize a sound source**.
- Used **cross-correlation and Least Mean Squares Adaptive Filtering** for noise reduction.

**Key Features:**
- Computes **Time Difference of Arrival (TDOA)** between two microphones.
- Estimates **Angle of Arrival (AOA)** using **speed of sound and microphone spacing**.

🔗 **Code:** [`sound_source_localization.m`](sound_source_localization.m)

---

## 📌 **5. Real-Time Heartbeat Monitoring using PIC16F876 Microcontroller**
### 🛠 Technologies: **Embedded C, MPLAB XC8, Microcontrollers**

**Overview:**
- Designed a **low-cost heartbeat monitoring system** using a **PIC16F876** microcontroller.
- Sensed blood flow variations in the fingertip and displayed **heartbeat rate (BPM)** on an **LCD screen**.

**Key Features:**
- Uses **RA0** (analog input) to read heartbeat sensor data.
- Displays BPM on a **16x2 character LCD**.
- Implemented using **MPLAB XC8** and **PIC microcontroller programming**.

🔗 **Code:** [`heartbeat_monitor_pic16f876.c`](heartbeat_monitor_pic16f876.c)

---

## 📫 **Contact & Contributions**
- Author: **Naga Kiran Machiraju**
- GitHub: [@Naga-Kiran-M](https://github.com/Naga-Kiran-M)
- If you have any suggestions or improvements, feel free to open an issue or contribute! 🚀
