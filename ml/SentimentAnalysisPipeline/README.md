# 📌 Sentiment Analysis of IMDB Movie Reviews

This project is all about **teaching a machine to understand emotions in text!** I built a sentiment analysis pipeline that classifies **IMDB movie reviews** into **positive or negative** sentiments.  

We dive into **data preprocessing, feature extraction (TF-IDF), training machine learning models (Logistic Regression & Naive Bayes), evaluating results, and visualizing predictions** with confusion matrices.  

---  

##  Table of Contents
- [Overview]
- [Installation]  
- [Usage] 
- [Code Explanation]  
- [Results & Evaluation]  
- [Images]  

---

##  Overview  
In this project, I analyzed **50k** IMDB reviews  to determine whether they express a **positive** or **negative** sentiment.   

 ## **What I Did:**  
 **Loaded & cleaned** the dataset (removed HTML, special characters, stopwords)  
 **Transformed text into numerical features** using **TF-IDF**  
 **Trained two machine learning models**:  
   - **Logistic Regression**  (*Best performer!*)  
   - **Multinomial Naive Bayes**  
 **Evaluated model accuracy & visualized results**  

### **Goal:** 
Automatically predict whether a given review is **positive** or **negative** based on its text.  

---

##  Installation
To run this project, you need **Python 3** and some essential libraries. Install them using:  

```bash
pip install numpy pandas nltk seaborn matplotlib scikit-learn beautifulsoup4
```

---

##  Usage
1️ **Download the dataset**: 
*Installation link-*    ``` 
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews?resource=download ```
 - Make sure **IMDB_Dataset.csv** is in the same folder as the script.  
---
2️ **Run the script**:  
```bash
Sentiment_Analysis_Pipeline.py
```

3️ **See the results!**  
- The model will train, evaluate, and display **accuracy, confusion matrices, and sentiment predictions.**  

---

##  Code Explanation
### 1️ Data Preprocessing  
- **I cleaned the text** (removed HTML, square brackets, special characters).  
- **Lowercased everything** for consistency.  
- **Tokenized words** and **removed stopwords** using NLTK.  
- **Lemmatized words** (converted to base form, e.g., "running" → "run").  

### 2️ Feature Extraction (TF-IDF)
- Converted processed text into **numerical vectors** using **TF-IDF**.  
- Kept **only the top 5000 most important words** to improve accuracy.  

### 3️ Model Training & Evaluation
- **Tried two models**:  
  - **Logistic Regression** ( **Best performer!**)  
  - **Multinomial Naive Bayes**  
- **Checked accuracy, precision, recall, and F1-score.**  
- **Final Model Choice:** **Logistic Regression (88.79% accuracy)**  

### 4 Visualization
- Plotted **Confusion Matrices** to see how well the models performed.  

---

##  Results & Evaluation
###  Accuracy Scores

| **Logistic Regression**   | **88.79%** |
| **Multinomial Naive Bayes**   | **85.83%**   |

- Logistic Regression **performed better** with **higher accuracy and precision.**  
- Naive Bayes **was slightly worse** but still decent.If there is no need for higher accuracy ,
  I would prefer Naive Bayes because it's less computationally expensive (more efficient). 

#  Images


##  Confusion Matrices 

**These show how well the model predicted**

### **Confusion Matrix for Logistic Regression:**  

![Figure_1](https://github.com/user-attachments/assets/5895cbd1-5e67-4ed5-b45b-a0a0bab75dfc)

 ### **Confusion Matrix for Naive Bayes:**  
![Figure_2](https://github.com/user-attachments/assets/9d197a10-0b7e-454d-8e8d-6126bab8705f)

---
##  Conclusion
 **What I Learned:**  
 Cleaning and preprocessing text is **crucial** for accurate sentiment analysis.  
 **TF-IDF** helps extract **important words** without making the dataset too big.  
 **Logistic Regression** is **the best choice** for this dataset if our priority is high accuracy , i also could have tried **support vector machines (SVM)** 
but they are generally slower than the models used in this project , though it could be a good practice project to compare accuracy of all 3 models.

 **Next Steps (Future Improvements):**  
 Try **deep learning models (LSTMs, Transformers)** for better accuracy.  
 Add **a real-time user interface** (e.g., a chatbot that predicts sentiment).  
 Experiment with **more datasets (Twitter, Amazon Reviews, etc.)**.  

---

##  Thank You for Reading!
Hope this project helps you understand **Sentiment Analysis with ML!** If you have any questions, feel free to **modify, test, and improve it.**  

Let’s keep building cool AI stuff! :)

