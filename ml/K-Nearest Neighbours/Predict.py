import joblib
import numpy as np

# Load the optimized model
model = joblib.load("optimized_knn_pipeline.pkl")

# New sample data (ensure same feature format)
new_data = np.array([[5.1, 3.5, 1.4, 0.2]]) 

# Predict
prediction = model.predict(new_data)
print("Predicted Species:", prediction[0])
