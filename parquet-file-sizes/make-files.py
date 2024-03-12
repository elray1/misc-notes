from itertools import product
from string import ascii_lowercase
import pandas as pd
import numpy as np
import datetime

def make_df(temp_scale, n_samples):
  if temp_scale == 'd':
    horizons = np.arange(-27, 8)
  else:
    horizons = np.arange(-4, 2)
  
  df = pd.DataFrame.from_records(
    list(product(
      [pd.to_datetime('2024-01-26')],
      horizons,
      np.arange(50).astype('str'),
      np.arange(30).astype('str'),
      ['sample'],
      np.arange(n_samples)
    )),
    columns = ['nowcast_date', 'horizon', 'location', 'lineage', 'output_type', 'output_type_id']
  )

  df['target_date'] = df['nowcast_date'] + pd.to_timedelta(df['horizon'], temp_scale)
  df['value'] = np.random.standard_normal(df.shape[0])
  
  return df


df1 = make_df('d', 100)
df1.to_parquet('parquet-file-sizes/example1.parquet')
df1.shape

df2 = make_df('d', 500)
df2.to_parquet('parquet-file-sizes/example2.parquet')
df2.shape

df3 = make_df('w', 100)
df3.to_parquet('parquet-file-sizes/example3.parquet')
df3.shape

df4 = make_df('w', 500)
df4.to_parquet('parquet-file-sizes/example4.parquet')
df4.shape
