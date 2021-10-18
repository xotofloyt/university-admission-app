# Importing the libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('admissions.csv')

X = dataset[['gpa', 'gre']]
y = dataset['admit']


regressor = LogisticRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

prediction = 'Admitted' if model.predict([[2.9, 750]]) else 'Not Admitted'
print()
print(prediction)
print()
