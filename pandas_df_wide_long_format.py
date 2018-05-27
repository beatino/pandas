# Pandas - Long / Wide Format

import os
import numpy as np
import pandas as pd
################################################################################
# Create DataFrame mit id,typ unique und einem Value
m = 10
df = pd.DataFrame(np.random.rand(m,1), columns=['Value'])
df['id'] = np.random.randint(3, size=(m, 1))
df['typ'] = np.random.choice(list('abc'), size=m, replace=True)
df = df.groupby(['id','typ'],as_index=False).mean()
print(df)
################################################################################
# Umwandlung: From Long to Wide Format
wide = df.pivot(index='id',columns='typ',values='Value')
print(wide)
################################################################################
# Umwandung: From Wide to Long Format
wide['id'] = wide.index
long = wide.melt(id_vars=['id'],value_vars=list('abc'))
print(long)

