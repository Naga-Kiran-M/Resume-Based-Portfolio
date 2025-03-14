% Image Restoration and Enhancement using Wiener Filter
clc; clear; close all;

% Read and display the original image
original_img = im2double(imread('cameraman.tif'));
figure;
subplot(2,2,1);
imshow(original_img);
title('Original Image');

% Simulate distortion (blur + noise)
PSF = fspecial('motion', 10, 45); % Motion blur
blurred_img = imfilter(original_img, PSF, 'conv', 'circular');
noisy_img = imnoise(blurred_img, 'gaussian', 0, 0.01);
subplot(2,2,2);
imshow(noisy_img);
title('Blurred and Noisy Image');

% Apply Wiener filter for restoration
estimated_nsr = 0.01; % Noise-to-signal ratio
restored_img = deconvwnr(noisy_img, PSF, estimated_nsr);
subplot(2,2,3);
imshow(restored_img);
title('Restored Image using Wiener Filter');

% Apply Histogram Equalization for Enhancement
enhanced_img = histeq(restored_img);
subplot(2,2,4);
imshow(enhanced_img);
title('Enhanced Image with Histogram Equalization');
