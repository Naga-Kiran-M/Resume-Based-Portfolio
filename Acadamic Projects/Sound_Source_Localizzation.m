% Sound Source Localization using TDOA
clc; clear; close all;

% Simulation Parameters
fs = 8000; % Sampling frequency
mic_distance = 0.2; % Distance between microphones (meters)
speed_of_sound = 343; % Speed of sound in air (m/s)

% Load or generate microphone signals
mic1 = audioread('mic1.wav');
mic2 = audioread('mic2.wav');

% Ensure signals are of same length
min_length = min(length(mic1), length(mic2));
mic1 = mic1(1:min_length);
mic2 = mic2(1:min_length);

% Compute Cross-Correlation
[correlation, lags] = xcorr(mic1, mic2);
[~, max_index] = max(abs(correlation));
delay_samples = lags(max_index);

time_delay = delay_samples / fs; % Time delay estimation

% Compute Angle of Arrival (AOA)
angle = asind((time_delay * speed_of_sound) / mic_distance);

% Display Results
disp(['Estimated Time Delay: ', num2str(time_delay), ' seconds']);
disp(['Estimated Angle of Arrival: ', num2str(angle), ' degrees']);

% Plot Cross-Correlation
figure;
plot(lags/fs, correlation);
title('Cross-Correlation between Microphone Signals');
xlabel('Time Lag (s)');
ylabel('Correlation Amplitude');
grid on;
