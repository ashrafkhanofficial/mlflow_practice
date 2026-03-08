import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import pandas as pd

# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# mlflow.set_experiment('First_expirement')

# mlflow.delete_run('a23de39ccfd84d40988a4106e74e6ac6')
model = mlflow.pyfunc.load_model("models:/first_model/1")
print(model)

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = pd.Series(data.target, name='target')

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # rf = RandomForestClassifier(random_state=42)
# print(X_test.iloc[[0]])
# print(y_test.iloc[0])