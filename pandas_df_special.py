# Pandas - Spzielle Funktionen mit DataFrames
import os
import numpy as np
import pandas as pd
################################################################################
# Erste Zeile aus der Gruppe ausgeben
df = pd.DataFrame(np.random.rand(6,3), columns=list('abc'))
df['x'] = ['x1','x2','x1','x1','x3','x2']
df['y'] = ['p','q','q','p','p','q']
print(df)
print(df.groupby(['x','y']).count())
df.groupby(['x','y']).first()
################################################################################
# Funktionsanwendung und Mapping z.B auf Zeilen
df = pd.DataFrame(np.random.rand(4,3), columns=list('abc'))
df['max-min'] = df.apply(lambda x: x.max() - x.min(), axis=1)
df
################################################################################
# Funktionsanwendung elementweise
df = pd.DataFrame(np.random.rand(4,3), columns=list('abc'))
df.applymap(lambda x: '%.2f' %x)
################################################################################
# Sortierung nach Columns
df = pd.DataFrame(np.random.rand(4,3), columns=list('abc'))
df.sort_index(axis=1,ascending=False)
################################################################################
# Sortierung nach Zeilen
df = pd.DataFrame(np.random.rand(4,3), columns=list('abc'))
df.sort_index(axis=0,ascending=False)
################################################################################
# DatenFrames zusammenfuegen (rbind)
df1 = pd.DataFrame(np.random.randint(10, size=(3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.random.randint(10, size=(3, 4)), columns=list('abcd'))
df3 = pd.DataFrame(np.random.randint(10, size=(3, 4)), columns=list('abcd'))
frames = [df1,df2]
frames.append(df3)
#ignore_index=True um Index richtig zu setzen
pd.concat(frames, ignore_index=True)
################################################################################
# DatenFrames zusammenfuegen (cbind)
df1 = pd.DataFrame(np.random.randint(10, size=(3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.random.randint(10, size=(3, 4)), columns=list('abcd'))
frames = [df1]
frames.append(df2)
df = pd.concat(frames, ignore_index=True,axis=1)
df.columns = list('abcdefgh')
df
################################################################################