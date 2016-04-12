# plot_spectrum.py is an example of matplotlib as applied to text spectra
#
# My example uses 2MASS J0937+2931 - see Burgasser et al. (2006) ApJ, 639, 1095 -
# but you can use this method for basically any object.
#
#############################################################

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


# Input spectrum - you will want to change 'Filename.txt' to whatever file you wish to use.
filename = 'Filename.txt'

# numpy.loadtxt - a useful way to load text files
# loadtxt statements below to read in the relevant data
# Note that usecols needs to read 0, and 1, etc.
# or it interprets the statement as a single element, not a column

wavelength_obj = np.loadtxt(filename, dtype = float, comments = '#', usecols = (0,))
flux_obj = np.loadtxt(filename, dtype = float, comments = '#', usecols = (1,))
noise_obj = np.loadtxt(filename, dtype = float, comments = '#', usecols = (2,))

# Some statements to set up the plot itself
fig = plt.figure()

ax1 = plt.axes()

# Arrays to reflect actual data = use '1' suffix to avoid any confusion
x1 = wavelength_obj
y1 = flux_obj
z1 = noise_obj

# Labels for the plot's titles and axes - you'll want to change the text as appropriate
fig.suptitle('Spectrum of 2MASS J0937+2931 (d/sdT6)', fontsize=20, fontweight='bold')

#r at the start of the text string and $ blah $ around the LaTeX bit
ax1.set_xlabel(r'Wavelength / $\mu$m', fontsize=16)
ax1.set_ylabel(r'Flux, normalised to 1.27$\mu$m', fontsize=16)


# Some definitions for where the plot starts and stops
#since both of these will need to be called at least twice,
# it makes sense to define them.
x_start = 0.67
x_stop = 2.5

y_start = -0.25
y_stop = 1.1

# Annotation-text to describe what is on the plot
ax1.text(1.75, 0.9, 'Object spectrum', color='black')
ax1.text(1.75, 0.75, 'Noise spectrum', color='black')

# Create plot lines for spectrum and noise
line1, = ax1.plot(x1, y1, color='blue')
line2, = ax1.plot(x1, z1, color='red')

# Set axes to remove unneeded white space
ax1.set_xlim(left = x_start, right = x_stop)
ax1.set_ylim(y_start, y_stop)

# Lines to go with the annotations
x_spectrum = np.arange(1.5, 1.725, 0.01)
x_len_spec = len(x_spectrum)
y_spectrum = np.zeros(x_len_spec, dtype=float) + 0.92

x_noise = np.arange(1.5, 1.725, 0.01)
x_len_noise = len(x_noise)
y_noise = np.zeros(x_len_noise, dtype=float) + 0.77

line3, = ax1.plot(x_spectrum, y_spectrum, color='blue')
line4, = ax1.plot(x_noise, y_noise, color='red')

# create a dashed line across at zero

x_0 = np.arange(x_start, x_stop, 0.001)
x_len_0 = len(x_0)
y_0 = np.zeros(x_len_0, dtype=float)

line0, = ax1.plot(x_0, y_0, linestyle='--', color='black')

# And now, to display and save the plot itself...
plt.show()

# You may wish to change Object.png to something else
plt.savefig('Object.png')
