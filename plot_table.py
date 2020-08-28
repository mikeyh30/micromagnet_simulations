import pandas as pd
import matplotlib.pyplot as plt

# df1 = pd.read_csv('./test1.out/table.txt',delimiter='\t')
df2 = pd.read_csv('./hysteresis.out/table.txt',delimiter='\t')

# plt.subplot(1,2,1)
# plt.plot(df1['B_extx (T)'],df1['mx ()'])

# plt.subplot(1,2,2)
plt.plot(df2['B_extx (T)'],df2['mx ()'])

plt.show()
