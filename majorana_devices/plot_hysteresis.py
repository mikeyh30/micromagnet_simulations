import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sim")
args = parser.parse_args()

df = pd.read_csv('./hysteresis/' + args.sim + '.out/table.txt',delimiter='\t')

plt.plot(df['B_extx (T)'],df['mx ()'])

plt.show()
