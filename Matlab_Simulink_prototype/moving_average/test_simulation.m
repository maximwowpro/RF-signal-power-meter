%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   26.02.2019


% Firstly, create a sine wave with noise
Fs = 8000;                   % samples per second
dt = 1/Fs;                   % seconds per sample
StopTime = 0.15;             % seconds
t = (0 : dt : StopTime-dt);  % seconds

% Sine signal
frequency = 60;               % Hz
sine_signal = cos(2 * pi * frequency * t);

% Noise signal
amplitude = 1;
noise_to_signal_ratio = 0.3;
noise = amplitude * noise_to_signal_ratio * randn(1, numel(t));

% Add noise to sine signal
sine_signal = sine_signal + noise;

% Smooth signal using moving average algorithm
av_1 = 4; 
av_2 = 16;
av_3 = 64;

t_1 = t(av_1 / 2 : end - av_1 / 2 - 1);
t_2 = t(av_2 / 2 : end - av_2 / 2 - 1);
t_3 = t(av_3 / 2 : end - av_3 / 2 - 1);


out_1 = moving_average(sine_signal, av_1);
out_2 = moving_average(sine_signal, av_2);
out_3 = moving_average(sine_signal, av_3);

% Plot all signals
subplot(2, 2, 1);
plot(t, sine_signal);
xlabel('time (seconds)');
title('Without average');

subplot(2, 2, 2);
disp(numel(t_1))
disp(numel(out_1))
plot(t_1, out_1);
xlabel('time (seconds)');
title(strcat('Average = ', num2str(av_1)));

subplot(2, 2, 3);
plot(t_2, out_2);
xlabel('time (seconds)');
title(strcat('Average = ', num2str(av_2)));

subplot(2, 2, 4);
plot(t_3, out_3);
xlabel('time (seconds)');
title(strcat('Average = ', num2str(av_3)));


sgtitle('Moving average test');


