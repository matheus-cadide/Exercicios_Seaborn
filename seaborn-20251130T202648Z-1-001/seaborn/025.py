import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Titanic-Dataset.csv')
print(df.info())


sns.histplot(x = df['Fare'],bins= 30, data = df, color= 'red')
sns.despine(left= True, top = True)
sns.color_palette('colorblind')
plt.show()
