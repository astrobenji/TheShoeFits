#!/usr/bin/env python

from fitsreader.py import read_fits

def test_1():
	filename = 'Datafiles/spectra/spec-4055-55359-0001.fits'
	hdu_list = fits.open(filename)
	assert len(hdu_list) == 4