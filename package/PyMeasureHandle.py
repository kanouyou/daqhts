## @package PySlowControlHandle
#  class description:
#    thread for data taking and control the power supply

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import PyMonitorGui
import PyKeithleyHandle
import PyPowerControl
import PyCurrentSupply
import PyDataHandle
import PyLogHandle as log

from PyQt4 import QtGui, QtCore

filename = "measurement"
shunt_resistor = 0.25e-3

## class to read the random number for test
#
class PyTestThread(QtCore.QThread):

    ## data signal
    data_signal = QtCore.pyqtSignal(float, float, float)

    ## constructor
    def __init__(self, parent=None):
        super(PyTestThread, self).__init__(parent)
        self.stop = False

    ## setup gpib address
    def Initialize(self, gpib):
        self.stop = False
        for i in range(len(gpib)):
            print "set gpib: ", gpib[i]
            log.Info("set gpib: ", gpib[i])

    ## stop this thread
    def Stop(self):
        self.stop = True

    ## run this thread
    def Run(self):
        if self.stop==True:
            self.stop = False
        while True:
            if self.stop:
                return
            m1 = np.random.random()
            time.sleep(0.5)
            m2 = np.random.random() + np.random.random()
            time.sleep(0.5)
            m3 = np.random.random() / np.random.random()
            time.sleep(0.5)
            self.data_signal.emit(m1,m2,m3)
        self.Stop()
        self.finished.emit()


## class to handle the controller thread
#
class PyControlThread(QtCore.QThread):

    ## data signal (return voltage and current)
    data_signal = QtCore.pyqtSignal(float, float)

    ## switch signal
    #info_signal = QtCore.pyqtSignal(str)

    ## constructor
    def __init__(self, parent=None):
        super(PyControlThread, self).__init__(parent)
        self.switch = False
        self.ps = PyCurrentSupply.PyCurrentSupply()
        self.protI = 50.
        self.protV = 1.
        self.speed = 0.1

    ## initialization
    def Initialize(self, gpib, speed=0.1, protI=10., protV=5.):
        self.ps.SetGpib( gpib )
        self.protI = protI
        self.protV = protV
        self.speed = speed
        self.ps.SetProtectVolt()
        #info = self.ps.GetInstrInfo().split(",")
        #self.info_signal.emit(info[1])
        print "connected to ", self.ps.GetInstrInfo()
        print "set protection voltage to ", self.ps.GetProtectVolt(), " [V]"
        log.Info("connected to ", self.ps.GetInstrInfo())

    ## turn off the current supply
    def TurnOff(self):
        self.switch = False
        self.ps.TurnOff()

    ## turn on the current supply
    def TurnOn(self):
        self.switch = True
        self.ps.TurnOn()
        print "turn on the current supply."

    ## update
    def Update(self, speed, protI=None, protV=None):
        self.speed = speed
        if protI!=None:
            self.protI = protI
        if protV!=None:
            self.protV = protV

    ## run
    def Run(self):
        I0 = 0.01
        V0 = 0.001
        self.TurnOff()
        self.ps.SetCurrent(I0)
        self.ps.SetVoltage(V0)

        I = I0
        self.TurnOn()
        while True:
            cI = self.ps.GetCurrent()
            cV = self.ps.GetVoltage()
            if self.switch==False:
                self.TurnOff()
                print "turn off"
                break
            if cI>self.protI or cV>self.protV:
                self.TurnOff()
                print "voltage: ", cV, " current: ", cI
                print "turn off: exceeded over the protection current or voltage"
                break
            self.ps.SetSmartCurrent(I)
            self.data_signal.emit(cV, cI)
            time.sleep(0.5)
            I += self.speed
        self.TurnOff()
        self.finished.emit()



## class to read the data from instrument
#
class PyMeasureThread(QtCore.QThread):

    ## data signal
    data_signal = QtCore.pyqtSignal(float, float, float)

    ## info signal
    info_signal = QtCore.pyqtSignal(str, str, str)

    ## constructor
    def __init__(self, parent=None):
        super(PyMeasureThread, self).__init__(parent)
        self.stop = False
        self.monitor = [PyKeithleyHandle.PyKeithley(), \
                        PyKeithleyHandle.PyKeithley(), \
                        PyKeithleyHandle.PyKeithley()]
        print "connected gpib: ", self.monitor[0].GetGpibPort()

    ## setup gpib address
    def Initialize(self, gpib):
        self.stop = False
        info = []
        for i in range(len(gpib)):
            self.monitor[i].SetGpib( gpib[i] )
            instr = self.monitor[i].GetInstrInfo()
            print "/*******************************************************/"
            print " set gpib: ", gpib[i]
            print " instrument: ", instr
            print "/*******************************************************/"
            info.append( instr )
        for i in range(len(info)):
            item = info[i].split(",")
            info[i] = item[1]
        self.info_signal.emit( info[0], info[1], info[2] )

    ## stop this thread
    def Stop(self):
        self.stop = True

    ## run this thread
    def Run(self):
        if self.stop==True:
            self.stop = False
        while True:
            if self.stop:
                return
            m1 = self.monitor[0].Read()
            m2 = self.monitor[1].Read()
            m3 = self.monitor[2].Read()
            self.data_signal.emit(m1,m2,m3)
        self.Stop()
        self.finished.emit()



## class to handle the gui
#
class PyMonitorHandle(QtGui.QMainWindow, PyMonitorGui.Ui_Monitor):

    ## constructor
    def __init__(self, parent=None):
        super(PyMonitorHandle, self).__init__(parent)
        self.setupUi(self)
        self.SetGrid()
        self.SetButtom()
        self._cnt = 0

    ## setup run buttom
    def SetButtom(self):
        self._start.clicked.connect(self.RunGui)
        self._stop.clicked.connect(self.Stop)
        self.measure = PyMeasureThread()
        self.measure.data_signal.connect(self.Plot)
        self.measure.info_signal.connect(self.GetInfo)
        self.measure.finished.connect(self.Finish)

    ## run gui
    @QtCore.pyqtSlot()
    def RunGui(self):
        self.Initialization()
        self._start.setEnabled(False)
        self._stop.setEnabled(True)
        self.measure.Run()

    ## get instrument information
    @QtCore.pyqtSlot(str, str, str)
    def GetInfo(self, info1, info2, info3):
        info = [info1, info2, info3]
        for i in range(len(info)):
            self._plabel[i].setText(info[i])

    ## get dat from thread
    @QtCore.pyqtSlot(float, float, float)
    def Plot(self, data1, data2, data3):
        dt = time.time() - self._starttime
        data = np.array([data1, data2, data3], dtype="float")
        self._output.FillAll(time.time(), data)
        self.draw(dt, data)

    ## finished the data
    @QtCore.pyqtSlot()
    def Finish(self):
        self.measure.wait()
        self._start.setEnabled(True)
        self._stop.setEnabled(False)

    ## stop the data taking
    @QtCore.pyqtSlot()
    def Stop(self):
        self.measure.Stop()
        self._output.Close()
        #plt.savefig("meas.pdf")
        self.measure.wait()
        self._start.setEnabled(True)
        self._stop.setEnabled(False)

    ## initialization
    def Initialization(self):
        self._output = PyDataHandle.PyDataHandle(filename+str(self._cnt))
        self._starttime = time.time()
        self._data = {"m1":np.array([]), "m2":np.array([]), "m3":np.array([])}
        self._time = np.array([])
        gpib = []
        for i in range(len(self._port)):
            gpib.append( "GPIB1::%i::INSTR" %self._port[i].value() )
        self.measure.Initialize( gpib )
        self._cnt += 1

    ## sperate subplots
    def SetGrid(self):
        gs = gridspec.GridSpec(3,3)
        ax1 = self._fig.add_subplot( gs[0,0] )
        ax2 = self._fig.add_subplot( gs[0,1] )
        ax3 = self._fig.add_subplot( gs[0,2] )
        ax4 = self._fig.add_subplot( gs[1,0:] )
        ax5 = self._fig.add_subplot( gs[2,0:] )
        self._ax = [ax1, ax2, ax3, ax4, ax5]
        # setup label
        for i in range(len(self._ax)):
            self._ax[i].set_ylabel("Voltage [V]")
        self._ax[3].set_xlabel("Current [A]")
        self._ax[4].set_xlabel("Current [A]")
        # adjust the figure
        self._fig.subplots_adjust(top=0.95, hspace=0.48, wspace=0.48, right=0.96)

    ## ploting
    def draw(self, t, data):
        data[2] /= shunt_resistor
        QtGui.qApp.processEvents()
        for i in range(len(self._ax)):
            self._ax[i].clear()
        for i in range(len(data)):
            self._display[i].display(data[i])
        self._time = np.append(self._time, t)
        self._data["m1"] = np.append(self._data["m1"], data[0])
        self._data["m2"] = np.append(self._data["m2"], data[1])
        self._data["m3"] = np.append(self._data["m3"], data[2])
        # plot
        self._ax[0].plot(self._time, self._data["m1"], "k")
        self._ax[1].plot(self._time, self._data["m2"], "k")
        self._ax[2].plot(self._time, self._data["m3"], "k")
        self._ax[3].plot(self._data["m3"], self._data["m1"], "r", linewidth=0., marker="v", markeredgewidth=0.)
        self._ax[4].plot(self._data["m3"], self._data["m2"], "b", linewidth=0., marker="^", markeredgewidth=0.)
        for i in range(len(self._ax)):
            self._ax[i].set_ylabel("Voltage [V]")
        self._ax[3].set_xlabel("Current [A]")
        self._ax[4].set_xlabel("Current [A]")
        self.plot.draw()



## class to handle the controller of current supply
#
class PyMeasureController(QtGui.QMainWindow, PyPowerControl.Ui_Control):

    ## constructor
    def __init__(self, parent=None):
        super(PyMeasureController, self).__init__(parent)
        self.setupUi(self)
        self.Setup()

    ## setup
    def Setup(self):
        self._turnON.clicked.connect(self.Run)
        self._turnOFF.clicked.connect(self.Stop)
        self._update.clicked.connect(self.Update)
        self.control = PyControlThread()
        self.control.data_signal.connect(self.Display)
        self.control.finished.connect(self.Finish)

    ## run controller
    @QtCore.pyqtSlot()
    def Run(self):
        self.init()
        self.control.Run()
        #self._turnON.setEnabled(False)
        #self._turnOFF.setEnabled(True)

    ## stop the current supply
    @QtCore.pyqtSlot()
    def Stop(self):
        self.control.TurnOff()
        self.control.wait()
        #self._turnON.setEnabled(True)
        #self._turnOFF.setEnabled(False)

    ## update the parameter
    @QtCore.pyqtSlot()
    def Update(self):
        speed = self._speed.value()
        protI = self._limI.value()
        protV = self._limV.value()
        self.control.Update(speed, protI, protV)
        self.control.wait()

    ## display current and voltage value
    @QtCore.pyqtSlot(float, float)
    def Display(self, V, I):
        QtGui.qApp.processEvents()
        self._currLabel.setText( "I: %.2f [A]" %I)
        self._voltLabel.setText( "V: %.2e [V]" %V)

    ## finished measurement
    @QtCore.pyqtSlot()
    def Finish(self):
        self.control.wait()
        #self._turnON.setEnabled(True)
        #self._turnOFF.setEnabled(False)

    ## initialize
    def init(self):
        gpib  = "GPIB1::%i::INSTR" %self._port.value()
        speed = self._speed.value()
        protI = self._limI.value()
        protV = self._limV.value()
        self.control.Initialize(gpib, speed, protI, protV)

