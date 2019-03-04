%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.03.2019

function [power_mw, power_dbm] = calculate_signal_power (target_band)

	% This function calculates the power of RF signal, which occupies some frequency band.
	% target_band should be a part of amplitude-frequency specter in frequencies, what our signal operates with.

	% Convert complex numbers to real
	target_band = abs(target_band);
	
	% Power of freqency band is the su of all FFT samples, which represents this band
	power_mw = sum(target_band);
	
	% Convert linear value to logarithmic
	power_dbm = log10(power_mw) * 10;

end
