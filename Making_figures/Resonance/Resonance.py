# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')

import warnings     # added to ignore the plotting warings about font types in math mode
warnings.simplefilter("ignore", UserWarning)

import matplotlib as mpl
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import os as os
import numpy as np
import scipy as sp
import copy as copy
from matplotlib import cm
import time
#import pykrige as pykrige
import scipy.io as sio
tt1 = time.time()

# set default fonts and plot colors
plt.rcParams.update({'image.cmap': 'viridis'})
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.fontset': 'custom'})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.it': 'serif:italic'})
plt.rcParams.update({'mathtext.bf': 'serif:bold'})
plt.close('all')



#%% plot the resonant response

tt = np.linspace(0,10,1000)

x_0=1/1000   # mm
v_0=0/1000   # mm/s 
k= 50         # N/m
m = 1         # kg
c = 0.9       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
omega=omega_n
f_0=1
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

xx = (v_0/omega)* np.sin(omega*tt) + x_0 * np.cos(omega*tt) + f_0/(2*omega)*tt*np.sin(omega*tt)

xx_outline = f_0/(2*omega)*tt

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.plot(tt,xx_outline*1000,'k--',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.plot(tt,-xx_outline*1000,'k--',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
#plt.legend(loc=1,ncol=2,framealpha=1)
plt.savefig('Python.pdf')





























































































