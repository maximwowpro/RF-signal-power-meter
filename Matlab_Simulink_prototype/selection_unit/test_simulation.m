%   Created by Max Shvayuk.
%   This program is the part of the "RF signal power meter" project.
%   https://github.com/maximwowpro/RF-signal-power-meter
%   Kyiv, Ukraine.
%   01.03.2019

center_freq       = 100e6;
samp_rate         = 2e6;
samples_per_frame = 4096;


target_freq_begin = 99.5e6;
target_freq_end   = 99.7e6;

vect_full = 1 : samples_per_frame;

% vect_target should contain values from 1024 till 1434 and its size should be 411
vect_target = select_target_band_of_array(vect_full, center_freq, samp_rate, target_freq_begin, target_freq_end);

disp(numel(vect_target));
disp(vect_target);

