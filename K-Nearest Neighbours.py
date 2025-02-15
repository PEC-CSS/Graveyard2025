# Stage 1: Environment Setup & Data Preparation for KNN
#Ensure necceary libraries are imported
#pip install numpy pandas scikit-learn joblib scipy matplotlib seaborn

# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # For saving and loading the model

# Scikit-learn imports for pipeline and modeling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

# Step 2: Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Step 3: Preprocess the Data
X = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Step 4: Define a Pipeline for Scaling and Model Training
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5, weights='distance'))
])

# Step 5: Train the model using the pipeline
knn_pipeline.fit(X_train, y_train)

# Step 6: Save the trained pipeline
joblib.dump(knn_pipeline, "knn_model_pipeline.pkl")

# Step 7: Predict using the pipeline
y_pred = knn_pipeline.predict(X_test)

# Step 8: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("KNN Classification Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Stage 2: Model Optimization (Hyperparameter Tuning)
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats as stats

param_dist = {
    'knn__n_neighbors': stats.randint(3, 16),
    'knn__weights': ['uniform', 'distance'],
    'knn__metric': ['euclidean', 'manhattan']
}

random_search = RandomizedSearchCV(knn_pipeline, param_distributions=param_dist, n_iter=20, cv=5, scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)

# Display best parameters and accuracy
print("Best Hyperparameters Found:", random_search.best_params_)
print("Best Cross-Validation Accuracy: {:.2f}%".format(random_search.best_score_ * 100))

# Step 9: Evaluate the best model
y_pred_best = random_search.best_estimator_.predict(X_test)
print("\nTest Accuracy of Best Model: {:.2f}%".format(accuracy_score(y_test, y_pred_best) * 100))
print("\nClassification Report for Best Model:")
print(classification_report(y_test, y_pred_best))

# Step 10: Save the optimized model
joblib.dump(random_search.best_estimator_, "optimized_knn_pipeline.pkl")

print("\nFinal optimized model saved as 'optimized_knn_pipeline.pkl'.")
