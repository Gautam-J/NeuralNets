import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC

df = pd.read_csv('titanic_dataset.csv')
X = df.drop(['survived', 'name', 'ticket', 'pclass', 'sex'], axis=1).values

x_cat = df[['pclass', 'sex']]

encoder = OneHotEncoder()
x_ohe = encoder.fit_transform(x_cat).toarray()
joblib.dump(encoder, 'encoder.pkl')

X = np.hstack((X, x_ohe))
y = df['survived'].values

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
joblib.dump(scaler, 'scaler.pkl')

sm = SMOTE(random_state=42)
x_train, y_train = sm.fit_sample(x_train, y_train)

model = SVC()
model.fit(x_train, y_train)
joblib.dump(model, 'model.pkl')

score_train = model.score(x_train, y_train)
score_test = model.score(x_test, y_test)

print(f'Training accuracy: {score_train}')
print(f'Testing accuracy: {score_test}')
