from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

app = Flask(__name__, static_url_path='/static')

# Load Naive Bayes model
naive_bayes_model = joblib.load('final_naive_bayes_model.joblib')

# Load TF-IDF vectorizer
vectorizer_nb = joblib.load('vectorizer_nb.joblib')

# Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('web_app_temp.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("Received POST request to /predict")
        print("Form data:", request.form)
        sentence = request.form.get('sentence')
        print("Received sentence:", sentence)
        
        # Preprocess input sentence
        sentence_tfidf = vectorizer_nb.transform([sentence])
        sentiment_score = sia.polarity_scores(sentence)['compound']
        input_data = np.hstack((sentence_tfidf.toarray(), np.array(sentiment_score).reshape(-1, 1) + 1))
        
        # Predict using Naive Bayes model
        prediction = naive_bayes_model.predict(input_data)[0]
        
        return render_template('temp_result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
