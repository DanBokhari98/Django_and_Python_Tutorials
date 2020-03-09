ipython notebook --matplotlib inline
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('people-example.csv')

plt.figure()
df.plot(kind='line')
plt.show()
