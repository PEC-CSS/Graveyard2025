# Simple Linear Regression with Pipeline  
*Predicting California Housing Prices Using Median Income*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This project implements **Simple Linear Regression** on the California Housing dataset using scikit-learn’s Pipeline. The goal is to predict house prices based on the **Median Income (MedInc)** feature. The main way i solved this can be divided into following steps:

- Data Loading & Exploration
- Preprocessing and Feature Scaling
- Building a Pipeline for model training and storing it 
- Hyperparameter Tuning using GridSearchCV
- Model Evaluation & Visualization

---

## Features

- **Data Exploration:** Basic EDA with using describe(),info(), and scatter plots.
- **Pipeline Approach:** Integrates preprocessing (scaling) and regression into one streamlined pipeline, I preferred using pipeline because it is portable and in general used in ML as industry standard.
- **Hyperparameter Tuning:** Uses GridSearchCV to optimize hyperparameters(the parameters which model uses for the regression ,in general parameters are called as hyperparameters in ML) for Linear Regression.
- **Visualization:** Generate a scatter plot for visualisation and EDA and regression plot that displays the fitted line alongside actual data.

---

## Installation

Ensure you have **Python 3** installed. Then, install the required packages with:

pip install numpy pandas matplotlib seaborn scikit-learn joblib scipy
Code Explanation
1. Data Loading & Exploration
Dataset: The California Housing dataset is loaded using fetch_california_housing(), then converted into a Pandas DataFrame.
EDA: Basic exploration is performed using head(), info(), and describe(). A scatter plot visualizes the relationship between Median Income and House Price.
2. Preprocessing
Feature Selection: The predictor is MedInc (Median Income) and the target is Price.
Train-Test Split: The data is split into training (70%) and testing (30%) sets.
Scaling: StandardScaler standardizes the features to ensure the model’s performance.
3. Pipeline Creation & Model Training
A Pipeline is constructed with two steps: scaling and linear regression.
The model is trained on the training set.
4. Hyperparameter Tuning
GridSearchCV is used to optimize hyperparameters for the Linear Regression model.
5. Evaluation & Visualization
The optimized model is evaluated on the test set using Mean Squared Error (MSE) and R² Score.
A regression plot is generated to visualize the fitted regression line against actual data.
6. Model Persistence
The final optimized pipeline is saved using joblib.dump() so it can be loaded and used for predictions later.
How to Run

---

**Run the main script:**
_python Simple Linear Regression.py_
This trains the model, prints evaluation metrics, displays the regression plot, and saves the optimized pipeline as optimized_linear_regression_pipeline.pkl.

**Make Predictions:**
Use the provided predict.py script to load the saved model and predict house prices:
_python predict.py --medinc 3.5_

---
# Images
---
## Scatter Plot
![Figure_1](https://github.com/user-attachments/assets/527d1f77-cafb-4d19-b59c-34df0d413c0d)



## Regression Plot:
![Figure_2](https://github.com/user-attachments/assets/dee4f48d-6b01-49ad-ab93-20a48cedd612)


## Prediciton Result 
![Screenshot 2025-02-16 230933](https://github.com/user-attachments/assets/14d5d91c-17fd-4c78-af9b-d9aef2f62f7e)

