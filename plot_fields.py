import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, patches
import argparse

plt.rcParams["figure.figsize"] = (20, 10)

parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()

# Magnetostatic field (mT)
f = np.load("B_field/" + args.a + ".out/strayfield.npy") * 1000

dim, zr, yr, xr = f.shape

X, Y, Z = np.meshgrid(np.arange(0, xr, 1), np.arange(0, yr, 1), np.arange(zr))
u, v, w = f[0, :, :, :], f[1, :, :, :], f[2, :, :, :]
u, v, w = u.transpose(1, 2, 0), v.transpose(1, 2, 0), w.transpose(1, 2, 0)

CNT_height = 15
mag_B = np.hypot(u, v, w)

cx = 5 #nm
cy = 5 #nm
cz = 10#nm

U, V, W = np.gradient(mag_B, cx, cy, cz)

slice1 = 20

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(4, 4)
axes1 = fig.add_subplot(gs[:, 0])
axes2 = fig.add_subplot(gs[:, 1])
axes3 = fig.add_subplot(gs[:1, 2:])
axes4 = fig.add_subplot(gs[2:, 2:])

x = np.linspace(0,80*5,80)
y = np.linspace(0,384*5,384)

im1 = axes1.pcolor(x,y,mag_B[:, :, CNT_height])
axes1.axvline(x=slice1*5, color="r", label="axvline - full height")
cbar = fig.colorbar(im1, ax=axes1)
axes1.set_title("Magnetostatic field (mT)")
axes1.set_aspect('equal')
axes1.streamplot(x,y,u[:, :, CNT_height],v[:, :, CNT_height])

im2 = axes2.pcolor(x,y,V[:, :, CNT_height])
axes2.axvline(x=slice1*5, color="r", label="axvline - full height")
cbar = fig.colorbar(im2, ax=axes2)
axes2.set_title("Magnetostatic field gradient (mT/nm)")
axes2.set_aspect('equal')

electrode_position = 800 # distance from centre.
rect1 = patches.Rectangle((0,(384*5)/2 - electrode_position-100),80*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect2 = patches.Rectangle((0,(384*5)/2 + electrode_position),80*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect3 = patches.Rectangle((0,(384*5)/2 - electrode_position-100),80*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect4 = patches.Rectangle((0,(384*5)/2 + electrode_position),80*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect5 = patches.Rectangle((0,(384*5)/2 - 250),80*5,500,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect6 = patches.Rectangle((0,(384*5)/2 - 250),80*5,500,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)

axes1.add_patch(rect1)
axes1.add_patch(rect2)
axes1.add_patch(rect5)
axes2.add_patch(rect3)
axes2.add_patch(rect4)
axes2.add_patch(rect6)

(l,) = axes3.plot(y,u[:, slice1, CNT_height], label="x")
(l,) = axes3.plot(y,v[:, slice1, CNT_height], label="y")
(l,) = axes3.plot(y,w[:, slice1, CNT_height], label="z")
axes3.legend()
axes3.set_title("Magnetostatic field (mT)")

region_size = np.max(np.maximum(u[:, slice1, CNT_height],v[:, slice1, CNT_height],w[:, slice1, CNT_height]))

axes3.add_patch(patches.Rectangle(((384*5)/2 - electrode_position-100,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
axes3.add_patch(patches.Rectangle(((384*5)/2 + electrode_position,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
axes3.add_patch(patches.Rectangle(((384*5)/2 - 250,-region_size),500,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))


(l,) = axes4.plot(y,U[:, slice1, CNT_height], label="x")
(l,) = axes4.plot(y,V[:, slice1, CNT_height], label="y")
(l,) = axes4.plot(y,W[:, slice1, CNT_height], label="z")
axes4.legend()
axes4.set_title("Magnetostatic field gradient (mT/nm)")

region_size = np.max(np.maximum(U[:, slice1, CNT_height],V[:, slice1, CNT_height],W[:, slice1, CNT_height]))

axes4.add_patch(patches.Rectangle(((384*5)/2 - electrode_position-100,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
axes4.add_patch(patches.Rectangle(((384*5)/2 + electrode_position,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
axes4.add_patch(patches.Rectangle(((384*5)/2 - 250,-region_size),500,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))


plt.show()
