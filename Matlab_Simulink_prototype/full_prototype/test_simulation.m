%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.03.2019


% Create a sine wave
Fs = 2000;                   % samples per second
dt = 1/Fs;                   % seconds per sample
StopTime = 0.5;              % seconds
t = (0 : dt : StopTime-dt);  % seconds

% Noise signal
amplitude = 1;
noise_to_signal_ratio = 0.03;
noise = amplitude * noise_to_signal_ratio * randn(1, numel(t)) + amplitude * noise_to_signal_ratio * randn(1, numel(t)) * j;

% Sine signal
frequency_1 = 60;               % Hz
complex_sine_1 = 2 * cos(2 * pi * frequency_1 * t) + 2 * sin(2 * pi * frequency_1 * t) * j;

frequency_2 = 65;               % Hz
complex_sine_2 = 1.8 * cos(2 * pi * frequency_2 * t) + sin(2 * pi * frequency_2 * t) * j;

frequency_3 = 70;               % Hz
complex_sine_3 = 1.6 * cos(2 * pi * frequency_3 * t) + sin(2 * pi * frequency_3 * t) * j;

frequency_4 = 75;               % Hz
complex_sine_4 = 1.4 * cos(2 * pi * frequency_4 * t) + sin(2 * pi * frequency_4 * t) * j;

frequency_5 = 80;               % Hz
complex_sine_5 = 1.2 * cos(2 * pi * frequency_5 * t) + sin(2 * pi * frequency_5 * t) * j;

frequency_6 = 85;               % Hz
complex_sine_6 = 1 * cos(2 * pi * frequency_6 * t) + sin(2 * pi * frequency_6 * t) * j;

frequency_7 = 90;               % Hz
complex_sine_7 = 0.8 * cos(2 * pi * frequency_7 * t) + sin(2 * pi * frequency_7 * t) * j;

complex_signal_final = complex_sine_1 + complex_sine_2 + complex_sine_3 + complex_sine_4 + complex_sine_5 + complex_sine_6 + complex_sine_7;

% Represent our signal in frequency domain, using FFT
freq_domain = abs(fft(complex_signal_final));
freq_domain_target = select_target_band_of_array(freq_domain, 500, Fs, 25, 40);
[power_mw, power_dbm] = calculate_signal_power(freq_domain_target);

disp(power_mw);
disp(power_dbm);

% Plot the signals
subplot(2, 2, 1);
plot(t, abs(complex_signal_final));
xlabel('time (seconds)');
ylabel('amplitude');
title('Time domain');

subplot(2, 2, 2);
plot(freq_domain, '-o');
xlabel('frequency');
ylabel('amplitude');
title('Freqency domain full');

subplot(2, 2, 3);
plot3(t, real(complex_signal_final), imag(complex_signal_final));

subplot(2, 2, 4);
plot(freq_domain_target, '-or');
xlabel('frequency');
ylabel('amplitude');
title('Freqency domain target signal');

sgtitle('Full prototype test');

