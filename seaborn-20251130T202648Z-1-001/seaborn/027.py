import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Titanic-Dataset.csv')
print(df.info())

print(df['Sex'].value_counts())
sns.countplot(x = 'Sex', data= df, palette=sns.color_palette())
plt.show()