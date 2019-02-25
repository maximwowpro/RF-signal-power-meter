%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.02.2019

center_freq       = 100e6;
tuner_gain        = 40;    	 % dB
samp_rate         = 2.8e6;
samples_per_frame = 4096;

num_dump_frames = 100;		% We have to dump some frames before receiving information from RTL-SDR to not receive rubbish.

target_freq_begin = 100.350e6;
target_freq_end   = 100.550e6;

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

samples_vector = zeros(1, samples_per_frame);
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
% Use FFT to samples vector to provide information in frequency domain
samples_vector_fft = fft(samples_vector, samples_per_frame);

% Extrude target frequency band from FFT samples vector
target_freq_band_fft_vector = select_target_band_of_array(samples_vector_fft, ...
							  center_freq,                                    ...
							  samp_rate,                                      ...
							  target_freq_begin,                              ...
							  target_freq_end );

samples_vector_fft = abs(samples_vector_fft);
target_freq_band_fft_vector = abs(target_freq_band_fft_vector);

% Draw a plot with 2 graphs (FFT of full samples vector and FFT of target frequency band)
subplot(2, 1, 1);
x_freq_axis = (center_freq - samp_rate / 2 : samp_rate / samples_per_frame : center_freq + samp_rate / 2 - 1);
plot(x_freq_axis, samples_vector_fft);
title('Full FFT');
xlabel('Frequency');
ylabel('Signal power');

subplot(2, 1, 2);
x_freq_axis = (target_freq_begin : samp_rate / samples_per_frame : target_freq_end);
numel(x_freq_axis)
numel(target_freq_band_fft_vector)
plot(x_freq_axis, target_freq_band_fft_vector(3 : end-1));
title('Target band FFT');
xlabel('Frequency');
ylabel('Signal power');

sgtitle('FFT of samples vector, received from RTL-SDR');
