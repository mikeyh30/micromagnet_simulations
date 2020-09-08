import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

f = np.load("strayfield.npy")

dim, zr, yr, xr = f.shape                                                                  

X,Y,Z = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1),np.arange(4))  
u,v,w = f[0,:,:,:],f[1,:,:,:],f[2,:,:,:]                                 
u,v,w = u.transpose(1,2,0), v.transpose(1,2,0), w.transpose(1,2,0)

fig, axes = plt.subplots(1,2)

# axes[0,0] = fig.gca(projection='3d') 
# axes[0,0].set_xlabel("x") 
# axes[0,0].set_ylabel("y") 
# axes[0,0].set_zlabel("z") 
# axes[0,0].quiver(X, Y, Z, u, v, w, length=0.1)
f2 = np.load("v1.npy")

X2, Y2 = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1))
# fig, ax = plt.subplots(figsize=(7, 2))
# Choose a z slice
axes[0].imshow(f2[0,0,:,:])
a=3
axes[0].quiver(X2[::a,::a], Y2[::a,::a], v[::a, ::a, 0], u[::a, ::a, 0],scale=1.2)
axes[0].set_aspect('equal')

im2 = axes[1].imshow(np.hypot(u[:,:,0],v[:,:,0]),norm=LogNorm(vmin=0.01, vmax=1))
axes[1].streamplot(X2[::a,::a], Y2[::a,::a], v[::a, ::a, 0], u[::a, ::a, 0],
                linewidth=1, cmap=plt.cm.inferno,
                density=2, arrowstyle='->', arrowsize=1.5)
fig.colorbar(im2, ax=axes[1])

plt.show()