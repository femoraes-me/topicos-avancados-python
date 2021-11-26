#<!---------------------------------------------------------------------------->
#<!--                  IFSP - Instituto Federal de São Paulo                 -->
#<!--                       Tópicos Avançados (TPA A6)                       -->
#<!-- File       : Ex302_1D_filter.py                                        -->
#<!-- Description: Script to apply a mean filter in an 1D signal             -->
#<!-- Author     : Fabricio Batista Narcizo (narcizo[at]itu[dot]dk)          -->
#<!-- Information: No additional information                                 -->
#<!-- Date       : 16/11/2021                                                -->
#<!-- Change     : 16/11/2021 - Creation of this script                      -->
#<!-- Review     : 16/11/2021 - Finalized                                    -->
#<!---------------------------------------------------------------------------->

__version__ = "$Revision: 2021111601 $"

################################################################################
import cv2
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
from functools import partial
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.widgets import Slider

################################################################################

def updateSignal(slider, val):
    """
    This function will be performed when the user changes the kernel slider.
    """
    # Global variables.
    global kernel

    # Create a mask for the slider to set only number divisible by 3.
    slider.val = int(round(val))
    slider.poly.xy[2] = slider.val, 1
    slider.poly.xy[3] = slider.val, 0
    slider.valtext.set_text(slider.valfmt % (2 * slider.val + 1))

    # Update the global variable.
    global kernel
    kernel = 2 * slider.val + 1

    # Draw the filtered signal.
    drawFilteredSignal()

def drawFilteredSignal():
    """
    This function apply the mean filter and show the filtered signal.
    """
    # Clear the plot before showing the new signal.
    global lines
    if (len(filtered_ax.lines)):
        filtered_ax.lines.pop()
        lines.remove()

    # Range from 0 to n (x-axis).
    X = range(signal.shape[0])    

    # Filter the signal.
    filtered = filterSignal(signal)

    # Show the filtered signal.
    lines = filtered_ax.vlines(X, [0], filtered)
    filtered_ax.plot(X, filtered, "ko")

def filterSignal(signal):

    # Get the original signal.
    filtered = signal.copy()

    # TODO: Your code here
    
    return filtered

# Generate the discrete one-dimensional signal.
# TODO: Change this code
n = 50
signal = np.ones(n)

# TODO: Your code here

# Range from 0 to n (x-axis).
X = range(signal.shape[0])

# Global kernel variable.
kernel = 3

# Vector to manager the vertical lines.
lines = []

# Get the maximum value generate in the 1D signal.
max_noise = signal.max()

# Create one Matplot windows to visualize an 1D function.
fig = plt.figure("1D Filtering")

original_ax = fig.add_subplot(211)
original_ax.set_title("Original Signal")
original_ax.set_xlim([-1, n])
original_ax.set_ylim([0, max_noise + 10])

filtered_ax = fig.add_subplot(212)
filtered_ax.set_title("Filtered Signal")
filtered_ax.set_xlim([-1, n])
filtered_ax.set_ylim([0, max_noise + 10])

# Define the kernel slider.
axcolor = "lightgoldenrodyellow"
slider_ax = plt.axes([0.1225, 0.02, 0.78, 0.03], facecolor=axcolor)
slider_kernel = Slider(slider_ax, "Kernel", 1.0, 10.0, valinit=1, valfmt="%i")
slider_kernel.on_changed(partial(updateSignal, slider_kernel))
slider_kernel.valtext.set_text("3")

# Show the original distribuition.
original_ax.vlines(X, [0], signal)
original_ax.plot(X, signal, "ko")

# Draw the filtered signal.
drawFilteredSignal()

# Show the matplotlib window.
plt.show()
