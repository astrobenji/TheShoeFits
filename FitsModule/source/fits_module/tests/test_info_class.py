#!/usr/bin/env python

import numpy as np
from astropy.io import fits

from fits_module_class import Info

def test_fits_module():
	filename='../../Datafiles/spectra/spec-4055-55359-0001.fits'
	file_1 = Info(filename)	
	np.testing.assert_approx_equal(file_1.ra, 236.433204)
	
def test_1():
	filename = '.	./../Datafiles/spectra/spec-4055-55359-0001.fits'
	hdu_list = fits.open(filename)
	assert len(hdu_list) == 4
	