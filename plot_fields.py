import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.widgets import Slider
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()

f = np.load("B_field/"+args.a+".out/strayfield.npy")

dim, zr, yr, xr = f.shape                                                                  

X,Y,Z = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1),np.arange(4))  
u,v,w = f[0,:,:,:],f[1,:,:,:],f[2,:,:,:]                                 
u,v,w = u.transpose(1,2,0), v.transpose(1,2,0), w.transpose(1,2,0)

fig, axes = plt.subplots(1,2)

f2 = np.load("B_field/"+args.a+".out/"+args.a+".npy")

X2, Y2 = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1))

a=3

slice2 = 3
mag_B = np.hypot(u[:,:,slice2],v[:,:,slice2])

grad = np.gradient(mag_B)

slice1 = 39

im3 = axes[1].imshow(grad[0])
axes[1].axvline(x = slice1, color = 'b', label = 'axvline - full height') 
cbar = fig.colorbar(im3, ax=axes[1])
print(type(grad))
l, = axes[0].plot(grad[0][:,slice1])

plt.show()