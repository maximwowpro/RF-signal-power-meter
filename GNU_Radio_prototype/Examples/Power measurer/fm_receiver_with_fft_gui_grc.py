#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Receiver With Fft Gui Grc
# Generated: Tue Feb  5 16:29:36 2019
##################################################

if __name__ == '__main__':
	import ctypes
	import sys
	if sys.platform.startswith('linux'):
		try:
			x11 = ctypes.cdll.LoadLibrary('libX11.so')
			x11.XInitThreads()
		except:
			print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
from gnuradio import qtgui


class fm_receiver_with_fft_gui_grc(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "Fm Receiver With Fft Gui Grc")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("Fm Receiver With Fft Gui Grc")
		qtgui.util.check_set_qss()
		try:
			self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		except:
			pass
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)

		self.settings = Qt.QSettings("GNU Radio", "fm_receiver_with_fft_gui_grc")
		self.restoreGeometry(self.settings.value("geometry").toByteArray())


		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 4.8e6
		self.heterodyne_freq = heterodyne_freq = -0.5e6
		self.center_sdr_hardware_freq = center_sdr_hardware_freq = 100e6

		##################################################
		# Blocks
		##################################################
		self.wbfm_receive = analog.wfm_rcv(
			quad_rate=480e3,
			audio_decimation=10,
		)
		self.vector_sink_if = blocks.vector_sink_c(1, 1024)
		self.stream_to_vector_if = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
		self.src_heterodyne = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, heterodyne_freq, 1, 0)
		self.src_hackrf = osmosdr.source( args="numchan=" + str(1) + " " + '' )
		self.src_hackrf.set_sample_rate(samp_rate)
		self.src_hackrf.set_center_freq(100*1e6, 0)
		self.src_hackrf.set_freq_corr(0, 0)
		self.src_hackrf.set_dc_offset_mode(0, 0)
		self.src_hackrf.set_iq_balance_mode(0, 0)
		self.src_hackrf.set_gain_mode(False, 0)
		self.src_hackrf.set_gain(10, 0)
		self.src_hackrf.set_if_gain(20, 0)
		self.src_hackrf.set_bb_gain(30, 0)
		self.src_hackrf.set_antenna('', 0)
		self.src_hackrf.set_bandwidth(0, 0)

		self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
			1024, #size
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			center_sdr_hardware_freq - heterodyne_freq, #fc
			samp_rate, #bw
			"", #name
			1 #number of inputs
		)
		self.qtgui_freq_sink_x_0.set_update_time(0.10)
		self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
		self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
		self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
		self.qtgui_freq_sink_x_0.enable_autoscale(False)
		self.qtgui_freq_sink_x_0.enable_grid(False)
		self.qtgui_freq_sink_x_0.set_fft_average(0.1)
		self.qtgui_freq_sink_x_0.enable_axis_labels(True)
		self.qtgui_freq_sink_x_0.enable_control_panel(False)

		if not True:
		  self.qtgui_freq_sink_x_0.disable_legend()

		if "complex" == "float" or "complex" == "msg_float":
		  self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

		labels = ['', '', '', '', '',
				  '', '', '', '', '']
		widths = [1, 1, 1, 1, 1,
				  1, 1, 1, 1, 1]
		colors = ["blue", "red", "green", "black", "cyan",
				  "magenta", "yellow", "dark red", "dark green", "dark blue"]
		alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
				  1.0, 1.0, 1.0, 1.0, 1.0]
		for i in xrange(1):
			if len(labels[i]) == 0:
				self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
			else:
				self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
			self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
			self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
			self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

		self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
		self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
		self.probe_vector_if = blocks.probe_signal_vc(1024)
		self.output_audio_final = audio.sink(48000, '', True)
		self.multiply_output_volume = blocks.multiply_const_vff((0.6, ))
		self.low_pass_filter = filter.fir_filter_ccf(10, firdes.low_pass(
			1, samp_rate, 70000, 20000, firdes.WIN_HAMMING, 6.76))
		self.IF_mixer = blocks.multiply_vcc(1)



		##################################################
		# Connections
		##################################################
		self.connect((self.IF_mixer, 0), (self.low_pass_filter, 0))
		self.connect((self.IF_mixer, 0), (self.qtgui_freq_sink_x_0, 0))
		self.connect((self.IF_mixer, 0), (self.stream_to_vector_if, 0))
		self.connect((self.IF_mixer, 0), (self.vector_sink_if, 0))
		self.connect((self.low_pass_filter, 0), (self.wbfm_receive, 0))
		self.connect((self.multiply_output_volume, 0), (self.output_audio_final, 0))
		self.connect((self.src_hackrf, 0), (self.IF_mixer, 1))
		self.connect((self.src_heterodyne, 0), (self.IF_mixer, 0))
		self.connect((self.stream_to_vector_if, 0), (self.probe_vector_if, 0))
		self.connect((self.wbfm_receive, 0), (self.multiply_output_volume, 0))

	def print_vector_sink_if(self):
		print str(len(self.vector_sink_if.data()))
		print (self.vector_sink_if.data())

	def closeEvent(self, event):
		self.settings = Qt.QSettings("GNU Radio", "fm_receiver_with_fft_gui_grc")
		self.settings.setValue("geometry", self.saveGeometry())
		event.accept()

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.src_heterodyne.set_sampling_freq(self.samp_rate)
		self.src_hackrf.set_sample_rate(self.samp_rate)
		self.qtgui_freq_sink_x_0.set_frequency_range(self.center_sdr_hardware_freq - self.heterodyne_freq, self.samp_rate)
		self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, 70000, 20000, firdes.WIN_HAMMING, 6.76))

	def get_heterodyne_freq(self):
		return self.heterodyne_freq

	def set_heterodyne_freq(self, heterodyne_freq):
		self.heterodyne_freq = heterodyne_freq
		self.src_heterodyne.set_frequency(self.heterodyne_freq)
		self.qtgui_freq_sink_x_0.set_frequency_range(self.center_sdr_hardware_freq - self.heterodyne_freq, self.samp_rate)

	def get_center_sdr_hardware_freq(self):
		return self.center_sdr_hardware_freq

	def set_center_sdr_hardware_freq(self, center_sdr_hardware_freq):
		self.center_sdr_hardware_freq = center_sdr_hardware_freq
		self.qtgui_freq_sink_x_0.set_frequency_range(self.center_sdr_hardware_freq - self.heterodyne_freq, self.samp_rate)


def main(top_block_cls=fm_receiver_with_fft_gui_grc, options=None):

	from distutils.version import StrictVersion
	if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
		style = gr.prefs().get_string('qtgui', 'style', 'raster')
		Qt.QApplication.setGraphicsSystem(style)
	qapp = Qt.QApplication(sys.argv)

	tb = top_block_cls()
	tb.start()
	tb.show()

	tb.print_vector_sink_if()

	def quitting():
		tb.stop()
		tb.wait()
	qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
	qapp.exec_()


if __name__ == '__main__':
	main()
