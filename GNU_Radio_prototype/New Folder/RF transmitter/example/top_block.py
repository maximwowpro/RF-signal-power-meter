#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jan 31 14:49:54 2019
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
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.central_freq = central_freq = 100000000
        self.wbfm_out_quadrature_samp_rate = wbfm_out_quadrature_samp_rate = 250000
        self.wbfm_in_audio_samp_rate = wbfm_in_audio_samp_rate = 62500
        self.low_pass_gain = low_pass_gain = 0.9
        self.input_level = input_level = 0.9
        self.input_audio_samp_rate = input_audio_samp_rate = 44100
        self.central_freq_slider = central_freq_slider = central_freq

        ##################################################
        # Blocks
        ##################################################
        self._low_pass_gain_range = Range(0, 1, 0.01, 0.9, 200)
        self._low_pass_gain_win = RangeWidget(self._low_pass_gain_range, self.set_low_pass_gain, 'Gain after WBFM', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_pass_gain_win)
        self._input_level_range = Range(0, 10, 0.01, 0.9, 200)
        self._input_level_win = RangeWidget(self._input_level_range, self.set_input_level, 'Signal imput level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._input_level_win)
        self._central_freq_slider_range = Range(central_freq - 1*10e6, central_freq + 1*10e6, 1 * 1e5, central_freq, 200)
        self._central_freq_slider_win = RangeWidget(self._central_freq_slider_range, self.set_central_freq_slider, 'Central frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._central_freq_slider_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=625,
                decimation=441,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	wbfm_in_audio_samp_rate*4, #bw
        	"Signal before WBFM", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	central_freq_slider, #fc
        	wbfm_out_quadrature_samp_rate*4, #bw
        	"Final signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	wbfm_out_quadrature_samp_rate*4, #bw
        	"Signal after WBFM", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
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
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(wbfm_out_quadrature_samp_rate)
        self.osmosdr_sink_0.set_center_freq(central_freq_slider, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(40, 0)
        self.osmosdr_sink_0.set_if_gain(40, 0)
        self.osmosdr_sink_0.set_bb_gain(40, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	low_pass_gain, wbfm_out_quadrature_samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/max/Work/shit/GNU_radio/RF transmitter/example/audio.wav', True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((input_level, ))
        self.audio_sink_0_0 = audio.sink(input_audio_samp_rate, '', True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=wbfm_in_audio_samp_rate,
        	quad_rate=wbfm_out_quadrature_samp_rate,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_wfm_tx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_central_freq(self):
        return self.central_freq

    def set_central_freq(self, central_freq):
        self.central_freq = central_freq
        self.set_central_freq_slider(self.central_freq)

    def get_wbfm_out_quadrature_samp_rate(self):
        return self.wbfm_out_quadrature_samp_rate

    def set_wbfm_out_quadrature_samp_rate(self, wbfm_out_quadrature_samp_rate):
        self.wbfm_out_quadrature_samp_rate = wbfm_out_quadrature_samp_rate
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.central_freq_slider, self.wbfm_out_quadrature_samp_rate*4)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.wbfm_out_quadrature_samp_rate*4)
        self.osmosdr_sink_0.set_sample_rate(self.wbfm_out_quadrature_samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.low_pass_gain, self.wbfm_out_quadrature_samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_wbfm_in_audio_samp_rate(self):
        return self.wbfm_in_audio_samp_rate

    def set_wbfm_in_audio_samp_rate(self, wbfm_in_audio_samp_rate):
        self.wbfm_in_audio_samp_rate = wbfm_in_audio_samp_rate
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.wbfm_in_audio_samp_rate*4)

    def get_low_pass_gain(self):
        return self.low_pass_gain

    def set_low_pass_gain(self, low_pass_gain):
        self.low_pass_gain = low_pass_gain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.low_pass_gain, self.wbfm_out_quadrature_samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_input_level(self):
        return self.input_level

    def set_input_level(self, input_level):
        self.input_level = input_level
        self.blocks_multiply_const_vxx_0.set_k((self.input_level, ))

    def get_input_audio_samp_rate(self):
        return self.input_audio_samp_rate

    def set_input_audio_samp_rate(self, input_audio_samp_rate):
        self.input_audio_samp_rate = input_audio_samp_rate

    def get_central_freq_slider(self):
        return self.central_freq_slider

    def set_central_freq_slider(self, central_freq_slider):
        self.central_freq_slider = central_freq_slider
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.central_freq_slider, self.wbfm_out_quadrature_samp_rate*4)
        self.osmosdr_sink_0.set_center_freq(self.central_freq_slider, 0)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
