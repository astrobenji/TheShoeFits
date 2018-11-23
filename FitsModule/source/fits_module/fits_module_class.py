from astropy.io import fits

class Info(object):

    def __init__(self, filename):
        self.telescope = None
        self.ra = None
        self.dec = None
        self.plate_id = None

        with fits.open(filename) as hdu_list:
            dat = hdu_list[0]
            self.telescope = dat.header['TELESCOP']
            self.ra = dat.header['RA']
            self.dec = dat.header['DEC']
            self.plate_id = dat.header['PLATEID']

#filename='../../Datafiles/spectra/spec-4055-55359-0001.fits'
#file_1 = Info(filename)
#print(file_1.ra)


#create two classes
#class HDU list
#classs HDU struct
