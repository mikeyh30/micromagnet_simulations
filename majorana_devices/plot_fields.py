import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, patches
import argparse

plt.rcParams["figure.figsize"] = (20, 10)

parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()

# Magnetostatic field (mT)
# f = np.load("b_field/" + args.a + ".out/strayfield.npy") * 1000
f = np.load("b_field/" + args.a + ".npy") * 1000

dim, zr, yr, xr = f.shape

X, Y, Z = np.meshgrid(np.arange(0, xr, 1), np.arange(0, yr, 1), np.arange(zr))
u, v, w = f[0, :, :, :], f[1, :, :, :], f[2, :, :, :]
u, v, w = u.transpose(1, 2, 0), v.transpose(1, 2, 0), w.transpose(1, 2, 0)

CNT_height = 3
mag_B = np.hypot(u, v, w)

cx = 10 #nm
cy = 10 #nm
cz = 10#nm

U, V, W = np.gradient(mag_B, cx, cy, cz)

slice1 = 20

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(2,2)
axes1 = fig.add_subplot(gs[:, 0])
axes2 = fig.add_subplot(gs[:, 1])

x = np.linspace(0,256*cx,256)
y = np.linspace(0,384*cy,384)

im1 = axes1.pcolormesh(y,x,mag_B[:, :, CNT_height])
axes1.axvline(x=slice1*5, color="r", label="axvline - full height")
cbar = fig.colorbar(im1, ax=axes1)
im1.set_clim(0, 50);
axes1.set_title("Magnetostatic field (mT)")
axes1.set_aspect('equal')
partial = range(150,256)
axes1.streamplot(y,x[partial],u[partial, :, CNT_height],v[partial, :, CNT_height])



dV = np.gradient(v[:, :, CNT_height],5,axis=0)
im2 = axes2.pcolor(y,x,dV)
axes2.axvline(x=slice1*5, color="r", label="axvline - full height")
cbar = fig.colorbar(im2, ax=axes2)
axes2.set_title("Magnetostatic field gradient (mT/nm)")
axes2.set_aspect('equal')

# electrode_position = 800 # distance from centre.
# rect1 = patches.Rectangle((0,(384*5)/2 - electrode_position-100),256*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
# rect2 = patches.Rectangle((0,(384*5)/2 + electrode_position),256*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
# rect3 = patches.Rectangle((0,(384*5)/2 - electrode_position-100),256*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
# rect4 = patches.Rectangle((0,(384*5)/2 + electrode_position),256*5,100,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
# rect5 = patches.Rectangle((0,(384*5)/2 - 250),256*5,500,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)
# rect6 = patches.Rectangle((0,(384*5)/2 - 250),256*5,500,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2)

rect1 = patches.Rectangle((65*cx,150*cx),15*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect2 = patches.Rectangle((102.5*cx,150*cx),20*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect3 = patches.Rectangle((145*cx,150*cx),15*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect4 = patches.Rectangle((182.5*cx,150*cx),20*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect5 = patches.Rectangle((225*cx,150*cx),15*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect6 = patches.Rectangle((262.5*cx,150*cx),20*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)
rect7 = patches.Rectangle((305*cx,150*cx),15*cx,(128-100)*cx, linewidth=1, edgecolor='r',facecolor='r', fill=True, alpha=0.2)


axes1.add_patch(rect1)
axes1.add_patch(rect2)
axes1.add_patch(rect3)
axes1.add_patch(rect4)
axes1.add_patch(rect5)
axes1.add_patch(rect6)
axes1.add_patch(rect7)
# axes1.add_patch(rect1)
# axes1.add_patch(rect2)
# axes1.add_patch(rect5)
# axes2.add_patch(rect3)
# axes2.add_patch(rect4)
# axes2.add_patch(rect6)

# (l,) = axes3.plot(y,u[:, slice1, CNT_height], label="x")
# (l,) = axes3.plot(y,v[:, slice1, CNT_height], label="y")
# (l,) = axes3.plot(y,w[:, slice1, CNT_height], label="z")
# axes3.legend()
# axes3.set_title("Magnetostatic field (mT)")


# region_size = np.max(np.maximum(np.maximum(u[:, slice1, CNT_height],v[:, slice1, CNT_height]),w[:, slice1, CNT_height]))
# axes3.add_patch(patches.Rectangle(((384*5)/2 - electrode_position-100,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
# axes3.add_patch(patches.Rectangle(((384*5)/2 + electrode_position,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
# axes3.add_patch(patches.Rectangle(((384*5)/2 - 250,-region_size),500,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))

# # want du/dy etc
# du = np.gradient(u[:, slice1, CNT_height],y)
# dv = np.gradient(v[:, slice1, CNT_height],y)
# dw = np.gradient(w[:, slice1, CNT_height],y)

# (l,) = axes4.plot(y,du, label="x")
# (l,) = axes4.plot(y,dv, label="y")
# (l,) = axes4.plot(y,dw, label="z")
# axes4.legend()
# axes4.set_title("Magnetostatic field gradient (mT/nm)")

# region_size = np.max(np.maximum(np.maximum(U[:, slice1, CNT_height],V[:, slice1, CNT_height]),W[:, slice1, CNT_height]))

# axes4.add_patch(patches.Rectangle(((384*5)/2 - electrode_position-100,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
# axes4.add_patch(patches.Rectangle(((384*5)/2 + electrode_position,-region_size),100,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))
# axes4.add_patch(patches.Rectangle(((384*5)/2 - 250,-region_size),500,2*region_size,linewidth=1,edgecolor='r',facecolor='r', fill=True, alpha=0.2))


plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# ax.quiver(  X[::32,::5,::4],
#             Y[::32,::5,::4],
#             Z[::32,::5,::4],
#             u[::32,::5,::4],
#             v[::32,::5,::4],
#             w[::32,::5,::4],
#             normalize=True)
# plt.show()