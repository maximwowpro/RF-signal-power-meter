%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   20.02.2019

center_freq       = 100e6;
tuner_gain        = 40;    	 % dB
samp_rate         = 2e6;
samples_per_frame = 4096;

num_dump_frames = 100;		% We have to dump some frames before receiving information from RTL-SDR to not receive rubbish.

average_factor_1 = 8;
average_factor_2 = 64;
average_factor_3 = 256;

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

% dump some frames to not receive rubbish information
for i = 1:1:num_dump_frames
	rubbish_data = step(obj_rtlsdr);
end

disp(sprintf(['Center freqency = ', num2str(center_freq / 1e6), ' MHz\n', ...
      'Bandwidth = ', num2str(samp_rate / 1e6), ' MHz\n',                 ...
      'Precision of one dot at the graph = ', num2str(samp_rate / samples_per_frame / 1e3), ' kHz\n']));

% Receive one sample vector from RTL-SDR
samples_vector = step(obj_rtlsdr);

fft_non_average = fft(samples_vector);

% Smooth signal using recursion moving average
samples_vector_averaging_1 = moving_average(samples_vector, average_factor_1);
samples_vector_averaging_2 = moving_average(samples_vector, average_factor_2);
samples_vector_averaging_3 = moving_average(samples_vector, average_factor_3);

fft_average_time_1 = abs(fft(samples_vector_averaging_1));
fft_average_time_2 = abs(fft(samples_vector_averaging_2));
fft_average_time_3 = abs(fft(samples_vector_averaging_3));

fft_average_freq_1 = abs(moving_average(fft_non_average, average_factor_1));
fft_average_freq_2 = abs(moving_average(fft_non_average, average_factor_2));
fft_average_freq_3 = abs(moving_average(fft_non_average, average_factor_3));

% Calculate magnitude of complex numbers
samples_vector = abs(samples_vector);
samples_vector_averaging_1 = abs(samples_vector_averaging_1);
samples_vector_averaging_2 = abs(samples_vector_averaging_2);
samples_vector_averaging_3 = abs(samples_vector_averaging_3);

fft_non_average = abs(fft_non_average);

% Draw a plot
%------------------------------------------------------
subplot(4, 3, 1);
plot(samples_vector);
title('Time domain without averaging');
xlabel('Time');
ylabel('U(t)');

subplot(4, 3, 2);
plot(10 * log10(fft_non_average));
title('FFT without averaging');
xlabel('Frequency');
ylabel('mW');

%------------------------------------------------------
subplot(4, 3, 4);
plot(samples_vector_averaging_1);
title(strcat('Time domain with average factor = ', num2str(average_factor_1)));
xlabel('Time');
ylabel('U(t)');

subplot(4, 3, 5);
plot(10 * log10(fft_average_time_1));
title('FFT with average in time domain');
xlabel('Frequency');
ylabel('mW');

subplot(4, 3, 6);
plot(10 * log10(fft_average_freq_1));
title('FFT with average in frequency domain');
xlabel('Frequency');
ylabel('mW');


%------------------------------------------------------
subplot(4, 3, 7);
plot(samples_vector_averaging_2);
title(strcat('Time domain with average factor = ', num2str(average_factor_2)));
xlabel('Time');
ylabel('U(t)');

subplot(4, 3, 8);
plot(10 * log10(fft_average_time_2));
title('FFT with average in time domain');
xlabel('Frequency');
ylabel('mW');

subplot(4, 3, 9);
plot(10 * log10(fft_average_freq_2));
title('FFT with average in frequency domain');
xlabel('Frequency');
ylabel('mW');

%------------------------------------------------------
subplot(4, 3, 10);
plot(samples_vector_averaging_3);
title(strcat('Time domain with average factor = ', num2str(average_factor_3)));
xlabel('Time');
ylabel('U(t)');

subplot(4, 3, 11);
plot(10 * log10(fft_average_time_3));
title('FFT with average in time domain');
xlabel('Frequency');
ylabel('mW');

subplot(4, 3, 12);
plot(10 * log10(fft_average_freq_3));
title('FFT with average in frequency domain');
xlabel('Frequency');
ylabel('mW');


sgtitle('Test moving average in time and frequency domain');
