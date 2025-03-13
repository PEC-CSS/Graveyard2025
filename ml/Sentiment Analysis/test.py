import pickle
import numpy as np
from Sentiment_Analysis_Pipeline import preprocess_text, tfidf, lr, mnb

#  Welcome message
print("\n Sentiment Analysis Test ")
print("Enter a movie review, and I'll predict if it's POSITIVE or NEGATIVE!")

while True:
    #  Take user input
    user_review = input("\nType your review (or type 'exit' to quit): ").strip()
    
    if user_review.lower() == "exit":
        print("\n Exiting sentiment analysis. Have a great day! ")
        break

    #  Preprocess the input review
    processed_review = preprocess_text(user_review)

    #  Convert text into numerical features using TF-IDF
    review_features = tfidf.transform([processed_review])

    #  Get predictions from both models
    lr_prediction = lr.predict(review_features)[0]
    mnb_prediction = mnb.predict(review_features)[0]

    #  Print results
    print("\n Results:")
    print(f" **Logistic Regression Prediction:** {'Positive ' if lr_prediction == 1 else 'Negative '}")
    print(f" **Naive Bayes Prediction:** {'Positive ' if mnb_prediction == 1 else 'Negative '}")

    print("\n🎬 Try another review or type 'exit' to quit.")
