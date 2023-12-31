# -*- coding: utf-8 -*-
"""Linear regression canada percapita prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANZSikVCqmnjufcL1bRu3EJqyZCyyLx6
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('canada_per_capita_income.csv')
df['per capita income (US$)']

plt.xlabel("year")
plt.ylabel("per capita")
plt.scatter(df.year,df['per capita income (US$)'],color='green',marker='+')

k = df.drop('per capita income (US$)',axis='columns')
k

reg = linear_model.LinearRegression()
reg.fit(k,df['per capita income (US$)'])

reg.predict([[2016]])