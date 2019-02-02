#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Created by Max Shvayuk.
# This program is the part of the "RF signal power meter" project.
# There is GNU Radio Companion script with similar functionality, at the link. Use it to understand how this program works.
# https://github.com/maximwowpro/RF-signal-power-meter
# Kyiv, Ukraine.
# 03.02.2019

import sys, getopt
from PyQt4 import Qt
from gnuradio.filter import firdes
import sip
from gnuradio import qtgui
from fm_receiver_without_gui import GR_fm_radio_receiver_without_gui
from fm_receiver_without_gui import \
	DEFAULT_SDR_SRC_HARDWARE_FREQ, \
	DEFAULT_HETERODYNE_FREQ, \
	DEFAULT_SAMPLE_RATE, \
	DEFAULT_LOW_PASS_FILTER_CUTOFF_FREQ, \
	DEFAULT_LOW_PASS_FILTER_TRANS_WIDTH, \
	DEFAULT_OUTPUT_SIGNAL_GAIN

QT_GUI_UPDATE_FREQUENCY = 0.01 #seconds

class GR_fm_radio_receiver_with_fft_gui (GR_fm_radio_receiver_without_gui):
	def __init__(self, target_freq, samp_rate = DEFAULT_SAMPLE_RATE,
				 low_pass_filter_cutoff_freq = DEFAULT_LOW_PASS_FILTER_CUTOFF_FREQ,
				 low_pass_filter_trans_width = DEFAULT_LOW_PASS_FILTER_TRANS_WIDTH,
				 volume = DEFAULT_OUTPUT_SIGNAL_GAIN,
				 gui_mode = 0):

		GR_fm_radio_receiver_without_gui.__init__(self,
												  target_freq,
												  samp_rate,
												  low_pass_filter_cutoff_freq,
												  low_pass_filter_trans_width,
												  volume)

		if (0 == gui_mode):
			pass
		elif (1 == gui_mode):
			# Init QT GUI
			self.qt_fft_gui = Qt.QWidget()
			self.qt_fft_gui.setWindowTitle("FM receiver with FFT GUI")
			qtgui.util.check_set_qss()
			try:
				self.qt_fft_gui.setWindowIcon(Qt.QIcon.fromTheme("gnuradio-grc"))
			except:
				pass

			self.qt_fft_gui.top_scroll_layout = Qt.QVBoxLayout()
			self.qt_fft_gui.setLayout(self.qt_fft_gui.top_scroll_layout)
			self.qt_fft_gui.top_scroll = Qt.QScrollArea()
			self.qt_fft_gui.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
			self.qt_fft_gui.top_scroll_layout.addWidget(self.qt_fft_gui.top_scroll)
			self.qt_fft_gui.top_scroll.setWidgetResizable(True)
			self.qt_fft_gui.top_widget = Qt.QWidget()
			self.qt_fft_gui.top_scroll.setWidget(self.qt_fft_gui.top_widget)
			self.qt_fft_gui.top_layout = Qt.QVBoxLayout(self.qt_fft_gui.top_widget)
			self.top_grid_layout = Qt.QGridLayout()
			self.qt_fft_gui.top_layout.addLayout(self.top_grid_layout)

			self.qt_fft_gui.settings = Qt.QSettings("GNU Radio", "fm_receiver_with_fft_gui")
			self.qt_fft_gui.restoreGeometry(self.qt_fft_gui.settings.value("geometry").toByteArray())

			self.qt_gui_fft_sink = qtgui.freq_sink_c(
				1024,                                                   # FFT array size
				firdes.WIN_BLACKMAN_hARRIS,                             # wintype
				self.center_sdr_hardware_freq - self.heterodyne_freq,   # FFT center freqency
				self.samp_rate,                                         # FFT bandwidth
				"FM receiver spectre",                                  # Title of FFT sink
				1                                                       # number of inputs
			)
			self.qt_gui_fft_sink.set_update_time(QT_GUI_UPDATE_FREQUENCY)
			self.qt_gui_fft_sink.set_y_axis(-140, 10)
			self.qt_gui_fft_sink.set_y_label('Relative Gain', 'dB')
			self.qt_gui_fft_sink.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
			self.qt_gui_fft_sink.enable_autoscale(False)
			self.qt_gui_fft_sink.enable_grid(True)
			self.qt_gui_fft_sink.set_fft_average(0.1)
			self.qt_gui_fft_sink.enable_axis_labels(True)
			self.qt_gui_fft_sink.enable_control_panel(True)

			# Configure settings of the FFT graph line
			self.line_label = 'Signal\npower at\ndifferent\nfrequencies'
			self.line_width = 2
			self.line_color = "blue"
			self.line_transparrency = 1.0
			self.qt_gui_fft_sink.set_line_label(0, self.line_label)
			self.qt_gui_fft_sink.set_line_width(0, self.line_width)
			self.qt_gui_fft_sink.set_line_color(0, self.line_color)
			self.qt_gui_fft_sink.set_line_alpha(0, self.line_transparrency)

			# Create a wrapper of C++ GNU Radio API to display it's results in QWidget window. This is a magic, don't try to understand it.
			self._qt_gui_fft_sink_win = sip.wrapinstance(self.qt_gui_fft_sink.pyqwidget(), Qt.QWidget)
			self.top_grid_layout.addWidget(self._qt_gui_fft_sink_win)

			# Connect Intermediate Frequency mixer to QT GUI to build graph
			self.connect((self.IF_mixer, 0), (self.qt_gui_fft_sink, 0))
		else:
			print ("You set invalid GUI_mode (-g) option argument (\"" + str(gui_mode) + "\". \nEnter \"0\" to run without GUI or \"1\" to run with FFT GUI. \nNow progran starts without GUI.")


def main (argv):
	target_freq = 0
	samp_rate = 0
	low_pass_filter_cutoff_freq = 0
	low_pass_filter_trans_width = 0
	volume = 0
	gui_mode = 0

	usage_str = "Usage: <script_name>.py -f <target Frequency> -s <Sample rate>(optional) " + \
				"-c <low pass filter Cutoff frequency>(optional) -t <low pass filter Trans width>(optional) " + \
				"-v <audio volume>(optional) -g <Disable / Enable GUI: 0 or 1>(optional)\n"
	if (0 == len(argv)):
		print (usage_str)
	try:
		# Set short and long program arguments (flags)
		opts, args = getopt.getopt(argv,
								   ":h:f:s:c:t:v:g:",
								   ["targetfreq=",
									"samplerate=",
									"lowpasscutoff=",
									"lowpasstranswidth=",
									"volume=",
									"guimode="])
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
		elif opt in ("-g", "--guimode"):
			gui_mode = arg

	if (0 == target_freq):
		target_freq = DEFAULT_SDR_SRC_HARDWARE_FREQ + DEFAULT_HETERODYNE_FREQ
		print ("Target freqency not defined, using default target frequency, " +
			   "%.3E"%(target_freq) + " Hz\n")

	# To work with int number, not with str
	gui_mode = int(gui_mode)

	if ((0 == gui_mode) or (1 == gui_mode)):
		if (1 == gui_mode):
			qapp = Qt.QApplication(sys.argv)

		fm_receiver = GR_fm_radio_receiver_with_fft_gui (float(target_freq), float(samp_rate),
											float(low_pass_filter_cutoff_freq),
											float(low_pass_filter_trans_width),
											float(volume),
											gui_mode)
		if (1 == gui_mode):
			print ("Run with FFT GUI.\n")
			fm_receiver.start()
			fm_receiver.qt_fft_gui.show()

			def stop_program ():
				fm_receiver.stop()
				fm_receiver.wait()

			qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), stop_program)
			qapp.exec_()
		elif (0 == gui_mode):
			print ("Run without FFT GUI.\n")
			fm_receiver.start()
			try:
				raw_input('Press Enter to quit: ')
			except EOFError:
				pass
			fm_receiver.stop()
			fm_receiver.wait()
	else:
		print ("You set invalid GUI_mode (-g) option argument (\"" + str(gui_mode) +
			   "\". \nEnter \"0\" to run without GUI or \"1\" to run with FFT GUI. \nNow progran aborts.")


if __name__ == '__main__':
	main(sys.argv[1:])
