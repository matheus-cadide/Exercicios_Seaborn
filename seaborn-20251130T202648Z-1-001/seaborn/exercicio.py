import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter
from openpyxl.styles.fills import fills

df = pd.read_csv('Titanic-Dataset.csv')
print(df.info())
sns.set_style('whitegrid')
'''
primeiro exercicio


sns.jointplot(x = 'Fare', y = 'Age',data = df)
plt.show()
'''
'''
#segundo exercício
sns.histplot(x = 'Fare', bins = 30, data = df, color = 'red')
sns.despine(top = True, left=True, right=True)

plt.show()
'''
#terceiro exercício
sns.boxplot(data= df, x = 'Pclass', y = 'Age',  palette= 'pastel',flierprops={"marker": "d", 'markerfacecolor': 'black'} )
plt.show()