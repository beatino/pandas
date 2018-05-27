# Pandas - Create DataFrames
import os
import numpy as np
import pandas as pd

################################################################################
### Leeres DataFrame erzeugen
df = pd.DataFrame()
print(df.shape)
### DataFrame mit Random Wertem (int Index und Columns)
df = pd.DataFrame(np.random.rand(4,3))
### DataFrame mit Index- und Column- Names
idx = ['n'+str(i) for i in range(4)]
col = list('abc')
df = pd.DataFrame(np.random.rand(4,3), index=idx, columns=col)
################################################################################
### Create DataFrame from Dictionaries, Items und Records
myDict = [{'k1':4, 'k2':6}, {'k1':7, 'k2':3 }]
pd.DataFrame(myDict)
# Create DataFrame from Dictionaries (Spalten orientiert)
myDict = {'k1':[3,3,3,3], 'k2':[9,9,9,9], 'k3': [0,0,0,0]}
pd.DataFrame.from_dict(myDict)
# Create DataFrame from Items (Spalen orientiert)
myDict = [('k1',[3,3,3,3]), ('k2',[9,9,9,9]), ('k3',[0,0,0,0])]
pd.DataFrame.from_items(myDict)
# Create DataFrame from Records Zeilen orientiert
data = [(3,3,3,3),(9,9,9,9),(0,0,0,0)]
labels = ['k1','k2','k3','k4']
pd.DataFrame.from_records(data, columns=labels)
# Create DataFrame aus Zeilen
z1 = [3,3,3,3]
z2 = [9,9,9,9]
z3 = [0,0,0,0]
labels = ['k1','k2','k3','k4']
pd.DataFrame(list([z1, z2, z3]),columns=labels)
# Create DataFrame aus Spalten
k1 = [3,3,3,3]
k2 = [9,9,9,9]
k3 = [0,0,0,0]
labels = ['k1','k2','k3']
pd.DataFrame(list(zip(k1, k2, k3)),columns=labels)
################################################################################
### Rename Column- und Index- Names
df = pd.DataFrame(np.random.rand(4,3))
# Rename Column-Names
df.columns = ['Col1','Col2','Col3']
# Rename Index-Names
df.index = ['z1','z2','z3','z4']
################################################################################
### Spalten oder Zeilen löschen
# Spalten loeschen
df = pd.DataFrame(np.random.rand(4,3), columns=list('abc'))
df.drop(['a','b'],axis=1)
# oder
df.drop(df.columns[[0, 1]], axis=1)
# Zeilen loeschen
df.drop([0, 1], axis=0)
# spezifische Zeilen loeschen
idx = df.index[df['a']>0.8]
df.drop(idx)

