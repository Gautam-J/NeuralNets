import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('iris.csv', names=names)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1:].values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
joblib.dump(scaler, 'scaler.pkl')

encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train.reshape(-1,))
y_test = encoder.transform(y_test.reshape(-1,))
joblib.dump(encoder, 'encoder.pkl')

model = SVC()
model.fit(x_train, y_train)
joblib.dump(model, 'model.pkl')

score_train = model.score(x_train, y_train)
score_test = model.score(x_test, y_test)

print(f'Training accuracy: {score_train}')
print(f'Testing accuracy: {score_test}')
