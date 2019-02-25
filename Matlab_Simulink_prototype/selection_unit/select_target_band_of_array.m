%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   25.02.2019

function [target_vector] = select_target_band_of_array (fft_vector, center_freq, sample_rate, target_freq_begin, target_freq_end)

	% This function returns a "target vector", what is a part of FFT samples vector.
	% For example, your input is FFT samples vector with center freqency = 1 MHz, sample rate = 200 kHz and FFT size = 4096.
	% So, the step of one FFT sample is 200k / 4096 = 48.8 Hz.
	% If your target frequency band is 950 kHz till 1050 kHz. The function returns an array of 
	% FFT samples from 1024 to 3072, what represens our target frequency band.
	
	if (center_freq - (sample_rate / 2) > target_freq_begin)
		error('Invalid values of frequencies! target_freq_begin is too small.');
	elseif (center_freq + (sample_rate / 2) < target_freq_end)
		error('Invalid values of frequencies! target_freq_begin is too big.');
	end
	
	fft_size = numel(fft_vector);
	one_sample_freq_band = round(sample_rate / numel(fft_vector));
	
	begin_index = round((target_freq_begin - (center_freq - (sample_rate / 2))) / one_sample_freq_band);
	last_index  = fft_size - round((center_freq + (sample_rate / 2) - target_freq_end) / one_sample_freq_band);
	
	target_vector = fft_vector(begin_index : last_index);	
end
