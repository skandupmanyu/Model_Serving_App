import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('./california_housing_train.csv')
print('Read data')

X = df[['housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']]
y = df['median_house_value']

model_rf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=20)
model_rf.fit(X, y)

print('Model trained')

with open('model_rf.pkl', 'wb') as f:
  pickle.dump(model_rf, f)

print('Saved pickle')

data = {'housing_median_age': 15.0,
        'total_rooms': 5612.0,
        'total_bedrooms': 1283.0,
        'population': 1015.0, 
        'households': 472.0, 
        'median_income': 1.4936}

print('Prediction: ', model_rf.predict([list(data.values())])[0])