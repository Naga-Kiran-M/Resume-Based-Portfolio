% Noise Reduction in Audio Signals using MATLAB

% Step 1: Load the Noisy Audio File
[audio, fs] = audioread('assets/datasets/noisy_audio.wav');
t = (0:length(audio)-1)/fs; % Time axis

% Step 2: Apply Fast Fourier Transform (FFT)
Y = fft(audio);
frequencies = (0:length(Y)-1) * fs / length(Y);

% Step 3: Design a Low-Pass Filter
fc = 1000; % Cutoff Frequency in Hz
[b, a] = butter(6, fc/(fs/2), 'low'); % 6th order Butterworth filter

% Step 4: Apply the Filter to Remove Noise
filtered_audio = filter(b, a, audio);

% Step 5: Plot the Results
figure;
subplot(2,1,1);
plot(t, audio);
title('Original Noisy Audio');
xlabel('Time (s)'); ylabel('Amplitude');

subplot(2,1,2);
plot(t, filtered_audio);
title('Filtered Audio');
xlabel('Time (s)'); ylabel('Amplitude');

% Step 6: Save and Play the Processed Audio
audiowrite('assets/datasets/filtered_audio.wav', filtered_audio, fs);
sound(filtered_audio, fs);
