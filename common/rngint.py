# -*- coding: utf-8 -*-

"""
Random Number Generator for Integers
with user-specified digits
"""

from math import *
from random import *

def RandomInteger(digit=1):
    assert (digit>=1)
    istart=0
    if(digit>1):
        istart=10**(digit-1)

    iend=10**digit
    ranint=randrange(istart,iend)
    return ranint

def MinNumber(digit=1):
    istart=0
    if(digit>1):
        istart=10**(digit-1)
    return istart

def MaxNumber(digit=1):
    iend=10**digit
    return iend