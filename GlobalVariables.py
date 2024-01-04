import os
import sys

picdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pic')
photodir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pic/photos')
libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
