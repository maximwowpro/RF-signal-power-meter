#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jan 30 23:34:03 2019
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
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
        self.heterodyne_freq = heterodyne_freq = 915*1e6
        self.gain_src = gain_src = 3*10e-6
        self.gain_fm = gain_fm = 32768
        self.samp_rate = samp_rate = 640000
        self.heterodyne_freq_slider = heterodyne_freq_slider = heterodyne_freq
        self.gain_src_slider = gain_src_slider = gain_src
        self.gain_fm_slider = gain_fm_slider = gain_fm
        self.center_freq = center_freq = 915e6

        ##################################################
        # Blocks
        ##################################################
        self._heterodyne_freq_slider_range = Range(heterodyne_freq-10*1e6, heterodyne_freq+10*1e6, 1e5, heterodyne_freq, 200)
        self._heterodyne_freq_slider_win = RangeWidget(self._heterodyne_freq_slider_range, self.set_heterodyne_freq_slider, 'Heterodyne freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._heterodyne_freq_slider_win)
        self._gain_src_slider_range = Range(gain_src-10*1e-6, gain_src+10*10e-6, 1*10e-7, gain_src, 200)
        self._gain_src_slider_win = RangeWidget(self._gain_src_slider_range, self.set_gain_src_slider, 'Gain src', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_src_slider_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate*30, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(0, 100)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
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
        self._gain_fm_slider_range = Range(gain_fm-10e3, gain_fm+100e3, 1e3, gain_fm, 200)
        self._gain_fm_slider_win = RangeWidget(self._gain_fm_slider_range, self.set_gain_fm_slider, 'Gain FM', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_fm_slider_win)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((gain_src_slider, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, '/home/max/Work dir/_University/Digilent/RF-signal-power-meter/GNU_Radio_prototype/Examples/FM transmitter/audio_fifo.fifo', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.audio_sink_0 = audio.sink(32000, '', True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=32000,
        	quad_rate=640000,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, heterodyne_freq_slider, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_wfm_tx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_heterodyne_freq(self):
        return self.heterodyne_freq

    def set_heterodyne_freq(self, heterodyne_freq):
        self.heterodyne_freq = heterodyne_freq
        self.set_heterodyne_freq_slider(self.heterodyne_freq)

    def get_gain_src(self):
        return self.gain_src

    def set_gain_src(self, gain_src):
        self.gain_src = gain_src
        self.set_gain_src_slider(self.gain_src)

    def get_gain_fm(self):
        return self.gain_fm

    def set_gain_fm(self, gain_fm):
        self.gain_fm = gain_fm
        self.set_gain_fm_slider(self.gain_fm)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate*30)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_heterodyne_freq_slider(self):
        return self.heterodyne_freq_slider

    def set_heterodyne_freq_slider(self, heterodyne_freq_slider):
        self.heterodyne_freq_slider = heterodyne_freq_slider
        self.analog_sig_source_x_0.set_frequency(self.heterodyne_freq_slider)

    def get_gain_src_slider(self):
        return self.gain_src_slider

    def set_gain_src_slider(self, gain_src_slider):
        self.gain_src_slider = gain_src_slider
        self.blocks_multiply_const_vxx_1.set_k((self.gain_src_slider, ))

    def get_gain_fm_slider(self):
        return self.gain_fm_slider

    def set_gain_fm_slider(self, gain_fm_slider):
        self.gain_fm_slider = gain_fm_slider

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate*30)


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
