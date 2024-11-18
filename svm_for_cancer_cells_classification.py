# -*- coding: utf-8 -*-
"""SVM for Cancer Cells classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gky0StxnttMufNVku6RlwQlaZKzCwLCf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cell_df = pd.read_csv('cell_samples.csv')
cell_df.head()

cell_df.info()

malignant_df = cell_df[cell_df['Class']==4][0:200]
benign_df = cell_df[cell_df['Class']==2][0:200]

axes = benign_df.plot(kind='scatter', x='Clump', y='UnifSize', color='blue', label='Benign')
malignant_df.plot(kind='scatter', x='Clump', y='UnifSize', color='red', label='Benign', ax=axes)

cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]
cell_df['BareNuc'] = cell_df['BareNuc'].astype(int)
cell_df.dtypes

cell_df['Mit'].unique()

cell_df.columns
feature_df = cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize',
       'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]

X = np.asarray(feature_df)
y = np.asarray(cell_df['Class'])
X[0:5]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train.shape
X_test.shape
y_train.shape
y_test.shape

from sklearn import svm

classifier = svm.SVC(kernel='rbf', gamma='auto', C=2)
classifier.fit(X_train, y_train)
y_predict = classifier.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_predict))

import pickle as pk

pk.dump(classifier, open('model.pkl', 'wb'))

from google.colab import files
files.download('model.pkl')