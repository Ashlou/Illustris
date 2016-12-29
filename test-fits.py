#Test
import illustris_python as il
from astropy.io import fits
import numpy as np
import sys
import numpy.lib.recfunctions as rfn

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

def test():
    a = np.array([123., 234., 345.])
    b = np.array([1, 0, 1])
    data = np.array(zip(a,b), dtype=np.dtype([('real','f4'), ('int','i4')]))
    write2fits('test.fits', data)
  

try:
    basepath = sys.argv[1]
    snapshot = int(sys.argvp[2])
    assert (snapshot >= 0 and snapshot <= 135), 'Snapshot between 0-135'
except:
    basepath = './Illustris-3/'
    snapshot = int('135')

subhalos = il.groupcat.loadSubhalos(basepath, snapshot)
allfields = subhalos.key()

#append_fields(objgal, ['TYCHOVETO'], data=[tychomask], dtypes=tychomask.dtype, usemask=False)
