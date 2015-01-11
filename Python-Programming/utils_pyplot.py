#!python3
"""
Various utilities for working with Python and Matplotlib
"""

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import os

from math import ceil, sqrt
from skimage.io import imread

def show_images(images,titles=None):
    """Display a list of images"""
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images, titles):
        a = fig.add_subplot(1,n_ims,n) # Make subplot
        if image.ndim == 2: # Is image grayscale?
            plt.gray() # Only place in this blog you can't replace 'gray' with 'grey'
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()

def tile_images(lst, size=None):
    """
    Given a list of images, display them in a tiled format.
    """
    num_plots = len(lst)
    if size is None:
        cols = ceil(sqrt(num_plots))
        rows  = ceil(num_plots/cols)
    else:
        rows, cols = size

    # Set up the figure
    fig, axes = plt.subplots(rows, cols)

    # Plot the images using `plt.imshow`
    for i, x in enumerate(lst):
        ax = axes[i]
        # If the element is a string, assume that it's a path
        if isinstance(x, str):
            try:
                img = imread(os.path.abspath(x))
                ax.imshow(img)
            except IOError:
                print("Unable to load image: %s" %x)
            except Exception as e:
                print(e)
        # Otherwise, attempt to load it as a numpy array
        else:
            try:
                img = np.array(x)
                ax.imshow(img)
            except Exception as e:
                print(e)

    # Show the images
    plt.show()

    # Return the fig and axes images, in case that is wanted
    return fig, axes