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


try:
    basepath = sys.argv[1]
    snapshot = int(sys.argv[2])
    assert (snapshot >= 0 and snapshot <= 135), 'Snapshot between 0-135'
except:
    basepath = '/home/ahmad/Illustris-3'
    snapshot = int('135')

subhalos = il.groupcat.loadSubhalos(basepath, snapshot)
allfields = subhalos.keys()

''' AVAILABLE COLUMNS
SubhaloPos
SubhaloBHMdot
SubhaloVmax
SubhaloWindMass
SubhaloGasMetallicityMaxRad
SubhaloVelDisp
SubhaloSFR
SubhaloStarMetallicityMaxRad
SubhaloLen
SubhaloSFRinHalfRad
SubhaloStellarPhotometrics
SubhaloGasMetallicity
SubhaloBHMass
SubhaloIDMostbound
SubhaloMassType
SubhaloStellarPhotometricsMassInRad
SubhaloHalfmassRad
SubhaloParent
SubhaloSpin
SubhaloStarMetallicityHalfRad
SubhaloVel
SubhaloLenType
SubhaloGasMetallicitySfrWeighted
SubhaloGasMetallicityHalfRad
SubhaloMassInRad
SubhaloGrNr
SubhaloMassInHalfRad
SubhaloSFRinRad
SubhaloMassInMaxRad
SubhaloHalfmassRadType
SubhaloMassInMaxRadType
SubhaloCM
SubhaloStarMetallicity
count
SubhaloMassInHalfRadType
SubhaloMass
SubhaloMassInRadType
SubhaloVmaxRad
SubhaloSFRinMaxRad
SubhaloStellarPhotometricsRad
SubhaloGasMetallicitySfr

'''
# For desired columns, edit `ts`
ts = [
      'SubhaloPos',
      'SubhaloSFR',
      'SubhaloMass'
      ]

for tsi in ts:
   ar = subhalos[tsi]
   np.savetxt(tsi+'-data.txt', ar, header=''+tsi)
print 'done!'
