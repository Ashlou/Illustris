
from astropy.io import fits
import numpy as np
def write2fits(filename, arry):
    col = []
    for i, nms in enumerate(arry.dtype.names):
       print nms, type(nms)
       col.append(fits.Column(name=nms, format=arry[nms].dtype, array=arry[nms]))
    cols = fits.ColDefs(col)
    tbhdu = fits.new_table(cols)
    prihdr = fits.Header()
    prihdr['comments'] = "Add some comment here"
    prihdu = fits.PrimaryHDU(header=prihdr)
    thdulist = fits.HDUList([prihdu, tbhdu])
    thdulist.writeto(filename)
    print "Done ... written on .. %s"%(filename)


a = np.array([123., 234., 345.])
b = np.array([1, 0, 1])
data = np.array(zip(a,b), dtype=np.dtype([('real','f4'), ('int','i4')]))
write2fits('test.fits', data)
    
