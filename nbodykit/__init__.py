import sys
import os.path

def addpath(relpath):
    """
    Add path relative to root

    Parameters
    ----------
    relpath : string
        path to add

    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, os.path.join(root, relpath))

addpath('extern/sharedmem')
addpath('extern/MP-sort')
addpath('extern/pfft-python')
addpath('extern/kdcount')
addpath('extern/pypm')

