import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hyst_table")
args = parser.parse_args()

df = pd.read_csv(args.hyst_table,delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(df['B_exty (T)'],df['my ()'])

ax.set_title("Magnetization of whole array")
ax.set_xlabel("H (T)")
ax.set_ylabel("m ()")
# ax.annotate('(0,0.017)',(0,0.017),xytext=(-0.1,0.05),arrowprops=dict(arrowstyle="->"))
# ax.annotate('(0,-0.017)',(0,-0.017),xytext=(0.05,-0.05),arrowprops=dict(arrowstyle="->"))

plt.show()
