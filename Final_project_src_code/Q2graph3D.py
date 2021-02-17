#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:44:48 2021

@author: Chokeunhee
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from pylab import meshgrid,title

def function(x,y):
    return  20 * np.sin((np.pi/2) * (x - 2 * np.pi)) + 20 * np.sin((np.pi/2) 
                        * (y - 2 * np.pi)) + ((x - 2 * np.pi) ** 2) + ((y - 2 * np.pi) ** 2)

x = np.arange(0,10,0.1)
y = np.arange(0,10,0.1)
X,Y = meshgrid(x, y)
Z = function(X,Y)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.RdBu,linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
title("\u03C8(x,y)")
plt.show()

