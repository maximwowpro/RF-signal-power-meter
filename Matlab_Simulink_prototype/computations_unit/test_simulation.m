%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.03.2019


% Create a sine wave
Fs = 8000;                   % samples per second
dt = 1/Fs;                   % seconds per sample
StopTime = 0.5;              % seconds
t = (0 : dt : StopTime-dt);  % seconds

% Noise signal
amplitude = 1;
noise_to_signal_ratio = 0.03;
noise = amplitude * noise_to_signal_ratio * randn(1, numel(t)) + amplitude * noise_to_signal_ratio * randn(1, numel(t)) * j;

% Sine signal
frequency_1 = 60;               % Hz
sine_signal_1 = cos(2 * pi * frequency * t);
complex_sine_1 = 2 * cos(2 * pi * frequency_1 * t) + 2 * sin(2 * pi * frequency_1 * t) * j;
complex_sine_noisy_1 = complex_sine_1 + noise;

frequency_2 = 65;               % Hz
sine_signal_2 = cos(2 * pi * frequency * t);
complex_sine_2 = cos(2 * pi * frequency_2 * t) + sin(2 * pi * frequency_2 * t) * j;
complex_sine_noisy_2 = complex_sine_1 + noise;

frequency_3 = 70;               % Hz
sine_signal_3 = cos(2 * pi * frequency * t);
complex_sine_3 = cos(2 * pi * frequency_3 * t) + sin(2 * pi * frequency_3 * t) * j;
complex_sine_noisy_3 = complex_sine_1 + noise;

frequency_4 = 75;               % Hz
sine_signal_4 = cos(2 * pi * frequency * t);
complex_sine_4 = cos(2 * pi * frequency_4 * t) + sin(2 * pi * frequency_4 * t) * j;
complex_sine_noisy_4 = complex_sine_1 + noise;

complex_signal_final = complex_sine_1 + complex_sine_2 + complex_sine_3 + complex_sine_4;

% Represent our signal in frequency domain, using FFT
freq_domain = abs(fft(complex_signal_final));

% Plot the signals
subplot(2, 2, 1);
plot(t, abs(complex_signal_final));
xlabel('time (seconds)');
ylabel('amplitude');
title('Time domain');

subplot(2, 2, 2);
plot(freq_domain, '-or');
xlabel('frequency');
ylabel('amplitude');
title('Freqency domain');

subplot(2, 2, 3);
plot3(t, real(complex_signal_final), imag(complex_signal_final));

subplot(2, 2, 4);
plot3(t, real(complex_signal_final), imag(complex_signal_final));

sgtitle('Computations unit test');




