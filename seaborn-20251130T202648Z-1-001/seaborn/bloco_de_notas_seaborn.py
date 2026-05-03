import seaborn as sns
#Para conseguir mostrar o gráfico no pycharm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#um dos dataset do seaborn
gorjeta = sns.load_dataset('tips')
print(gorjeta.head())
print(gorjeta.info())
'''
#Plotagem univalorada
sns.histplot(gorjeta['total_bill'])
plt.show()
'''
#Plotagem comparada
sns.jointplot(x = 'total_bill', y = 'tip', data =gorjeta)
plt.show()

'''
#em hexagono
sns.jointplot(x = 'total_bill', y = 'tip', data = gorjeta, kind ='hex')
plt.show()

#Com uma linha de tendencia
sns.jointplot(x = 'total_bill', y = 'tip', data = gorjeta, kind ='reg')
plt.show()

#Gráficos comparativos pra todas as variáveis numéricas
sns.pairplot(gorjeta)
plt.show()

#Rugplot ou código de barras
sns.rugplot(gorjeta['total_bill'])
plt.show()


#kde ou em linha
sns.kdeplot(gorjeta['total_bill'])
plt.show().

#Plotagem de categoria
sns.barplot(x = 'sex' , y = 'total_bill', data= gorjeta, estimator= np.std, color = 'red')
plt.show()

'''
'''
Gráfico de caixa
as bolinhas são os valores discrepantes 

a primeira linha da caixa ´o max, 2 é o terceiro qurtil, 3 é a mediana, 4 é o primeiro quartil, 5 o mínimo 

sns.boxplot(x = 'day' , y = 'total_bill', data= gorjeta )
plt.show()

#Gráfico de caixa com fumantes
sns.boxplot(x = 'day' , y = 'total_bill', data= gorjeta, hue = 'smoker' )
plt.show()

#Gráfico de violino
sns.violinplot(x= 'day', y = 'total_bill', data = gorjeta, hue = 'sex', split=True)
plt.show()

#stripplot ou colmeia ou bolinhas
sns.stripplot(x = 'day', y = 'total_bill', data = gorjeta, hue = 'smoker')
plt.show()

#gráfico de enxame parecido com o stripplot, mas as bolinhas estão dispersas nas laterais
sns.swarmplot(x='day', y= 'total_bill', data = gorjeta)
plt.show()

#coringa
sns.catplot(x = 'day', y = 'total_bill', data = gorjeta, kind ='bar')
plt.show()

#plotagem de matriz
voo = sns.load_dataset('flights')

#prints (voo.head())
vp= voo.pivot_table(index = 'month', columns = 'year', values = 'passengers')

sns.heatmap(vp)
plt.show()

sns.clustermap(vp, cmap = 'coolwarm', standard_scale = 1)
plt.show()
'''