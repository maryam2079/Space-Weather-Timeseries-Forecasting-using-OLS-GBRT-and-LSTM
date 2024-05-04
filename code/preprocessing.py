import pandas as pd
import numpy as np



#Preprocess
def clean(data):
  clean = data.copy()
  target = data.columns[data.isna().any()].tolist()
  for t in target:
    index = clean[clean[t].isna()].index
    for idx in index:
      clean.loc[idx, t] = clean.loc[0:idx, t].mean()

  return clean


