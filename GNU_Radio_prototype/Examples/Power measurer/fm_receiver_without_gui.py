#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Created by Max Shvayuk.
# This program is the part of the "RF signal power meter" project.
# There is GNU Radio Companion script with similar functionality, at the link. Use it to understand how this program works.
# https://github.com/maximwowpro/RF-signal-power-meter
# Kyiv, Ukraine.
# 01.02.2019

import sys, getopt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
import osmosdr
from threading import Thread, Event, Lock
import time

DEFAULT_SDR_SRC_HARDWARE_FREQ = 100e6
DEFAULT_HETERODYNE_FREQ = 0.5e6
DEFAULT_SAMPLE_RATE = 4.8e6
DEFAULT_LOW_PASS_FILTER_CUTOFF_FREQ = 70e3
DEFAULT_LOW_PASS_FILTER_TRANS_WIDTH = 20e3
DEFAULT_OUTPUT_SIGNAL_GAIN = 0.6


class WorkerThread(Thread):
	def __init__(self, periodMiliseconds, taskFunction):
		super(WorkerThread, self).__init__()
		self.periodMiliseconds = periodMiliseconds
		self.taskFunction = taskFunction
		self.stopRequest = Event()

	def run(self):
		while not self.stopRequest.isSet():
			self.taskFunction()
			time.sleep(self.periodMiliseconds)

	def join(self, timeout = None):
		self.stopRequest.set()
		super(WorkerThread, self).join(timeout)


class GR_fm_radio_receiver_without_gui(gr.top_block):

	def __init__(self, target_freq, samp_rate = DEFAULT_SAMPLE_RATE,
				 low_pass_filter_cutoff_freq = DEFAULT_LOW_PASS_FILTER_CUTOFF_FREQ,
				 low_pass_filter_trans_width = DEFAULT_LOW_PASS_FILTER_TRANS_WIDTH,
				 volume = DEFAULT_OUTPUT_SIGNAL_GAIN):
		gr.top_block.__init__(self, "FM receiver without GUI")
		self.counter = 0
		##################################################
		# Variables
		##################################################
		self.wbfm_freq = 0
		self.heterodyne_freq = 0
		self.center_sdr_hardware_freq = 0
		self.samp_rate = samp_rate
		self.low_pass_filter_cutoff_freq = low_pass_filter_cutoff_freq
		self.low_pass_filter_trans_width = low_pass_filter_trans_width
		self.output_audio_gain = volume
		if (0 == samp_rate):
			self.samp_rate = DEFAULT_SAMPLE_RATE
		if (0 == low_pass_filter_cutoff_freq):
			self.low_pass_filter_cutoff_freq = DEFAULT_LOW_PASS_FILTER_CUTOFF_FREQ
		if (0 == low_pass_filter_trans_width):
			self.low_pass_filter_trans_width = DEFAULT_LOW_PASS_FILTER_TRANS_WIDTH
		if (0 == volume):
			self.output_audio_gain = DEFAULT_OUTPUT_SIGNAL_GAIN

		self.calculate_frequencies (target_freq)

		##################################################
		# Blocks
		##################################################
		if ((self.audio_freq < 20e3) or (0 != self.samp_rate % self.wbfm_freq)):
			self.samp_rate = DEFAULT_SAMPLE_RATE
			self.wbfm_freq = DEFAULT_SAMPLE_RATE / 10
			print ("Error! Sample rate % WBFM frequency should be == 0\n" +
			       "Using default values: Sample rate = " + "%.1E"%(self.samp_rate) +
			       " Hz\nWBFM frequency = " + "%.1E"%(self.wbfm_freq) + " Hz\n")

		if ((self.audio_freq < 20e3) or (0 != self.wbfm_freq % self.audio_freq)):
			self.wbfm_freq = self.samp_rate / 10
			self.audio_freq = self.wbfm_freq / 10
			print ("Error! WBFM frequency % audio final frequency should be == 0\n" +
			       "Using default values:\nWBFM frequency = " + "%.1E"%(self.wbfm_freq) +
			       " Hz\nAudio final frequency = " + "%.1E"%(self.audio_freq) + " Hz\n")

		print ("Your FM radio settings:\nTarget frequency = " + "%.5g"%(target_freq) +
		       " Hz\nSample rate = " + "%.3g"%(self.samp_rate) +
		       " Hz \nLow pass filter cutoff frequency = " + "%.3g"%(self.low_pass_filter_cutoff_freq) +
		       " Hz \nLow pass filter transition width = " + "%.3g"%(self.low_pass_filter_trans_width) +
		       " Hz \nOutput signal gain (volume) = " + str(self.output_audio_gain) + "\n")

		self.wbfm_receive = analog.wfm_rcv(quad_rate=self.wbfm_freq,
										   audio_decimation=int(self.wbfm_freq / self.audio_freq),)

		self.vector_sink_if = blocks.vector_sink_c(1, 1024)

		self.src_heterodyne = analog.sig_source_c(self.samp_rate, analog.GR_COS_WAVE, self.heterodyne_freq, 1, 0)

		self.src_hackrf = osmosdr.source( args="numchan=" + str(1) + " " + '' )
		self.src_hackrf.set_sample_rate(self.samp_rate)
		self.src_hackrf.set_center_freq(self.center_sdr_hardware_freq, 0)
		self.src_hackrf.set_freq_corr(0, 0)
		self.src_hackrf.set_dc_offset_mode(0, 0)
		self.src_hackrf.set_iq_balance_mode(0, 0)
		self.src_hackrf.set_gain_mode(False, 0)
		self.src_hackrf.set_gain(10, 0)
		self.src_hackrf.set_if_gain(20, 0)
		self.src_hackrf.set_bb_gain(30, 0)
		self.src_hackrf.set_antenna('', 0)
		self.src_hackrf.set_bandwidth(0, 0)

		self.output_audio_final = audio.sink(int(self.audio_freq), '', True)

		self.multiply_output_volume = blocks.multiply_const_vff((self.output_audio_gain, ))

		self.low_pass_filter = filter.fir_filter_ccf(int(self.samp_rate / self.wbfm_freq),
														firdes.low_pass(1, self.samp_rate,
														self.low_pass_filter_cutoff_freq,
														self.low_pass_filter_trans_width,
														firdes.WIN_HAMMING, 6.76))
		self.IF_mixer = blocks.multiply_vcc(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.IF_mixer, 0), (self.low_pass_filter, 0))
		self.connect((self.IF_mixer, 0), (self.vector_sink_if, 0))
		self.connect((self.low_pass_filter, 0), (self.wbfm_receive, 0))
		self.connect((self.multiply_output_volume, 0), (self.output_audio_final, 0))
		self.connect((self.src_hackrf, 0), (self.IF_mixer, 1))
		self.connect((self.src_heterodyne, 0), (self.IF_mixer, 0))
		self.connect((self.wbfm_receive, 0), (self.multiply_output_volume, 0))

	def return_vector_if(self):
		arr = self.vector_sink_if.data()
		if self.counter == 5:
			print arr
		self.counter += 1
		# print len(arr)
		# for i in range (0, len(arr), 1):
		# 	print i# ("%.3f"%(arr[i].real) + " ; " + "%.3f"%(arr[i].imag))
		# print ("\n")

	def calculate_frequencies(self, target_freq):
		self.wbfm_freq = self.samp_rate / 10
		self.audio_freq = self.wbfm_freq / 10
		#Target frequency = SDR hardware source frequency - Heterodyne frequency
		#To understand this, read about Intermediate frequency and Heterodyning
		if (DEFAULT_SDR_SRC_HARDWARE_FREQ == target_freq):
			self.center_sdr_hardware_freq = DEFAULT_SDR_SRC_HARDWARE_FREQ + DEFAULT_HETERODYNE_FREQ
			self.heterodyne_freq = DEFAULT_HETERODYNE_FREQ
		else:
			self.center_sdr_hardware_freq = DEFAULT_SDR_SRC_HARDWARE_FREQ
			self.heterodyne_freq = DEFAULT_SDR_SRC_HARDWARE_FREQ - target_freq

def main (argv):
	target_freq = 0
	samp_rate = 0
	low_pass_filter_cutoff_freq = 0
	low_pass_filter_trans_width = 0
	volume = 0

	usage_str = "Usage: <script_name>.py -f <target Frequency> -s <Sample rate>(optional) -c <low pass filter Cutoff frequency>(optional) -t <low pass filter Trans width>(optional) -v <audio volume>(optional)\n"
	if (0 == len(argv)):
		print (usage_str)
	try:
		opts, args = getopt.getopt(argv,":h:f:s:c:t:v:",["targetfreq=", "samplerate=", "lowpasscutoff=", "lowpasstranswidth=", "volume="])
	except getopt.GetoptError:
		print (usage_str)
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			print (usage_str)
			sys.exit()
		elif opt in ("-f", "--targetfreq"):
			target_freq = arg
		elif opt in ("-s", "--samplerate"):
			samp_rate = arg
		elif opt in ("-c", "--lowpasscutoff"):
			low_pass_filter_cutoff_freq = arg
		elif opt in ("-t", "--lowpasstranswidth"):
			low_pass_filter_trans_width = arg
		elif opt in ("-v", "--volume"):
			volume = arg

	if (0 == target_freq):
		target_freq = DEFAULT_SDR_SRC_HARDWARE_FREQ + DEFAULT_HETERODYNE_FREQ
		print ("Target freqency not defined, using default target frequency, " +
		       "%.3E"%(target_freq) + " Hz\n")

	fm_receiver = GR_fm_radio_receiver_without_gui (float(target_freq), float(samp_rate),
	                                    float(low_pass_filter_cutoff_freq),
	                                    float(low_pass_filter_trans_width),
	                                    float(volume))

	interrogate_thread = WorkerThread(1, fm_receiver.return_vector_if)
	fm_receiver.start()
	interrogate_thread.start()

	try:
		raw_input('Press Enter to quit: ')
	except EOFError:
		pass
	fm_receiver.stop()
	fm_receiver.wait()


if __name__ == '__main__':
	main(sys.argv[1:])
