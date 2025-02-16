import joblib
import numpy as np

# Load the saved pipeline
model = joblib.load("optimized_linear_regression_pipeline.pkl")

# Function to predict house price based on Median Income
def predict_price(medinc):
    if not (0.5 <= medinc <= 15.0):
        print("⚠️ Warning: Input out of trained range (0.5 - 15.0). Prediction may be inaccurate.")
    
    medinc_array = np.array([[medinc]])  # Reshape input for model
    prediction = model.predict(medinc_array)
    return prediction[0]

# Example usage
if __name__ == "__main__":
    medinc = float(input("Enter Median Income (0.5 - 15.0): "))
    price = predict_price(medinc)
    print(f"Predicted House Price: ${price:.2f}")
