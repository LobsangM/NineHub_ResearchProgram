#File : pyregion_ds9.py
#user: Lobsang Méndez

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import pyregion

# Cargar el archivo .reg
reg_file = "regiones_ds9.reg"
regiones = pyregion.open(reg_file)

# Cargar los datos de la imagen
fits_file = "NGC5258_s_concat_uvt_dot75asec_rbeam1asec_csdot1.pbcor_hcorr.fits"
hdul = fits.open(fits_file)
image_data = hdul[0].data
header = hdul[0].header

# Generar la máscara para todas las regiones
mask_total = regiones.get_mask(header=header, shape=image_data.shape)

# Visualizar la máscara total
plt.imshow(image_data, origin='lower', cmap='gray')
plt.imshow(mask_total, origin='lower', cmap='YlGnBu_r', alpha=0.5)  # Superponer la máscara total
plt.title("Máscara total sobre la imagen")
plt.colorbar()
plt.show()

# Separar máscaras individuales (si necesario)
# mascaras_individuales = []
# for region in regiones:
#     single_region = pyregion.ShapeList([region])
#     mask = single_region.get_mask(header=header, shape=image_data.shape)
#     mascaras_individuales.append(mask)


# Cerrar el archivo FITS
hdul.close()
