#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jan 31 16:06:08 2019
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
        self.center_sdr_hardware_freq = center_sdr_hardware_freq = 100e6
        self.low_pass_filter_cutoff_freq = low_pass_filter_cutoff_freq = 70e3
        self.heterodyne_freq_slider = heterodyne_freq_slider = -1.10e6
        self.hackrf_freq_slider = hackrf_freq_slider = center_sdr_hardware_freq
        self.samp_rate = samp_rate = 4.8e6
        self.output_final_volume_slider = output_final_volume_slider = 0.6
        self.low_pass_trans_width_slider = low_pass_trans_width_slider = 20e3
        self.low_pass_filter_cutoff_freq_slider = low_pass_filter_cutoff_freq_slider = low_pass_filter_cutoff_freq
        self.curr_if_freq_label = curr_if_freq_label = hackrf_freq_slider - heterodyne_freq_slider

        ##################################################
        # Blocks
        ##################################################
        self._output_final_volume_slider_range = Range(0.2, 3, 0.2, 0.6, 200)
        self._output_final_volume_slider_win = RangeWidget(self._output_final_volume_slider_range, self.set_output_final_volume_slider, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._output_final_volume_slider_win)
        self._low_pass_trans_width_slider_range = Range(5e3, 50e3, 5e3, 20e3, 200)
        self._low_pass_trans_width_slider_win = RangeWidget(self._low_pass_trans_width_slider_range, self.set_low_pass_trans_width_slider, 'Filter trans width fr', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_pass_trans_width_slider_win)
        self._heterodyne_freq_slider_range = Range(-5e6, 5e6, 50e3, -1.10e6, 200)
        self._heterodyne_freq_slider_win = RangeWidget(self._heterodyne_freq_slider_range, self.set_heterodyne_freq_slider, 'IF frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._heterodyne_freq_slider_win)
        self._hackrf_freq_slider_range = Range(center_sdr_hardware_freq - 1e6, center_sdr_hardware_freq + 1e6, 50e3, center_sdr_hardware_freq, 200)
        self._hackrf_freq_slider_win = RangeWidget(self._hackrf_freq_slider_range, self.set_hackrf_freq_slider, 'SDR frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._hackrf_freq_slider_win)
        self.wbfm_receive = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.src_heterodyne = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, heterodyne_freq_slider, 1, 0)
        self.src_hackrf = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.src_hackrf.set_sample_rate(samp_rate)
        self.src_hackrf.set_center_freq(hackrf_freq_slider, 0)
        self.src_hackrf.set_freq_corr(0, 0)
        self.src_hackrf.set_dc_offset_mode(0, 0)
        self.src_hackrf.set_iq_balance_mode(0, 0)
        self.src_hackrf.set_gain_mode(False, 0)
        self.src_hackrf.set_gain(10, 0)
        self.src_hackrf.set_if_gain(20, 0)
        self.src_hackrf.set_bb_gain(30, 0)
        self.src_hackrf.set_antenna('', 0)
        self.src_hackrf.set_bandwidth(0, 0)

        self.qtgui_freq_sink_hackrf = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	hackrf_freq_slider, #fc
        	4.8*1e6, #bw
        	"FFT before filter", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_hackrf.set_update_time(0.10)
        self.qtgui_freq_sink_hackrf.set_y_axis(-140, 10)
        self.qtgui_freq_sink_hackrf.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_hackrf.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_hackrf.enable_autoscale(False)
        self.qtgui_freq_sink_hackrf.enable_grid(False)
        self.qtgui_freq_sink_hackrf.set_fft_average(0.2)
        self.qtgui_freq_sink_hackrf.enable_axis_labels(True)
        self.qtgui_freq_sink_hackrf.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_hackrf.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_hackrf.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_hackrf.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_hackrf.set_line_label(i, labels[i])
            self.qtgui_freq_sink_hackrf.set_line_width(i, widths[i])
            self.qtgui_freq_sink_hackrf.set_line_color(i, colors[i])
            self.qtgui_freq_sink_hackrf.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_hackrf_win = sip.wrapinstance(self.qtgui_freq_sink_hackrf.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_hackrf_win)
        self.qtgui_freq_sink_after_wbfm = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	hackrf_freq_slider - heterodyne_freq_slider, #fc
        	48*1e3, #bw
        	"FFT audio", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_after_wbfm.set_update_time(0.10)
        self.qtgui_freq_sink_after_wbfm.set_y_axis(-140, 10)
        self.qtgui_freq_sink_after_wbfm.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_after_wbfm.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_after_wbfm.enable_autoscale(False)
        self.qtgui_freq_sink_after_wbfm.enable_grid(False)
        self.qtgui_freq_sink_after_wbfm.set_fft_average(0.2)
        self.qtgui_freq_sink_after_wbfm.enable_axis_labels(True)
        self.qtgui_freq_sink_after_wbfm.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_after_wbfm.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_after_wbfm.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_after_wbfm.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_after_wbfm.set_line_label(i, labels[i])
            self.qtgui_freq_sink_after_wbfm.set_line_width(i, widths[i])
            self.qtgui_freq_sink_after_wbfm.set_line_color(i, colors[i])
            self.qtgui_freq_sink_after_wbfm.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_after_wbfm_win = sip.wrapinstance(self.qtgui_freq_sink_after_wbfm.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_after_wbfm_win)
        self.qtgui_freq_sink_after_low_pass = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	hackrf_freq_slider - heterodyne_freq_slider, #fc
        	48*1e4, #bw
        	"FFT after filter", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_after_low_pass.set_update_time(0.10)
        self.qtgui_freq_sink_after_low_pass.set_y_axis(-140, 10)
        self.qtgui_freq_sink_after_low_pass.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_after_low_pass.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_after_low_pass.enable_autoscale(False)
        self.qtgui_freq_sink_after_low_pass.enable_grid(False)
        self.qtgui_freq_sink_after_low_pass.set_fft_average(0.2)
        self.qtgui_freq_sink_after_low_pass.enable_axis_labels(True)
        self.qtgui_freq_sink_after_low_pass.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_after_low_pass.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_after_low_pass.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_after_low_pass.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_after_low_pass.set_line_label(i, labels[i])
            self.qtgui_freq_sink_after_low_pass.set_line_width(i, widths[i])
            self.qtgui_freq_sink_after_low_pass.set_line_color(i, colors[i])
            self.qtgui_freq_sink_after_low_pass.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_after_low_pass_win = sip.wrapinstance(self.qtgui_freq_sink_after_low_pass.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_after_low_pass_win)
        self.output_audio_final = audio.sink(48000, '', True)
        self.multiply_output_volume = blocks.multiply_const_vff((output_final_volume_slider, ))
        self._low_pass_filter_cutoff_freq_slider_range = Range(low_pass_filter_cutoff_freq - 40e3, low_pass_filter_cutoff_freq + 40e3, 5e3, low_pass_filter_cutoff_freq, 200)
        self._low_pass_filter_cutoff_freq_slider_win = RangeWidget(self._low_pass_filter_cutoff_freq_slider_range, self.set_low_pass_filter_cutoff_freq_slider, 'Filter cutoff freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._low_pass_filter_cutoff_freq_slider_win)
        self.low_pass_filter = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, low_pass_filter_cutoff_freq_slider, low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))
        self._curr_if_freq_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._curr_if_freq_label_formatter = None
        else:
          self._curr_if_freq_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._curr_if_freq_label_tool_bar.addWidget(Qt.QLabel('Current Frequency'+": "))
        self._curr_if_freq_label_label = Qt.QLabel(str(self._curr_if_freq_label_formatter(self.curr_if_freq_label)))
        self._curr_if_freq_label_tool_bar.addWidget(self._curr_if_freq_label_label)
        self.top_grid_layout.addWidget(self._curr_if_freq_label_tool_bar)
        self.IF_mixer = blocks.multiply_vcc(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.IF_mixer, 0), (self.low_pass_filter, 0))
        self.connect((self.low_pass_filter, 0), (self.qtgui_freq_sink_after_low_pass, 0))
        self.connect((self.low_pass_filter, 0), (self.wbfm_receive, 0))
        self.connect((self.multiply_output_volume, 0), (self.output_audio_final, 0))
        self.connect((self.src_hackrf, 0), (self.IF_mixer, 1))
        self.connect((self.src_hackrf, 0), (self.qtgui_freq_sink_hackrf, 0))
        self.connect((self.src_heterodyne, 0), (self.IF_mixer, 0))
        self.connect((self.wbfm_receive, 0), (self.multiply_output_volume, 0))
        self.connect((self.wbfm_receive, 0), (self.qtgui_freq_sink_after_wbfm, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_sdr_hardware_freq(self):
        return self.center_sdr_hardware_freq

    def set_center_sdr_hardware_freq(self, center_sdr_hardware_freq):
        self.center_sdr_hardware_freq = center_sdr_hardware_freq
        self.set_hackrf_freq_slider(self.center_sdr_hardware_freq)

    def get_low_pass_filter_cutoff_freq(self):
        return self.low_pass_filter_cutoff_freq

    def set_low_pass_filter_cutoff_freq(self, low_pass_filter_cutoff_freq):
        self.low_pass_filter_cutoff_freq = low_pass_filter_cutoff_freq
        self.set_low_pass_filter_cutoff_freq_slider(self.low_pass_filter_cutoff_freq)

    def get_heterodyne_freq_slider(self):
        return self.heterodyne_freq_slider

    def set_heterodyne_freq_slider(self, heterodyne_freq_slider):
        self.heterodyne_freq_slider = heterodyne_freq_slider
        self.src_heterodyne.set_frequency(self.heterodyne_freq_slider)
        self.qtgui_freq_sink_after_wbfm.set_frequency_range(self.hackrf_freq_slider - self.heterodyne_freq_slider, 48*1e3)
        self.qtgui_freq_sink_after_low_pass.set_frequency_range(self.hackrf_freq_slider - self.heterodyne_freq_slider, 48*1e4)
        self.set_curr_if_freq_label(self._curr_if_freq_label_formatter(self.hackrf_freq_slider - self.heterodyne_freq_slider))

    def get_hackrf_freq_slider(self):
        return self.hackrf_freq_slider

    def set_hackrf_freq_slider(self, hackrf_freq_slider):
        self.hackrf_freq_slider = hackrf_freq_slider
        self.src_hackrf.set_center_freq(self.hackrf_freq_slider, 0)
        self.qtgui_freq_sink_hackrf.set_frequency_range(self.hackrf_freq_slider, 4.8*1e6)
        self.qtgui_freq_sink_after_wbfm.set_frequency_range(self.hackrf_freq_slider - self.heterodyne_freq_slider, 48*1e3)
        self.qtgui_freq_sink_after_low_pass.set_frequency_range(self.hackrf_freq_slider - self.heterodyne_freq_slider, 48*1e4)
        self.set_curr_if_freq_label(self._curr_if_freq_label_formatter(self.hackrf_freq_slider - self.heterodyne_freq_slider))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.src_heterodyne.set_sampling_freq(self.samp_rate)
        self.src_hackrf.set_sample_rate(self.samp_rate)
        self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_freq_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_output_final_volume_slider(self):
        return self.output_final_volume_slider

    def set_output_final_volume_slider(self, output_final_volume_slider):
        self.output_final_volume_slider = output_final_volume_slider
        self.multiply_output_volume.set_k((self.output_final_volume_slider, ))

    def get_low_pass_trans_width_slider(self):
        return self.low_pass_trans_width_slider

    def set_low_pass_trans_width_slider(self, low_pass_trans_width_slider):
        self.low_pass_trans_width_slider = low_pass_trans_width_slider
        self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_freq_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_low_pass_filter_cutoff_freq_slider(self):
        return self.low_pass_filter_cutoff_freq_slider

    def set_low_pass_filter_cutoff_freq_slider(self, low_pass_filter_cutoff_freq_slider):
        self.low_pass_filter_cutoff_freq_slider = low_pass_filter_cutoff_freq_slider
        self.low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.low_pass_filter_cutoff_freq_slider, self.low_pass_trans_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_curr_if_freq_label(self):
        return self.curr_if_freq_label

    def set_curr_if_freq_label(self, curr_if_freq_label):
        self.curr_if_freq_label = curr_if_freq_label
        Qt.QMetaObject.invokeMethod(self._curr_if_freq_label_label, "setText", Qt.Q_ARG("QString", self.curr_if_freq_label))


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
