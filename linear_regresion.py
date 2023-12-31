# -*- coding: utf-8 -*-
"""linear_regresion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NX9u4m-HrjHGzO6GxUKaZSKAb6cxllrp
"""

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("/content/drive/MyDrive/House_Price[1].csv",header = 0)

df.head()

df.shape

df.describe()

sns.jointplot(x = 'n_hot_rooms',y = 'price',data = df)

sns.jointplot(x = 'rainfall',y = 'price',data = df)

sns.jointplot(x = 'crime_rate',y = 'price',data = df)

sns.countplot(x = 'airport', data = df)

sns.countplot(x = 'bus_ter', data = df)

sns.countplot(x = 'waterbody', data = df)