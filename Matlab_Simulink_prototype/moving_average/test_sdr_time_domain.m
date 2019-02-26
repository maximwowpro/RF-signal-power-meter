%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   20.02.2019

center_freq       = 100e6;
tuner_gain        = 40;    	 % dB
samp_rate         = 250e3;
samples_per_frame = 4096;

num_dump_frames = 100;		% We have to dump some frames before receiving information from RTL-SDR to not receive rubbish.

average_factor_1 = 8;
average_factor_2 = 16;
average_factor_3 = 64;

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

samples_vector     = zeros(1, samples_per_frame);
samples_vector_fft = zeros(1, samples_per_frame);

% dump some frames to not receive rubbish information
for i = 1:1:num_dump_frames
	rubbish_data = step(obj_rtlsdr);
end

disp(sprintf(['Center freqency = ', num2str(center_freq / 1e6), ' MHz\n', ...
      'Bandwidth = ', num2str(samp_rate / 1e6), ' MHz\n',                 ...
      'Precision of one dot at the graph = ', num2str(samp_rate / samples_per_frame / 1e3), ' kHz\n']));

% Receive one sample vector from RTL-SDR
samples_vector = step(obj_rtlsdr);

% Smooth signal using recursion moving average
samples_vector_averaging_1 = moving_average(abs(samples_vector), average_factor_1);
samples_vector_averaging_2 = moving_average(abs(samples_vector), average_factor_2);
samples_vector_averaging_3 = moving_average(abs(samples_vector), average_factor_3);

% Calculate the magnitude of complex numbers, received from RTL-SDR to convert complex numbers to real numbers
samples_vector = abs(samples_vector);

% Draw a plot with 4 graphs
subplot(2, 2, 1);
plot(samples_vector);
title('Time domain without averaging');
xlabel('Time');
ylabel('U(t)');

subplot(2, 2, 2);
plot(samples_vector_averaging_1);
title(strcat('Time domain with average factor = ', num2str(average_factor_1)));
xlabel('Time');
ylabel('U(t)');

subplot(2, 2, 3);
plot(samples_vector_averaging_2);
title(strcat('Time domain with average factor = ', num2str(average_factor_2)));
xlabel('Time');
ylabel('U(t)');

subplot(2, 2, 4);
plot(samples_vector_averaging_3);
title(strcat('Time domain with average factor = ', num2str(average_factor_3)));
xlabel('Time');
ylabel('U(t)');


sgtitle('Samples vector, received from RTL-SDR and smoothed by moving average');
