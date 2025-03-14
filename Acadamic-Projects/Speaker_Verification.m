% Speaker Verification using Cross-Correlation
clc; clear; close all;

% Load or simulate reference and test speech signals
fs = 8000; % Sampling frequency
ref_signal = audioread('reference_speaker.wav');
test_signal = audioread('test_speaker.wav');

% Ensure signals are of same length
min_length = min(length(ref_signal), length(test_signal));
ref_signal = ref_signal(1:min_length);
test_signal = test_signal(1:min_length);

% Compute Cross-Correlation
[correlation, lags] = xcorr(ref_signal, test_signal, 'coeff');

% Determine similarity threshold
similarity_score = max(abs(correlation));
threshold = 0.7; % Set an empirical threshold for verification

% Decision based on similarity score
if similarity_score > threshold
    disp('Speaker Verified: Match Found');
else
    disp('Speaker Not Verified: No Match');
end

% Plot the Cross-Correlation
figure;
plot(lags/fs, correlation);
title('Cross-Correlation of Speech Signals');
xlabel('Time Lag (s)');
ylabel('Correlation Coefficient');
grid on;
