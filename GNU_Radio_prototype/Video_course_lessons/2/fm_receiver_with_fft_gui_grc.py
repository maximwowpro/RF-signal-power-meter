#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Receiver With Fft Gui Grc
# Generated: Thu Feb 21 23:39:37 2019
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
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
        self.samp_rate = samp_rate = 32e3
        self.width = width = samp_rate/8
        self.cutoff_freq_low = cutoff_freq_low = samp_rate/8
        self.cutoff_freq_high = cutoff_freq_high = samp_rate/8

        ##################################################
        # Blocks
        ##################################################
        self._width_range = Range(samp_rate/1000, samp_rate/2, 1000, samp_rate/8, 200)
        self._width_win = RangeWidget(self._width_range, self.set_width, "width", "counter_slider", float)
        self.top_grid_layout.addWidget(self._width_win)
        self._cutoff_freq_low_range = Range(samp_rate/1000, samp_rate/2, 1000, samp_rate/8, 200)
        self._cutoff_freq_low_win = RangeWidget(self._cutoff_freq_low_range, self.set_cutoff_freq_low, "cutoff_freq_low", "counter_slider", float)
        self.top_grid_layout.addWidget(self._cutoff_freq_low_win)
        self._cutoff_freq_high_range = Range(samp_rate/1000, samp_rate/2, 1000, samp_rate/8, 200)
        self._cutoff_freq_high_win = RangeWidget(self._cutoff_freq_high_range, self.set_cutoff_freq_high, "cutoff_freq_high", "counter_slider", float)
        self.top_grid_layout.addWidget(self._cutoff_freq_high_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
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
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)

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
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, cutoff_freq_low, cutoff_freq_high, width, firdes.WIN_HAMMING, 6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.band_pass_filter_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_receiver_with_fft_gui_grc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_width(self.samp_rate/8)
        self.set_cutoff_freq_low(self.samp_rate/8)
        self.set_cutoff_freq_high(self.samp_rate/8)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.cutoff_freq_low, self.cutoff_freq_high, self.width, firdes.WIN_HAMMING, 6.76))

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.cutoff_freq_low, self.cutoff_freq_high, self.width, firdes.WIN_HAMMING, 6.76))

    def get_cutoff_freq_low(self):
        return self.cutoff_freq_low

    def set_cutoff_freq_low(self, cutoff_freq_low):
        self.cutoff_freq_low = cutoff_freq_low
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.cutoff_freq_low, self.cutoff_freq_high, self.width, firdes.WIN_HAMMING, 6.76))

    def get_cutoff_freq_high(self):
        return self.cutoff_freq_high

    def set_cutoff_freq_high(self, cutoff_freq_high):
        self.cutoff_freq_high = cutoff_freq_high
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.cutoff_freq_low, self.cutoff_freq_high, self.width, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=fm_receiver_with_fft_gui_grc, options=None):

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
