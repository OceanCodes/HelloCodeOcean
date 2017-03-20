"""
Otsu thresholding
==================

This example illustrates automatic Otsu thresholding.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly
from skimage import data, io, filters, exposure

# input = io.imread('/input/camera.png')
input = data.camera()
val = filters.threshold_otsu(input)

hist, bins_center = exposure.histogram(input)

fig = plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(input, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(input < val, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()

fig.savefig('/output/plot.png')
