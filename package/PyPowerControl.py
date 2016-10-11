# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/current.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Control(object):
    def setupUi(self, Control):
        Control.setObjectName(_fromUtf8("Control"))
        Control.resize(240, 181)
        self._speed = QtGui.QDoubleSpinBox(Control)
        self._speed.setGeometry(QtCore.QRect(130, 30, 91, 21))
        self._speed.setProperty("value", 0.2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self._speed.setFont(font)
        self._speed.setObjectName(_fromUtf8("_speed"))
        self._spLabel = QtGui.QLabel(Control)
        self._spLabel.setGeometry(QtCore.QRect(130, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._spLabel.setFont(font)
        self._spLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._spLabel.setObjectName(_fromUtf8("_spLabel"))
        self._port = QtGui.QSpinBox(Control)
        self._port.setGeometry(QtCore.QRect(20, 30, 91, 20))
        self._port.setProperty("value", 5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self._port.setFont(font)
        self._port.setObjectName(_fromUtf8("_port"))
        self._portLabel = QtGui.QLabel(Control)
        self._portLabel.setGeometry(QtCore.QRect(20, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._portLabel.setFont(font)
        self._portLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._portLabel.setObjectName(_fromUtf8("_portLabel"))
        self._limI = QtGui.QDoubleSpinBox(Control)
        self._limI.setGeometry(QtCore.QRect(20, 80, 91, 24))
        self._limI.setRange(0., 900.)
        font = QtGui.QFont()
        font.setPointSize(11)
        self._limI.setFont(font)
        self._limI.setObjectName(_fromUtf8("_limI"))
        self._limV = QtGui.QDoubleSpinBox(Control)
        self._limV.setGeometry(QtCore.QRect(130, 80, 91, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._limV.setFont(font)
        self._limV.setObjectName(_fromUtf8("_limV"))
        self._currLabel = QtGui.QLabel(Control)
        self._currLabel.setGeometry(QtCore.QRect(20, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._currLabel.setFont(font)
        self._currLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._currLabel.setObjectName(_fromUtf8("_currLabel"))
        self._voltLabel = QtGui.QLabel(Control)
        self._voltLabel.setGeometry(QtCore.QRect(130, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._voltLabel.setFont(font)
        self._voltLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._voltLabel.setObjectName(_fromUtf8("_voltLabel"))
        self._turnON = QtGui.QPushButton(Control)
        self._turnON.setGeometry(QtCore.QRect(10, 140, 110, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._turnON.setFont(font)
        self._turnON.setObjectName(_fromUtf8("_turnON"))
        self._turnOFF = QtGui.QPushButton(Control)
        self._turnOFF.setGeometry(QtCore.QRect(120, 140, 110, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self._turnOFF.setFont(font)
        self._turnOFF.setObjectName(_fromUtf8("_turnOFF"))
        self._update = QtGui.QPushButton(Control)
        self._update.setGeometry(QtCore.QRect(10, 110, 221, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._update.setFont(font)
        self._update.setObjectName(_fromUtf8("_update"))

        self.retranslateUi(Control)
        QtCore.QMetaObject.connectSlotsByName(Control)

    def retranslateUi(self, Control):
        Control.setWindowTitle(_translate("Control", "Form", None))
        self._spLabel.setText(_translate("Control", "0 [A/step]", None))
        self._portLabel.setText(_translate("Control", "port", None))
        self._currLabel.setText(_translate("Control", "limit I:", None))
        self._voltLabel.setText(_translate("Control", "limit V:", None))
        self._turnON.setText(_translate("Control", "ON", None))
        self._turnOFF.setText(_translate("Control", "OFF", None))
        self._update.setText(_translate("Control", "Update", None))

