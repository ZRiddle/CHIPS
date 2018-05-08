# sample/train_model.py
"""
Train model with sklearn package and save out pickle
This will be saved in the cloud storage and hosted
"""

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
import numpy as np


data = pd.read_csv("titanic_data.csv")

# Choose target
y = data.Survived.values

# Data selection and prep
data.fillna(0, inplace=True)
X = data[['Age', 'SibSp', 'Fare']].values

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

if 0:
    # Save out model as pkl file
    with open('model2.pkl', 'wb') as f:
        pickle.dump(clf, f)

x = np.array([[1, 1, 1]])
s = clf.predict_proba(x)[0][1]

print("Probability of Survival = {}".format(s))
