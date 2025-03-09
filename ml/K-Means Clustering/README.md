# K-Means Clustering for Customer Segmentation

This project demonstrates how to perform K-Means Clustering on a customer shopping dataset and visualize the resulting clusters. It includes data preprocessing, scaling, optimal cluster determination, clustering, evaluation, and visualization steps.

---

## Table of Contents

- [Overview]
- [Installation]
- [Usage]
- [Project Structure]
- [Code Explanation]
- [Results & Evaluation]
- [Screenshots]


---

## Overview

This project segments customers based on their shopping behavior. The key steps include:

1. **Data Loading & Exploration:** Reading the dataset and performing initial checks.
2. **Data Preprocessing:** Handling missing values, filtering numeric columns, and scaling features using `RobustScaler` (to address outliers).
3. **Determining Optimal Clusters:** Using the Elbow Method and Silhouette Score to identify the best k.
4. **K-Means Clustering:** Implementing the K-Means algorithm with the optimal k (updated from k=4 to k=5 based on evaluation).
5. **Visualization:** Applying PCA to reduce data dimensions to 2D and plotting clusters along with cluster centroids.
6. **Evaluation:** Calculating the Silhouette Score to assess cluster quality.

---

## Installation

Ensure you have **Python 3** installed. Install the required packages using pip:


pip install numpy pandas matplotlib seaborn scikit-learn
Usage
Place the dataset customer_shopping_data.csv in your working directory.

Run the main script:

# Code Explanation
```Below is a summary of the key sections in the code:```

---

**Data Loading & Preprocessing:**
The script loads the CSV file, checks for missing values, and selects numeric columns.
It scales the data using RobustScaler to minimize the effect of outliers.

**Determining Optimal k:**
The Elbow Method is used to plot inertia vs. the number of clusters.
Later on optimal silhouette is also found by iterating through possible values of k.
Based on the plot and optional silhouette analysis, k is updated from 4 to 5.

**Clustering & Visualization:**
K-Means is applied using the optimal k value.
PCA reduces the data to 2D for visualization, and scatter plots display the clusters.
Cluster centroids are overlaid on the PCA scatter plot.

**Evaluation:**
The Silhouette Score is computed to evaluate cluster separation.
Final cluster centers (in the scaled feature space) are printed.

**Optional Saving:**
The final DataFrame with cluster labels is saved as a CSV file for further analysis.

*For a complete code walkthrough, refer to the in-line comments in K_Means_Clustering.py.*

## Results & Evaluation

**Elbow Method:**
The inertia plot suggested an initial guess of k=4, but further analysis indicated that k=5 provides better separation.

**Silhouette Score:**
After updating to k=5, the silhouette score improved (though moderate), indicating better-defined clusters.

**Visualization:**
The PCA scatter plots clearly show the clusters. The centroids (marked with red X's) are overlaid to indicate cluster centers. These visuals help in understanding how customers are segmented based on their shopping behavior.

**Final Output:**
The final DataFrame with the updated cluster labels is saved to customer_segments_with_clusters.csv for future reference.

---

# Screenshots
Below are some sample screenshots from the project i took:

## Elbow Method Plot:

![Figure_1](https://github.com/user-attachments/assets/925b1765-d26e-4b14-8a7f-78b2e7cf9bd7)

## PCA Cluster Scatter Plot (k=4):

![Figure_2](https://github.com/user-attachments/assets/8b9f3cf6-37c8-4cc9-a5b0-e2291bde795c)

## PCA Cluster Scatter Plot(k=5):
![Figure_3](https://github.com/user-attachments/assets/54c761bf-a7f9-425d-90fe-15e49d55687b)


## Cluster Centroids Visualization:

![Figure_4](https://github.com/user-attachments/assets/3c4ceeb6-39db-49cb-9fec-b2b8c9a599f4)

---
# THANK YOU FOR READING THIS :)

