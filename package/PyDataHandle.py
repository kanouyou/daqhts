## @package PyDataHandle
#  module to handle the data
#

#import h5py  as hdf
import ROOT
import numpy as np
import time
import PyException

## class for data saving
#
class PyDataHandle:

    ## constructor
    def __init__(self, filename="measure.root"):
        if filename[-4:]=="root":
            self._file = ROOT.TFile(filename, "recreate")
        else:
            self._file = ROOT.TFile(filename+".root", "recreate")
        self._start = time.time()
        self._tree = ROOT.TTree("tree", "measurement result")
        # create float arrays (global time, local time, data)
        self._global = np.zeros(1, dtype=float)
        self._local  = np.zeros(1, dtype=float)
        self._data   = np.zeros(3, dtype=float)
        # setup branch
        self._tree.Branch("globaltime", self._global, "globaltime/D")
        self._tree.Branch( "localtime",  self._local,  "localtime/D")
        self._tree.Branch(   "measure",   self._data, "measure[3]/D")

    ## setup the start time
    def SetStartTime(self, time):
        self._start = time

    ## setup time
    def SetTime(self, time):
        self._global[0] = time
        self._local [0] = time - self._start

    ## setup data
    def SetData(self, data):
        if len(data)!=3:
            raise ERROR("data size is wrong.")
        self._data[0] = data[0]
        self._data[1] = data[1]
        self._data[2] = data[2]

    ## fill data into tree
    def Fill(self):
        self._tree.Fill()

    ## fill all data at once
    def FillAll(self, time, data):
        self.SetTime(time)
        self.SetData(data)
        self.Fill()

    ## close and save the file
    def Close(self):
        self._file.Write()
        self._file.Close()
