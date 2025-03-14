% Adaptive Noise Cancellation using LMS Algorithm
clc; clear; close all;

% Generate clean signal
t = 0:1/1000:1;
freq = 10; % Hz
clean_signal = sin(2*pi*freq*t);

% Generate noise
noise = 0.4 * randn(size(t));

% Generate noisy signal
noisy_signal = clean_signal + noise;

% Adaptive Noise Cancellation using LMS
mu = 0.01; % Step size
M = 10; % Filter order
lms_filter = zeros(1, M);
error_signal = zeros(size(t));
y_hat = zeros(size(t));

for i = M:length(t)
    x = noisy_signal(i:-1:i-M+1); % Input segment
    y_hat(i) = lms_filter * x'; % Filtered output
    error_signal(i) = clean_signal(i) - y_hat(i); % Error
    lms_filter = lms_filter + mu * error_signal(i) * x; % Update weights
end

% Plot results
figure;
subplot(3,1,1); plot(t, clean_signal); title('Clean Signal');
subplot(3,1,2); plot(t, noisy_signal); title('Noisy Signal');
subplot(3,1,3); plot(t, error_signal); title('Filtered Signal (Error)');
