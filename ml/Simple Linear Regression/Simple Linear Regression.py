import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
housing = fetch_california_housing()
df = pd.DataFrame(data=housing.data, columns=housing.feature_names)
df['Price'] = housing.target

# 2. Exploratory Data Analysis 
print(df.head())
print(df.info())
print(df.describe())
sns.scatterplot(x='MedInc', y='Price', data=df)
plt.show()

# 3. Select one feature for simple regression
X = df[['MedInc']]  # Single feature (Median Income)
y = df['Price']

# 4. Train-Test Split (70-30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5. Define Pipeline
regression_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# 6. Define Hyperparameter Grid
param_grid = {
    'regressor__fit_intercept': [True, False],  # Include intercept or not
    'regressor__n_jobs': [-1, 1]  # Use all CPU cores or just one
}

# 7. Perform Hyperparameter Tuning using GridSearchCV
grid_search = GridSearchCV(regression_pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)

# 8. Get the Best Model
best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

# 9. Evaluate on test set
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}\n")
print(f"\nR² Score: {r2:.2f}\n")

# 10. (Optional) Visualize the regression line
X_test_sorted = np.sort(X_test, axis=0)
y_pred_line = best_model.predict(X_test_sorted)

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test_sorted, y_pred_line, color='red', label='Regression Line')
plt.xlabel("\nMedian Income\n")
plt.ylabel("\nHouse Price\n")
plt.title("\nSimple Linear Regression - California Housing\n")
plt.legend()
plt.show()

# 11. Save the best pipeline
joblib.dump(best_model, "optimized_linear_regression_pipeline.pkl")
print("\nOptimized model pipeline saved as 'optimized_linear_regression_pipeline.pkl'.")
