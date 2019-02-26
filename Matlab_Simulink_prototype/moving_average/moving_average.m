%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   26.02.2019

function [out_vector] = moving_average (in_vector, average_factor)

	% This function counts a moving average of input vector and returns it.
	% It uses recursive algorithm. For more information see:
	% https://www.dspguide.com/ch15/5.html
	
	if (0 ~= mod(average_factor, 2))
		error('Invalid value of average_factor! It should be an even number.');
	end
	
	% This constants are required for many next operations
	vector_size = numel(in_vector);
	p =  average_factor / 2;
	n = (average_factor / 2) - 1;
	

	out_vector = zeros(1, vector_size);
	
	% Calculate moving average recursively

	% Calculate values with indexes from (average_factor / 2 + 1) till (vector_size - (average_factor / 2)) by default formula from article.
	% First element should be calculated manually:
	for i = 1 : average_factor
		out_vector(p + 1) = out_vector(p + 1) + in_vector(i);
	end
	
	for i = (p + 2) : (vector_size - n)
		out_vector(i) = out_vector(i-1) + in_vector(i + n) - in_vector(i - p - 1);
	end
	
	for i = (p + 1) : (vector_size - n)
		out_vector(i) = out_vector(i) / average_factor;
	end
	
	out_vector = out_vector(p+1 : end-p);
end
