%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.03.2019

center_freq       = 100e6;
tuner_gain        = 40;    	 % dB
samp_rate         = 2e6;
samples_per_frame = 4096;

num_dump_frames = 100;		% We have to dump some frames before receiving information from RTL-SDR to not receive rubbish.
num_useful_frames = 16;

target_freq_begin = 99.1e6;
target_freq_end   = 99.4e6;

average_factor = 16;

power_mw  = 0;
power_dbm = 0;

% Create an RTLSDR system object to receive samples from RTL-SDR
obj_rtlsdr = comm.SDRRTLReceiver(                      ...
                                    '0',               ...
            'CenterFrequency'    ,  center_freq,       ...
            'EnableTunerAGC'     ,  false,             ...
            'TunerGain'          ,  tuner_gain,        ...
            'SampleRate'         ,  samp_rate,         ...
            'SamplesPerFrame'    ,  samples_per_frame, ...
            'OutputDataType'     ,  'single',          ...
            'FrequencyCorrection',  0 );

% check if RTL-SDR is active
if isempty(sdrinfo(obj_rtlsdr.RadioAddress))
	error(['RTL-SDR failure. Please check connection to MATLAB using the "sdrinfo" command.']);
end

samples_vector = zeros(num_useful_frames, samples_per_frame);
samples_vector_fft_sev = zeros(num_useful_frames, samples_per_frame);

% dump some frames to not receive rubbish information
for i = 1:1:num_dump_frames
	rubbish_data = step(obj_rtlsdr);
end

disp(sprintf(['Center freqency = ', num2str(center_freq / 1e6), ' MHz\n', ...
      'Bandwidth = ', num2str(samp_rate / 1e6), ' MHz\n',                 ...
      'Precision of one dot at the graph = ', num2str(samp_rate / samples_per_frame / 1e3), ' kHz\n']));

% Receive one sample vector from RTL-SDR
for i = 1 : num_useful_frames
	samples_vector(i, :) = step(obj_rtlsdr);
end

% Use FFT to samples vector to provide information in frequency domain
for i = 1 : num_useful_frames
	samples_vector_fft_sev(i, :) = fft(samples_vector(i, :), samples_per_frame);
end
samples_vector_fft = add_several_fft_results (samples_vector_fft_sev);

% delete noise from FFT results using moving average algorithm
samples_vector_fft = moving_average(samples_vector_fft, average_factor);

% Select target frequency band from all frequency domain vector
[target_vector_fft, x_target_freq_axis] = select_target_band_of_array(samples_vector_fft, center_freq, samp_rate, target_freq_begin, target_freq_end);
%target_vector_fft = samples_vector_fft(500 : 900);

% Calculate signal power of target frequency band
[power_mw, power_dbm] = calculate_signal_power(target_vector_fft);

% Print calculated signal power
disp(sprintf(['Linear power = ', num2str(power_mw), ' mW\nLog power = ', num2str(power_dbm), ' dBm\n']));


% Draw a plot with 6 graphs
% Time-domain real signal (2D)
subplot(3, 2, 1);
plot(abs(samples_vector(1, :)));
title('Time domain real');
xlabel('Time');
ylabel('Amplitude');

% Time-domain complex signal (3D)
subplot(3, 2, 2);
time_axis = (1 : numel(samples_vector(1, :)));
plot3(time_axis, real(samples_vector(1, :)), imag(samples_vector(1, :)));
title('Time domain complex');
xlabel('???');
ylabel('???');
zlabel('???');

% Freqency-domain full received signal linear
subplot(3, 2, 3);
%x_freq_axis = (center_freq - samp_rate / 2) : ceil(samp_rate / samples_per_frame) : (center_freq + samp_rate / 2);
%x_freq_axis = x_freq_axis(average_factor/2 : end - average_factor/2 + 1);
%  disp('lol');
%  disp(numel(x_freq_axis));
%  disp(numel(samples_vector_fft));
%  disp('lol');
x_freq_axis = 1 : samples_per_frame - average_factor;
plot(x_freq_axis, abs(samples_vector_fft));
title('Frequency domain full signal, linear');
xlabel('Frequency');
ylabel('Amplitude, mW');

% Freqency-domain target signal linear
subplot(3, 2, 4);
plot(x_target_freq_axis, abs(target_vector_fft));
%plot(abs(target_vector_fft));
title('Frequency domain target signal, linear');
xlabel('Frequency');
ylabel('Amplitude, mW');

% Freqency-domain full received signal log
subplot(3, 2, 5);
%  x_freq_axis = (center_freq - samp_rate / 2) : ceil(samp_rate / samples_per_frame) : (center_freq + samp_rate / 2);
%  x_freq_axis = x_freq_axis(average_factor/2 : end - average_factor/2 + 1);
plot(x_freq_axis, 10 * log10(abs(samples_vector_fft)));
title('Frequency domain full signal, log');
xlabel('Frequency');
ylabel('Amplitude, dBm');

% Freqency-domain target signal log
subplot(3, 2, 6);
plot(x_target_freq_axis, 10 * log10(abs(target_vector_fft)));
%plot(10 * log10(abs(target_vector_fft)));
title('Frequency domain target signal, log');
xlabel('Frequency');
ylabel('Amplitude, dBm');

sgtitle('RF signal power meter prototype');
