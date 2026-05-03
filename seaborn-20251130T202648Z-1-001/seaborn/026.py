import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')
print(df.info())
df['class'] = df['Pclass']

sns.boxplot(x= 'class', y = 'Age', data = df, flierprops = {"marker": "x"} )
plt.show()
