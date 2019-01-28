#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov  6 14:32:53 2018
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
        self.center_sdr_hardware_f = center_sdr_hardware_f = 99e6
        self.sdr_hardware_f_slider = sdr_hardware_f_slider = center_sdr_hardware_f
        self.low_pass_filter_cutoff_f = low_pass_filter_cutoff_f = 70e3
        self.if_slider = if_slider = -1.50e6
        self.volume_slider = volume_slider = 0.6
        self.squelch_slider = squelch_slider = -60
        self.samp_rate = samp_rate = 4.8e6
        self.low_pass_trans_width_slider = low_pass_trans_width_slider = 20e3
        self.low_pass_filter_cutoff_f_slider = low_pass_filter_cutoff_f_slider = low_pass_filter_cutoff_f
        self.curr_f_label = curr_f_label = sdr_hardware_f_slider - if_slider

        ##################################################
        # Blocks
        ##################################################
        self._volume_slider_range = Range(0.2, 3, 0.2, 0.6, 200)
        self._volume_slider_win = RangeWidget(self._volume_slider_range, self.set_volume_slider, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_slider_win)
        self._squelch_slider_range = Range(-80, -30, 5, -60, 200)
        self._squelch_slider_win = RangeWidget(self._squelch_slider_range, self.set_squelch_slider, 'Squelch', "counter_slider", float)
        self.top_grid_layout.addWidget(self._squelch_slider_win)
        self._sdr_hardware_f_slider_range = Range(93e6, 106e6, 50e3, center_sdr_hardware_f, 200)
        self._sdr_hardware_f_slider_win = RangeWidget(self._sdr_hardware_f_slider_range, self.set_sdr_hardware_f_slider, 'SDR frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sdr_hardware_f_slider_win)
        self._low_pass_trans_width_slider_range = Range(5e3, 50e3, 5e3, 20e3, 200)
        self._low_pass_trans_width_slider_win = RangeWidget(self._low_pass_trans_width_slider_range, self.set_low_pass_trans_width_slider, 'Filter trans width fr', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_pass_trans_width_slider_win)
        self._low_pass_filter_cutoff_f_slider_range = Range(low_pass_filter_cutoff_f - 40e3, low_pass_filter_cutoff_f + 40e3, 5e3, low_pass_filter_cutoff_f, 200)
        self._low_pass_filter_cutoff_f_slider_win = RangeWidget(self._low_pass_filter_cutoff_f_slider_range, self.set_low_pass_filter_cutoff_f_slider, 'Filter cutoff freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_pass_filter_cutoff_f_slider_win)
        self._if_slider_range = Range(-5e6, 5e6, 50e3, -1.50e6, 200)
        self._if_slider_win = RangeWidget(self._if_slider_range, self.set_if_slider, 'IF frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_slider_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	sdr_hardware_f_slider - if_slider, #fc
        	0, #bw
        	"FFT audio", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	sdr_hardware_f_slider - if_slider, #fc
        	0, #bw
        	"FFT before filter", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
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
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(sdr_hardware_f_slider, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(30, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, low_pass_filter_cutoff_f_slider, low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))
        self._curr_f_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._curr_f_label_formatter = None
        else:
          self._curr_f_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._curr_f_label_tool_bar.addWidget(Qt.QLabel('Current Frequency'+": "))
        self._curr_f_label_label = Qt.QLabel(str(self._curr_f_label_formatter(self.curr_f_label)))
        self._curr_f_label_tool_bar.addWidget(self._curr_f_label_label)
        self.top_grid_layout.addWidget(self._curr_f_label_tool_bar)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume_slider, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_1 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_standard_squelch_0 = analog.standard_squelch(audio_rate=48e3)
        self.analog_standard_squelch_0.set_threshold(squelch_slider)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, if_slider, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_standard_squelch_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_wfm_rcv_1, 0), (self.analog_standard_squelch_0, 0))
        self.connect((self.analog_wfm_rcv_1, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_sdr_hardware_f(self):
        return self.center_sdr_hardware_f

    def set_center_sdr_hardware_f(self, center_sdr_hardware_f):
        self.center_sdr_hardware_f = center_sdr_hardware_f
        self.set_sdr_hardware_f_slider(self.center_sdr_hardware_f)

    def get_sdr_hardware_f_slider(self):
        return self.sdr_hardware_f_slider

    def set_sdr_hardware_f_slider(self, sdr_hardware_f_slider):
        self.sdr_hardware_f_slider = sdr_hardware_f_slider
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.sdr_hardware_f_slider - self.if_slider, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sdr_hardware_f_slider - self.if_slider, 0)
        self.osmosdr_source_0.set_center_freq(self.sdr_hardware_f_slider, 0)
        self.set_curr_f_label(self._curr_f_label_formatter(self.sdr_hardware_f_slider - self.if_slider))

    def get_low_pass_filter_cutoff_f(self):
        return self.low_pass_filter_cutoff_f

    def set_low_pass_filter_cutoff_f(self, low_pass_filter_cutoff_f):
        self.low_pass_filter_cutoff_f = low_pass_filter_cutoff_f
        self.set_low_pass_filter_cutoff_f_slider(self.low_pass_filter_cutoff_f)

    def get_if_slider(self):
        return self.if_slider

    def set_if_slider(self, if_slider):
        self.if_slider = if_slider
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.sdr_hardware_f_slider - self.if_slider, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sdr_hardware_f_slider - self.if_slider, 0)
        self.set_curr_f_label(self._curr_f_label_formatter(self.sdr_hardware_f_slider - self.if_slider))
        self.analog_sig_source_x_1.set_frequency(self.if_slider)

    def get_volume_slider(self):
        return self.volume_slider

    def set_volume_slider(self, volume_slider):
        self.volume_slider = volume_slider
        self.blocks_multiply_const_vxx_0.set_k((self.volume_slider, ))

    def get_squelch_slider(self):
        return self.squelch_slider

    def set_squelch_slider(self, squelch_slider):
        self.squelch_slider = squelch_slider
        self.analog_standard_squelch_0.set_threshold(self.squelch_slider)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_f_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_low_pass_trans_width_slider(self):
        return self.low_pass_trans_width_slider

    def set_low_pass_trans_width_slider(self, low_pass_trans_width_slider):
        self.low_pass_trans_width_slider = low_pass_trans_width_slider
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_f_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_low_pass_filter_cutoff_f_slider(self):
        return self.low_pass_filter_cutoff_f_slider

    def set_low_pass_filter_cutoff_f_slider(self, low_pass_filter_cutoff_f_slider):
        self.low_pass_filter_cutoff_f_slider = low_pass_filter_cutoff_f_slider
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_f_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_curr_f_label(self):
        return self.curr_f_label

    def set_curr_f_label(self, curr_f_label):
        self.curr_f_label = curr_f_label
        Qt.QMetaObject.invokeMethod(self._curr_f_label_label, "setText", Qt.Q_ARG("QString", self.curr_f_label))


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
