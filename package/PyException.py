## @package PyException
#  module to handle the error for measurement
#

import logging as log
from time import gmtime, strftime

## base class to handle the error
#
class PyException(Exception):

    ## return the string of current time
    def GetTimeNow(self):
        ctime = strftime("%d %b %Y %H:%M:%S", gmtime())
        return ctime

## error level: ERROR
#
class ERROR(PyException): 
    pass

## error level: WARN
#
class WARN(PyException):
    pass

## error level: DEBUG
class DEBUG(PyException):
    pass

## error level: INFO
#
class INFO(PyException):
    pass

## error level: OVER
class OVER(PyException):
    pass
