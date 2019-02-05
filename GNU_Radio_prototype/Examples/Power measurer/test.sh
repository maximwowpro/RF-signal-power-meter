# This command launches the program in GUI mode. Target frequency = 100.5 MHz.
echo "This command launches the program in GUI mode. Target frequency = 100.5 MHz."
./fm_receiver_with_fft_gui.py -f 100500000 -s 1000000 -c 50000 -t 25000 -v 1 -g 1

# This command launches the program in mode without GUI. Target frequency = 98 MHz.
echo "This command launches the program in mode without GUI. Target frequency = 98 MHz"
./fm_receiver_with_fft_gui.py -f 98000000 -s 1000000 -c 50000 -t 25000 -v 1 -g 0

# This command launches the program in the default mode. Target frequency = default (100.5 MHz).
echo "This command launches the program in the default mode. Target frequency = default (100.5 MHz)."
./fm_receiver_with_fft_gui.py
