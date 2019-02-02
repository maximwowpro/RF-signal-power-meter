# FM receiver without graphical user interface
Python 2.7 FM radio receiver program is presented here.  
I have used **HackRF** SDR in my tests, but it should correctly work with anoyher SDRs, supported by **osmosdr** library (for example, **RTL SDR**).  
You should have installed QT4 to run this program.  
To start it, just enter `./test.sh` in your terminal.  
GNU Radio packages should be installed to your Linux OS.  

### Files description:  
_test.sh_ - bash script with examples of commands how to launch a program. Run it to test!  
_fm\_receiver\_with\_fft\_gui.grc_ - GNU Radio Companion scheme file with algorithm of FM receiver. You can use it to watch how does it work.  
_fm_receiver_without_gui.py_ - this file contains **GR\_fm\_radio\_receiver\_without\_gui** - a class with basic FM receiver functional. It is a parent class for **GR\_fm\_radio\_receiver\_with\_fft\_gui**.  
_fm\_receiver\_with\_fft\_gui.py_ - this file contains **GR\_fm\_radio\_receiver\_with\_fft\_gui** - a class which provides availability to run FM receiver with QT FFT GUI.
