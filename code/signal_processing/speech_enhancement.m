% Speech Enhancement Using Spectrogram Filtering

% Step 1: Load Noisy Speech Signal
[speech, fs] = audioread('assets/datasets/noisy_speech.wav');

% Step 2: Compute Spectrogram
win = hamming(256);
overlap = 128;
nfft = 512;
[S, F, T] = spectrogram(speech, win, overlap, nfft, fs, 'yaxis');

% Step 3: Apply Spectral Subtraction (Noise Reduction)
noise_estimate = mean(abs(S(:, 1:10)), 2); % Estimate noise from first frames
S_denoised = max(abs(S) - repmat(noise_estimate, 1, size(S, 2)), 0) .* exp(1i*angle(S));

% Step 4: Convert Back to Time-Domain
speech_enhanced = real(ifft(S_denoised, nfft));

% Step 5: Save and Play Processed Speech
audiowrite('assets/datasets/enhanced_speech.wav', speech_enhanced, fs);
sound(speech_enhanced, fs);

% Step 6: Plot Results
figure;
subplot(2,1,1);
spectrogram(speech, win, overlap, nfft, fs, 'yaxis');
title('Original Noisy Speech Spectrogram');

subplot(2,1,2);
spectrogram(speech_enhanced, win, overlap, nfft, fs, 'yaxis');
title('Enhanced Speech Spectrogram');
