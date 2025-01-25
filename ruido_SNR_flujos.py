import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from regions import Regions
import pyregion

# Paso 1: Cargar el archivo de regiones
reg_file = "regiones_ds9.reg" 
regiones = pyregion.open(reg_file)


# Paso 2: Cargar la imagen 2D
fits_file = "NGC5258_s_concat_uvt_dot75asec_rbeam1asec_csdot1.pbcor_hcorr.fits" 
hdul = fits.open(fits_file)
image_data = hdul[0].data
header = hdul[0].header



# Listas para datos de flujo y ruido
flujos_totales = []
datos_extraidos = []


# Asumimos que la última región en el archivo contiene solo ruido
indice_region_ruido = 1  # Cambia si la región de ruido es otra
datos_ruido = []

# Paso 3: Iterar sobre cada región y calcular flujo
for i, region in enumerate(regiones):
    mask = region.to_mask(mode='center')
    masked_data = mask.multiply(image_data)
    datos_dentro_region = masked_data[mask.data > 0]
    flujo_total = np.sum(datos_dentro_region)
    flujos_totales.append(flujo_total)
    datos_extraidos.append(datos_dentro_region)
    if i == indice_region_ruido:
        datos_ruido.extend(datos_dentro_region)

