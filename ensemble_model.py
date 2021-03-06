# -*- coding: utf-8 -*-
"""ensemble_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GIX57ipvTRuMyCTVI-JfeH223PyU925m
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/drive/MyDrive/assessment/Train.csv')
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()

y = df['target']

df.drop(['target'],axis=1,inplace=True)

X = df.iloc[:,:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.1,random_state=40)

from sklearn.model_selection import RandomizedSearchCV

rf_reg = RandomForestRegressor()

param = {'n_estimators': [int(x) for x in np.linspace(start=10,stop=500,num=10)],
         'max_features': [1,3,4,6,8,9],
               'max_depth': [int(x) for x in np.linspace(1, 20, num = 3)],
               'min_samples_leaf': [1, 2,4,5,9,10,11],
         }

rf_random = RandomizedSearchCV(estimator=rf_reg,param_distributions=param,scoring='r2',n_iter =5, cv =7, random_state=0, n_jobs = -1)
rf_random.fit(X_train,y_train)

rf_random.best_params_

print("traning Score",rf_random.score(X_train,y_train))
print("test Score",rf_random.score(X_test,y_test))

rf_regs = RandomForestRegressor(max_depth=10,max_features=6,min_samples_leaf=2,n_estimators=115)

rf_regs.fit(X_train,y_train)

print("traning Score",rf_regs.score(X_train,y_train))
print("test Score",rf_regs.score(X_test,y_test))

test = pd.read_csv('/content/drive/MyDrive/assessment/test.csv')
test.drop(['Unnamed: 0','target'],axis=1,inplace=True)
test.head()

x_test = test.iloc[:,:]

y_pred = rf_regs.predict(x_test)

add = pd.read_excel('/content/drive/MyDrive/assessment/Test Set.xlsx')

add['rf_target'] = y_pred

