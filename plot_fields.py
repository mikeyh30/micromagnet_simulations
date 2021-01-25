import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
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

U, V, W = np.gradient(mag_B, 5, 5, 10)

slice1 = 20

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(4, 4)
axes1 = fig.add_subplot(gs[:, 0])
axes2 = fig.add_subplot(gs[:, 1])
axes3 = fig.add_subplot(gs[:1, 2:])
axes4 = fig.add_subplot(gs[2:, 2:])

im1 = axes1.pcolor(np.abs(mag_B)[:, :, CNT_height])
axes1.axvline(x=slice1, color="b", label="axvline - full height")
cbar = fig.colorbar(im1, ax=axes1)
axes1.set_title("Magnetostatic field (mT)")

im2 = axes2.pcolor(np.abs(V)[:, :, CNT_height])
axes2.axvline(x=slice1, color="b", label="axvline - full height")
cbar = fig.colorbar(im2, ax=axes2)
axes2.set_title("Magnetostatic field gradient (mT/nm)")

(l,) = axes3.plot(u[:, slice1, CNT_height], label="x")
(l,) = axes3.plot(v[:, slice1, CNT_height], label="y")
(l,) = axes3.plot(w[:, slice1, CNT_height], label="z")
axes3.legend()
axes3.set_title("Magnetostatic field (mT)")

(l,) = axes4.plot(U[:, slice1, CNT_height], label="x")
(l,) = axes4.plot(V[:, slice1, CNT_height], label="y")
(l,) = axes4.plot(W[:, slice1, CNT_height], label="z")
axes4.legend()
axes4.set_title("Magnetostatic field gradient (mT/nm)")

plt.show()
