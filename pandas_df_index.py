# Pandas - Ausgaben und Zuweisungen in DataFrames

import os
import numpy as np
import pandas as pd

################################################################################
### Pandas Indices
# Pandas DataFrame haben Zeilen und Spalten Indices. Man kann ueber Integer-
# Positionen oder uerber Labels auf Zellen, Zeilen oder Spalten zugreifen.

### Zeilenausgabe mit `iloc` und `loc`
# `iloc` gibt Zeilen (oder Spalten) an den Index-Positionen aus (nur Integer)  
# `loc` gibt Zeilen (oder Spalten) vom den Index-Labels aus

df = pd.DataFrame(np.random.rand(10,3), columns=list('abc'))

################################################################################
### Ausgabe einzelner Zellen
# spezifische Zelle ausgeben mit Integer Indices
df.iloc[1,1]
# oder
df.iat[1,1]
# spezifische Zelle ausgeben mit Label ausgeben
idx = df.index[4]
df.loc[idx,'c']
# oder
df.at[idx,'c']
################################################################################
### Zeilen ausgeben
# dritte Zeile ausgeben (Zeile mit Index=2)
df.iloc[2,:]
# die ersten drei Zeilen ausgeben
df.iloc[:3,:]
# oder 
df[:3]
# Zeilen von 7 bis zur letzten Zeile ausgeben
df.iloc[7:,:]
# oder
df[7:]
# letzten zwei Zeilen ausgeben
df.iloc[-2:,:]
# oder
df[-2:]
# zwei Zeile (2 und 3) ausgeben (exklusiv Ende)
df.iloc[2:4,:]
#### Spezifische Zeilen ausgeben (Bedingte Ausgabe)
# spezifische Zeilen ausgeben (nicht iloc verwenden!)
# iloc würde nur bei Integer Indices funktionieren
idx = df.index[df['b']>0.6]
df.loc[idx.values]
################################################################################
### Spalten Ausgabe
# Spalte b ausgeben
df['b']
# oder 
df.loc[:,'b']
# Spalte a und c ausgeben
df[['a','c']]
# oder
df.loc[:,['a','c']]
# zweite Spate ausgeben 
df.iloc[:,[1]]
# erste und dritte Spalte ausgeben
df.iloc[:,[0,2]]
# letzte Spalte ausgeben
df.iloc[:,-1:]
# letzten beiden Spalte ausgeben
df.iloc[:,-2:]
#### Spezifische Spalten ausgeben (Bedingte Ausgabe)
# Spalten mit erste Zeile groesser als Schwellwert ist
clx = df.columns[df.iloc[0,:]>0.6]
df.loc[:,clx]
################################################################################
### Wert einer Zellen Zuweisungen
# Spezifischer Zelle einen Wert zuweisen
df.at[2,'c'] = 3.0
df.iat[1,1] = 4.0
df.iloc[2,2] = 7
df.loc[df.index[0],'a'] = 8
### Werte mehreren Zellen Zuweisungen
# Wert 0.0 an spezifische Zeilen zuweisen
idx = df.index[df['a']>0.7]
df.loc[idx,['c']] = 0.0
# oder mit einer anderen Bedingung
idx = df.index[(df['a']>0.7) & (df['b']>0.3)]
df.loc[idx,['c']] = 0.0
# Zuweisung an mehrere spezifische Zellen 
idx = np.random.choice(range(9), 5, replace=False)
clx = np.random.randint(3, size=(5))
for q,p in zip(idx,clx):
    df.iloc[q,p] = np.NaN
# Ausgabe mit List Comprehension
[df.iloc[q,p] for q,p in zip(idx,clx)]
################################################################################
### np.NaN
# NaN ersetzen 
df.fillna(9.0)
# Zellen mit NaN bestimmen und dann loeschen
idx = df.index[df['b'].isnull()]
df.drop(idx)