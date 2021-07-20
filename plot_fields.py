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

fig, axes = plt.subplots(1,3)

# axes[0,0] = fig.gca(projection='3d') 
# axes[0,0].set_xlabel("x") 
# axes[0,0].set_ylabel("y") 
# axes[0,0].set_zlabel("z") 
# axes[0,0].quiver(X, Y, Z, u, v, w, length=0.1)
f2 = np.load("B_field/"+args.a+".out/"+args.a+".npy")

X2, Y2 = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1))
# fig, ax = plt.subplots(figsize=(7, 2))
# Choose a z slice
# axes[0].imshow(f2[0,0,:,:])
a=3
# axes[0].quiver(X2[::a,::a], Y2[::a,::a], v[::a, ::a, 0], u[::a, ::a, 0],scale=1.2)
# axes[0].set_aspect('equal')

mag_B = np.hypot(u[:,:,0],v[:,:,0])

grad = np.gradient(mag_B)
print(type(grad))
l, = axes[0].plot(grad[0][0,:])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.12, 0.03, 0.25, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'slice', 0, 255, valinit=128, valstep=1)

axes[0].set_ylim([-0.05,0.05])



def update(val):
    freq = int(sfreq.val)
    l.set_ydata(grad[0][freq,:])
    fig.canvas.draw_idle()


sfreq.on_changed(update)




# im2 = axes[1].imshow(np.hypot(u[:,:,0],v[:,:,0]),norm=LogNorm(vmin=0.01, vmax=1))
# axes[1].streamplot(X2[::a,::a], Y2[::a,::a], v[::a, ::a, 0], u[::a, ::a, 0],
#                 linewidth=1, cmap=plt.cm.inferno,
#                 density=2, arrowstyle='->', arrowsize=1.5)
# fig.colorbar(im2, ax=axes[1])



grad = np.gradient(mag_B)
im3 = axes[1].imshow(grad[0])
fig.colorbar(im3, ax=axes[1])


import matplotlib.image as mpimg
image = mpimg.imread("./B_field/"+args.a+".out/geom000000.jpg")
axes[2].imshow(image)

plt.show()