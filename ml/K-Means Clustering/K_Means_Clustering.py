# Objective: To implement K-Means Clustering on a dataset and visualize the clusters

# Description:
# This script performs K-Means Clustering on a customer shopping dataset. The steps i did are as follows:
# 1. Load the dataset from a CSV file.
# 2. Preprocess the data by checking for missing values and dropping non-numeric columns.
# 3. Scale the data using RobustScaler to handle outliers.
# 4. Determine the optimal number of clusters using the Elbow Method.
# 5. Apply K-Means Clustering with the optimal number of clusters.
# 6. Visualize the clusters using PCA to reduce the data to 2D.
# 7. Calculate the Silhouette Score to evaluate the clustering performance.
# 8. Optionally, test different values of k to find the best clustering configuration.
# 9. Visualize the clusters again with the updated k value and display the cluster centroids.

# Libraries Used:
# - pandas: For data manipulation and analysis.
# - numpy: For numerical operations.
# - matplotlib: For data visualization.
# - seaborn: For enhanced data visualization.
# - sklearn: For machine learning algorithms and preprocessing.

# Usage:
# Ensure that the dataset 'customer_shopping_data.csv' is in the working directory.
# Run the script using a Python interpreter.

# Example:
# python K_Means_Clustering.py

# Author: Mysterious-Wizard :)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

try:
    # Load dataset from local CSV (ensure file path is correct)
    print("Loading dataset...")
    df = pd.read_csv("customer_shopping_data.csv")  # Make sure the file is in your working directory
    print(df.head())
except Exception as e:
    print("Error loading dataset: ", e)

#Let's Preprocess our data and check for missing values and data types of columns
# Drop duplicates
# Check for missing values
missing_data = df.isnull().sum()
print("Missing values:\n", missing_data)

# Check data types of columns
print("Data Types:\n", df.dtypes)

# Drop non-numeric columns
df_numeric = df.select_dtypes(include=[np.number])

# Check the new dataframe with only numeric columns
print("Numeric columns:\n", df_numeric.head())

# Apply RobustScaler/StandardScaler to scale the data 
#I am experimenting with both scalers to see which one gives me better results
#I have used StandardScaler in previous projects and wanted to try RobustScaler this time
#RobustScaler is less sensitive to outliers than StandardScaler
scaler = RobustScaler()
df_scaled = scaler.fit_transform(df_numeric)

# Check the scaled data
print("Scaled data:\n", df_scaled[:5])

# Inertia values for different cluster numbers
inertia = []
cluster_range = range(1, 11)

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow Method graph to find the optimal number of clusters
# The optimal number of clusters is the value after which the decrease in inertia is minimal
plt.figure(figsize=(8, 6))
plt.plot(cluster_range, inertia, marker='o', linestyle='-', color='b')
plt.title("Elbow Method For Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()

# Apply K-Means with optimal clusters , in my case from the graph i am assuming k=4 is the best value
k = 4
kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Display the dataframe with cluster labels
print(df.head())

# Apply PCA to reduce data to 2D as we can't visualize data in more than 3 dimensions
# Apply PCA to the scaled data
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

# Create a DataFrame with the PCA results and cluster labels
df_pca_df = pd.DataFrame(df_pca, columns=['PCA1', 'PCA2'])
df_pca_df['Cluster'] = df['Cluster']

## Plot the 2D scatter plot with the clusters and PCA components
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca_df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=100, alpha=0.7)
plt.title('Customer Segments (K-Means Clustering)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

# # Calculate the Silhouette Score
sil_score = silhouette_score(df_scaled, df['Cluster'])
print(f"Silhouette Score: {sil_score:.4f}")

# Get cluster centers
cluster_centers = kmeans.cluster_centers_
print("Cluster Centers:\n", cluster_centers)

#Now i am not satisfied with my initial silhouette score , so i am gonna try to find the best value of K

# Test different k values (from 3 to 6)
# best_k = 4
# best_score = -1

#This is an alternate way to find best value of K , the only problem being that this is very computationally expensive
# and on a large dataset like the one i am using , it's gonna take a lot of time to preprocess the data
    # for k in range(3, 7):  # Testing k = 3 to k = 6
    #     kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=42)
    #     df['Cluster'] = kmeans.fit_predict(df_scaled)
        
    #     # Calculate Silhouette Score
    #     score = silhouette_score(df_scaled, df['Cluster'])
    #     print(f"Silhouette Score for k={k}: {score:.4f}")
        
    #     if score > best_score:
    #         best_score = score
    #         best_k = k
    # print(f"\nBest k value: {best_k} with Silhouette Score: {best_score:.4f}")

#You are free to test this commented out code , the results i obtained were k=5 is the best possible in given range
#This specific section of code takes a long period of time to run so be patient if you do decide to test it out

# Apply K-Means with the optimal k=5 since our initial assumption was k=4
k = 5
kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Apply PCA once again to the scaled data
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

# Update the df_pca_df DataFrame with new cluster labels for k=5 clusters
df_pca_df = pd.DataFrame(df_pca, columns=['PCA1', 'PCA2'])
df_pca_df['Cluster'] = df['Cluster']  # Use the updated cluster labels here

# Plot the 2D scatter plot with the updated clusters (k=5)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca_df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=100, alpha=0.7)
plt.title(f'Customer Segments (K-Means Clustering, k={k})')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

# Visualizing the clusters once again with centres this time 
# Plot the 2D scatter plot with cluster centers
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca_df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=100, alpha=0.7)

# Mark cluster centroids with red X
centroids_pca = pca.transform(kmeans.cluster_centers_)  # Transform the cluster centers into 2D
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], s=300, c='red', marker='X', label='Centroids')
plt.title(f'Customer Segments (K-Means Clustering, k={5})')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

# Display the cluster centroids
centroids = kmeans.cluster_centers_
print(f"Cluster Centroids:\n{centroids}")

# Save the DataFrame with cluster labels to a CSV file,this will help us in future analysis
df.to_csv('customer_segments_with_clusters.csv', index=False)
print("Data saved to 'customer_segments_with_clusters.csv'")