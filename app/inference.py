import numpy as np
import joblib
import os
import pandas as pd

model_path = os.path.join('model', 'model.pkl')

try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    exit()

sample_input = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
try:
    prediction = model.predict(sample_input)
    print(f"✅ Prediction: {prediction}")
except Exception as e:
    print(f"❌ Failed to make prediction: {e}")
