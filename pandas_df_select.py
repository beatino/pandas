# Pandas - Select, groupby and merge with DataFrames
import os
import numpy as np
import pandas as pd
################################################################################
### Select
df = pd.DataFrame(np.random.rand(6,3), columns=list('abc'))
df[['a','c']]
################################################################################
### Filter
idx = df.index[df['a']>0.5]
df.loc[idx,:]
################################################################################
### Mutate
idx = df.index[df['a']>0.5]
df.loc[idx,'b'] = 777
################################################################################
### Group By
df = pd.DataFrame(np.random.rand(6,3), columns=list('abc'))
df['x'] = ['x1','x2','x1','x1','x3','x2']
# Gruppierung nach Spalte x (Spalte x als Index)
df.groupby('x').sum()
# Gruppierung nach Spalte x (Spalte x bleibt Spalte)
df.groupby('x', as_index=False).sum()
# Gruppierung mit Fallunterscheidung
df.groupby(df['a']>0.5, as_index=False).sum()
# mehrere Aggregationen
df.groupby('x', as_index=False).agg([np.sum, np.mean, np.size])
# spezifische Ausgabe
dx = df.groupby('x', as_index=False).agg([np.sum, np.mean, np.size])
dx = dx.loc[:,[('a','sum'),('a','size')]]
dx.columns = ['sum','size']
# mehrere Aggregationen von spezifischen Spalten
df.groupby('x', as_index=False).agg({'a':np.mean, 'b':np.sum, 'c':np.size})
################################################################################
### Merge / Join
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html
# inner join
df1 = pd.DataFrame(np.random.rand(6,3), columns=list('abc'))
df1['x'] = ['x1','x2','x1','x1','x3','x2']
df2 = pd.DataFrame.from_dict({'x':['x1','x2','x3'], 'k2':[1,2,3], 'k3': [7,6,5]})
df1.merge(df2)
# oder
df1.merge(df2,on=['x'],how='inner')
# inner join nach groupby (miitels Index)
dx = df.groupby('x').sum()
df2.merge(dx, left_on='x', right_index=True)
# inner join mit unterschiedlichen Spalten Namen
df3 = pd.DataFrame.from_dict({'w':['x1','x2','x3'], 'k2':[1,2,3], 'k3': [7,6,5]})
df1.merge(df3,left_on=['x'],right_on=['w'],how='inner')


################################################################################
### Group By plus plus
df = pd.DataFrame(np.random.rand(6,3), columns=list('abc'))
df['x'] = ['x1','x2','x1','x1','x3','x2']
df['y'] = ['p','q','q','p','p','q']
df.groupby(['x','y']).first()
