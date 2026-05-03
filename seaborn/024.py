import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = pd.read_csv('Titanic-Dataset.csv')

print(titanic.info())

sns.jointplot(x = 'Fare', y = 'Age', data =titanic)
plt.show()

