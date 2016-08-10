## @package PyDataHandle
#  module to handle the data
#

import h5py  as hdf
import numpy as np

## class for data saving
#
class PyDataHandle:

    ## constructor
    def __init__(self, filename):
        self._filename = filename
