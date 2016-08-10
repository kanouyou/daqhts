# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/monitor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import matplotlib
from   matplotlib.backends import qt_compat
from   matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from   matplotlib.figure   import Figure

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName(_fromUtf8("Monitor"))
        Monitor.resize(649, 388)
        self._plabel = []
        self._port = []
        self._display = []
        ## port
        self.SetPort(Monitor)
        # port label
        self.SetLabel(Monitor)
        # lcd number
        self.SetLcdDisplay(Monitor)

        font = QtGui.QFont()
        font.setPointSize(11)

        self._start = QtGui.QPushButton(Monitor)
        self._start.setGeometry(QtCore.QRect(10, 240, 91, 21))
        self._start.setFont(font)
        self._start.setObjectName(_fromUtf8("_start"))
        self._stop = QtGui.QPushButton(Monitor)
        self._stop.setGeometry(QtCore.QRect(10, 270, 91, 21))
        self._stop.setFont(font)
        self._stop.setObjectName(_fromUtf8("_stop"))
        self._quit = QtGui.QPushButton(Monitor)
        self._quit.setGeometry(QtCore.QRect(10, 300, 91, 21))
        self._quit.setFont(font)
        self._quit.setObjectName(_fromUtf8("_quit"))

        # matplotlib canvas
        self._fig = Figure(facecolor="whitesmoke")
        self.plot = FigureCanvas(self._fig)
        self.plot.setGeometry(QtCore.QRect(120, 10, 521, 371))
        self.plot.setObjectName(_fromUtf8("monitor"))
        self.plot.setParent(Monitor)

        self.retranslateUi(Monitor)
        QtCore.QObject.connect(self._quit, QtCore.SIGNAL(_fromUtf8("clicked()")), Monitor.close)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        Monitor.setWindowTitle(_translate("Monitor", "Form", None))
        self._start.setText(_translate("Monitor", "Start", None))
        self._stop.setText(_translate("Monitor", "Stop", None))
        self._quit.setText(_translate("Monitor", "Quit", None))

    ## set port label
    def SetLabel(self, mainwin):
        numoflabel = 3
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        for i in range(numoflabel):
            self._plabel.append( QtGui.QLabel(mainwin) )
        self._plabel[0].setGeometry(QtCore.QRect(10, 30, 101, 21))
        self._plabel[1].setGeometry(QtCore.QRect(10, 70, 101, 21))
        self._plabel[2].setGeometry(QtCore.QRect(10, 110, 101, 21))

        for i in range(len(self._plabel)):
            self._plabel[i].setFont(font)
            self._plabel[i].setText(_fromUtf8( "Port %i" %(i+1) ))
            self._plabel[i].setTextFormat(QtCore.Qt.AutoText)
            self._plabel[i].setScaledContents(False)
            self._plabel[i].setAlignment(QtCore.Qt.AlignCenter)
            self._plabel[i].setWordWrap(False)
            self._plabel[i].setObjectName(_fromUtf8( "_pLabel%i" %(i+1) ))

    ## set port address
    def SetPort(self, mainwin):
        numofport = 3
        for i in range(numofport):
            self._port.append( QtGui.QSpinBox(mainwin) )

        self._port[0].setGeometry(QtCore.QRect(10, 10, 101, 21))
        self._port[0].setProperty("value", 20)
        self._port[1].setGeometry(QtCore.QRect(10, 50, 101, 21))
        self._port[1].setProperty("value", 6)
        self._port[2].setGeometry(QtCore.QRect(10, 90, 101, 21))
        self._port[2].setProperty("value", 12)
        for i in range(len(self._port)):
            self._port[i].setObjectName(_fromUtf8("_port%i" %(i+1)))


    ## set lcd display
    def SetLcdDisplay(self, mainwin):
        numoflcd = 3
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbol"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        for i in range(numoflcd):
            self._display.append( QtGui.QLCDNumber(mainwin) )

        self._display[0].setGeometry(QtCore.QRect(10, 140, 91, 16))
        self._display[1].setGeometry(QtCore.QRect(10, 160, 91, 16))
        self._display[2].setGeometry(QtCore.QRect(10, 180, 91, 16))

        for i in range(numoflcd):
            self._display[i].setFont(font)
            self._display[i].setSmallDecimalPoint(False)
            self._display[i].setNumDigits(14)
            self._display[i].setSegmentStyle(QtGui.QLCDNumber.Flat)
            self._display[i].setObjectName(_fromUtf8( "_num%i" %(i+1) ))



