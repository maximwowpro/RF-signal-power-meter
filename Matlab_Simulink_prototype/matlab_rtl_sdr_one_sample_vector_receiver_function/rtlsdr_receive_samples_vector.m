%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.02.2019

function [samples_vect] = rtlsdr_receive_samples_vector (rtlsdr_obj, center_freq, gain, samp_rate, samples_per_frame)

	% This function receives the vector of samples from RTL SDR.
	rtlsdr_obj.CenterFrequency = center_freq;
	rtlsdr_obj.TunerGain = gain;
	rtlsdr_obj.SampleRate = samp_rate;
	SamplesPerFrame = samples_per_frame;
	
	samples_vect = step(rtlsdr_obj);
end
