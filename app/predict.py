import joblib
import numpy as np

model = joblib.load("app/model.joblib")

def predict(features):
    """
    features: list [sepal_length, sepal_width, petal_length, petal_width]
    returns: predicted Iris species as text
    """
    X = np.array([features])
    pred = model.predict(X)[0]

    species = ["Setosa", "Versicolor", "Virginica"]
    return species[pred]
