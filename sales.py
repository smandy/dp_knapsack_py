import pylab as pl
import pandas as pd

import os
dir = '../Pandas-Data-Science-Tasks/SalesAnalysis/Sales_Data'

files = [ x for x in os.listdir(dir) if os.path.isfile(os.path.join(dir, x )) ]

df = pd.concat( [ pd.read_csv( os.path.join(dir, x)) for x in files] )
df = df[df['Order Date'] != 'Order Date']

#df = df.isn

df = df[df['Order ID'].notna()]
df['Quantity Ordered'] = df['Quantity Ordered'].astype('int')
df['Price Each'] = df['Price Each'].astype('float')

df['cost'] = df['Quantity Ordered'] * df['Price Each']
df['month'] = df['Order Date'].str[:2].astype('int')

byMonth = df.groupby('month').sum()
byMonth = byMonth.sort_values( by = 'cost')

pl.clf()
pl.bar( byMonth.index, byMonth['cost'] )
