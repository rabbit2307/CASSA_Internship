from reproject import reproject_exact
from astropy.io import fits
import numpy as np

# Load flux and exposure maps
flux1 = fits.getdata('16142/repro/work/img/16142b4_0.5-2_flux.img')
exp1  = fits.getdata('16142/repro/work/img/16142b4_0.5-2_thresh.expmap')

flux2 = fits.getdata('16143/repro/work/img/16143b4_0.5-2_flux.img')
exp2  = fits.getdata('16143/repro/work/img/16143b4_0.5-2_thresh.expmap')

# If needed, reproject flux2 and exp2 to flux1 WCS using reproject_exact
from reproject import reproject_exact
header1 = fits.getheader('16142/repro/work/img/16142b4_0.5-2_flux.img')
flux2_reproj, footprint = reproject_exact((flux2, fits.getheader('16143/repro/work/img/16143b4_0.5-2_flux.img')), header1)
exp2_reproj, _ = reproject_exact((exp2, fits.getheader('16143/repro/work/img/16143b4_0.5-2_thresh.expmap')), header1)

# Weighted stacking
stacked_num = flux1*exp1 + flux2_reproj*exp2_reproj
stacked_exp = exp1 + exp2_reproj

stacked_flux = stacked_num / stacked_exp

# Save final image
hdu = fits.PrimaryHDU(stacked_flux, header=header1)
hdu.writeto('stacked_flux.fits', overwrite=True)
