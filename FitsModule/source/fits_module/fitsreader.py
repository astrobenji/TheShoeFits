#!/usr/bin/env python

# FITS reader:

from astropy.io import fits
from classHDU import HDU_list
from classHDU import HDU_struct


def build_HDU_list(filename):
	''' Takes a FITS file and packages it into a struct '''
	hdu_list = fits.open(filename)
	new_HDU_list = HDU_list()
	new_HDU_list.n_files = len(hdu_list)
	for curr_HDU in hdu_list:
		new_HDU_object = HDU_struct()
		new_HDU_object.name = curr_HDU.name
		new_HDU_object.dimension[0]