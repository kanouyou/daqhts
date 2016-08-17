#!/usr/bin/env python2.7

import multiprocessing
import sys
sys.path.append("./package")

import PyLogHandle

from PyQt4 import QtGui, QtCore
import PyMeasureHandle


def usage():
    print "usage:"
    print " python main.py [option]\n"
    print "option:"
    print "   -h or --help        usage of hts daq"
    print "   -m or --monitor     run the data monitor"
    print "   -c ot --control     run the power supply controller"


def monitor():
    app  = QtGui.QApplication(sys.argv)
    form = PyMeasureHandle.PyMonitorHandle()
    form.show()
    app.exec_()


def controller():
    app  = QtGui.QApplication(sys.argv)
    form = PyMeasureHandle.PyMeasureController()
    form.show()
    app.exec_()


def multirun():
    p = []
    p.append( multiprocessing.Process(target=monitor) )
    p.append( multiprocessing.Process(target=controller) )
    for i in range(len(p)):
        p[i].start()
        p[i].join()


if __name__=="__main__":
    #logger = PyLogHandle.PyLogHandle()
    #logger.SetLevel()
    opt = sys.argv

    if len(opt)>1:
        if opt[1]=="-m" or opt[1]=="--monitor":
            monitor()
        elif opt[1]=="-c" or opt[1]=="--control":
            controller()
        elif opt[1]=="-h" or opt[1]=="--help":
            usage()
    else:
        while True:
            msg = raw_input(">> ")
            if msg=="run":
                multirun()
                msg = raw_input(">> ")
            elif msg=="kill":
                for p in multiprocessing.active_children():
                    p.terminate()
                msg = raw_input(">> ")
            elif msg==".q" or msg=="quit":
                break
            else:
                msg = raw_input(">> ")
        print ">> finished "
