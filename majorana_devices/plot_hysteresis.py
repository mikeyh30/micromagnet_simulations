import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hyst_table")
args = parser.parse_args()

df = pd.read_csv(args.hyst_table,delimiter='\t')

plt.plot(df['B_exty (T)'],df['my ()'])

plt.show()
