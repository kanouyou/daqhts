## @package PyGraphHandle
#  module to handle the graph ploting
#

import matplotlib.pyplot as plt
import numpy as np

## class to handle the graph ploting
#
class PyGraphHandle:

    # constructor
    def __init__(self, opt="graph"):
        self.fOpt = opt

    # choose the graph or hist
    def GetPlot(self, axis):
        if self.fOpt=="graph" or self.fOpt=="g":
            graph = PyGraph(axis)
            return graph
        elif self.fOpt=="hist" or self.fOpt=="h":
            hist = PyHist(axis)
            return hist


class PyGraph(PyGraphHandle):

    # constructor
    def __init__(self, axis):
        self.fAx = axis
        self.fX  = np.array([])
        self.fY  = np.array([], dtype="float64")

    # set point
    def SetPoint(self, x, y):
        self.fX = np.append(self.fX, x)
        self.fY = np.append(self.fY, y)

    # set data
    def SetData(self, x, y):
        self.fX = x
        self.fY = y

    # get graph
    def Plot(self, label="", marker="o"):
        self.fAx.plot(self.fX, self.fY, marker=marker, label=label)


class PyHist(PyGraphHandle):

    # constructor
    def __init__(self, axis):
        self.fAx = axis
        self.fData = np.array([], dtype="float64")

    # fill
    def Fill(self, data):
        self.fData = np.append(self.fData, data)

    # set data
    def SetData(self, data):
        self.fData = data

    # plot
    def Plot(self, label="", bin=20, alpha=0.6):
        self.fAx.hist(self.fData, bin=bin, alpha=alpha)

