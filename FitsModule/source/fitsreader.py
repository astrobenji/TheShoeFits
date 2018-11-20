#!/usr/bin/env python

# FITS reader:

from astropy.io import fits
from .classHDU import HDU_list
from .classHDU import HDU_struct


def build_HDU_list(filename):
	''' Takes a FITS file and packages it into a struct '''
	hdu_list = fits.open(filename)
	new_HDU_list = HDU_list()