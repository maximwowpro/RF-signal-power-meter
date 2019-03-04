%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   03.03.2019

function [average_fft_result] = add_several_fft_results (several_ffts)
	[num_rows, num_columns] = size(several_ffts);
	
	for i = 1 : num_columns
		average_fft_result(i) = sum(several_ffts(:, i)') / num_rows;
	end
end
