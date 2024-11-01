"""
Python package with mildly usefull methods, classes and constants.
"""

from .autotable import Table
from . import petint
from . import scope
from . import randbytes

__project__      = 'PetintLib'
__version__ = '1.4.5.2'
__keywords__     = ['Petint', 'Petras', 'Lib', 'Balint', 'Oscilloscope']
__author__       = 'Petras Balint'
__author_email__ = 'petras.balint04@gmail.com'
__url__          = 'https://github.com/Petint'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Topic :: Libraries",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

__entry_points__ = {}

__requires__ = []
__extra_requires__ = {'mcpi':'1.2.1'}
def asd():
    pass