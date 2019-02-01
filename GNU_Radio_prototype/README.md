# TODO: add a note about installing HarckRF drivers

# GNU Radio prototype
##### Here you can see the first prototype of our system, created in **GNU Radio**. The Gnu radio _.grc_ file and the _Python_ script are provided in this fold.

***

## Gnu Radio installation manual
All information is described for Arch-based Linux distributives (Arch, Manjaro).

 Install **Python2 PyQt4**
GUI part of Gnu Radio is provided by Python2 PyQt4 framework.
1.  If installation has failed - you should delete all installed PyQt4 packages and install them again.
List of these packages: python-sip, python-pyqt4, python-sip-pyqt4, python2-pyqt4, python2-sip-pyqt4.
To watch the list of installed packages, run:
`pacman -Q | grep pyqt`
To delete package, run:
`sudo pacman -Rs package_name`

2. First of all, you need __SIP__ - converter from Python to C++.
Install next packages:
https://www.archlinux.org/packages/extra/x86_64/sip/
https://www.archlinux.org/packages/extra/x86_64/python-sip/
https://www.archlinux.org/packages/extra/x86_64/python2-sip/
To installing PyQt4. you need modifying version of __SIP__, install it with this PKGBUILT file:
https://gitlab.com/inemum/inemum_archlinux/raw/master/python-sip-pyqt4/PKGBUILD
To install the package using PKGBUILT file, run makepkg -sri in the directory with this file.

3. Download PKGBUILT, which installs PyQt4:
https://aur.archlinux.org/packages/python2-pyqt4/
Building of packages takes a lot of time (40-90 min).
When building finishes, you will be asked to install 3 packages: _pyqt4-common_, _python-pyqt4_ _python2-pyqt4_.
Press yes.

4. Installation complete. To verify that it is correct, launch Python2 interpreter and run these 2 commands:
`from PyQt4 import Qt`
`qwerty = Qt.QWidget()`
If PyQt4 installed correctly, you see error message something about _"program has crashed, core dumped"_.
If PyQt4 installed incorrectly, you see the error message _"QWidget is not defined"_.

5. Install GnuRadio packages:
_gnuradio_
_gnuradio-companion_
_gnuradio-osmosdr_

6. Verify the installation. Try to run any Gnu Radio _.grc_ script.
