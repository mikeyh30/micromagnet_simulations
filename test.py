import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()

f = np.load("B_field/"+args.a+".out/strayfield.npy")

dim, zr, yr, xr = f.shape                                                                  

X,Y,Z = np.meshgrid(np.arange(0,128,1),np.arange(0,256,1),np.arange(4))  
u,v,w = f[0,:,:,:],f[1,:,:,:],f[2,:,:,:]                                 
u,v,w = u.transpose(1,2,0), v.transpose(1,2,0), w.transpose(1,2,0)

mag_B = np.hypot(u[:,:,0],v[:,:,0])
slice1 = 128


# axes[0].plot(mag_B[0,:])

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l, = plt.plot(mag_B[0,:])
ax.margins(x=0)

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0, 255, valinit=0, valstep=1)

ax.set_ylim([0,0.01])

def update(val):
    freq = sfreq.val
    l.set_ydata(mag_B[freq,:])
    fig.canvas.draw_idle()


sfreq.on_changed(update)



plt.show()