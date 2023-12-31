# -*- coding: utf-8 -*-
"""treatment of outliers in  python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NifWXc8NQFjMJ5fJNq4dwfOfaZUtzIwS
"""

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/House_Price[1].csv',header = 0)

df.info()

np.percentile(df.n_hot_rooms,[99])

np.percentile(df.n_hot_rooms,[99])[0]

UV = np.percentile(df.n_hot_rooms,[99])[0]

df[df.n_hot_rooms > UV]

df[df.n_hot_rooms >3* UV]

df.n_hot_rooms[df.n_hot_rooms >3* UV] = 3*UV

df[df.n_hot_rooms > UV]

np.percentile(df.rainfall,[1])[0]

LV = np.percentile(df.rainfall,[1])[0]

"""# **remove the outlier from rainfall**"""

df[df.rainfall < LV]

df[df.rainfall < 3*LV]

df.rainfall[df.rainfall < 3*LV] = 3*LV

df[df.rainfall < LV]

"""Missing value of imputation in python"""

df = pd.read_csv('/content/drive/MyDrive/House_Price[1].csv',header = 0)

df.info()

df.n_hos_beds = df.n_hos_beds.fillna(df.n_hos_beds.mean())

df.info()

