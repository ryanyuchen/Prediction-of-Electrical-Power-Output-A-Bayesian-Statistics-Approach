# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:13:29 2019

@author: Yu Chen
"""

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_excel('Folds5x2_pp.xlsx', sheet_name='Sheet1')
usedData = data[:60]
y = usedData['PE']
X = usedData[['AT', 'V', 'AP', 'RH']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
Train = pd.concat([X_train, y_train], axis=1)
Test = pd.concat([X_test, y_test], axis=1)
Train.to_csv('TrainingData.dat', sep=' ', index=False)
Test.to_csv('ValidatingData.dat', sep=' ', index=False)
