# Suicidal Language Detection and Topic Modelling (Year 3 Sem 2)(2024)

This project focuses on detecting suicidal language from Reddit posts and exploring key topics related to mental health using machine learning and NLP techniques. The goal is to help mental health professionals identify potential signs of suicidal ideation early and provide relevant support.

## Key Features

### 1. **Classification Models**
We developed and evaluated three classification models to identify whether texts were suicidal or non-suicidal:
- **Random Forest**
- **Naive Bayes** (best performing model for human evaluation)
- **Support Vector Machine (SVM)**

The models were assessed based on accuracy, precision, recall, and F1-score. The best-performing model was Naive Bayes, determined through human evaluation on generated test cases.

### 2. **Topic Modelling**
We applied three topic modelling techniques to uncover common themes within suicidal and non-suicidal texts:
- **Non-negative Matrix Factorization (NMF)**
- **Latent Dirichlet Allocation (LDA)**
- **BERTopic** (best model for topic coherence and meaningful clusters)

Each model was evaluated based on coherence scores, human evaluation, and the number of distinct topics generated. BERTopic produced the most coherent topics with minimal overlap.

### 3. **Results and Insights**
- **Classification**: The Naive Bayes model provided the most accurate classification of suicidal texts based on human-generated test cases.
- **Topic Modelling**: BERTopic revealed distinct clusters like *Mental Health Challenges*, *Media Engagement*, and *Self-Image and Physical Appearance*. These insights help mental health organizations identify key areas to focus on for suicide prevention.

### 4. **Demonstration**
- A **web application** was developed to classify texts and detect potential suicidal ideation. Users can input a sentence, and the app will predict whether it contains suicidal intent using the Naive Bayes model.
- **Topic modelling visualization** includes interactive charts and word clouds to help NGOs and mental health professionals understand patterns in suicidal discussions.

### 5. **Business Case**
Our solution can be used by mental health organizations and the Singapore government to monitor social media for early detection of suicidal behavior. This will help in running targeted interventions and raising awareness on prevalent topics like self-image and mental health.

### 6. **Challenges and Future Work**
- **Limitations**: The dataset was limited to English language posts and users from a specific age demographic (mainly Reddit users aged 18-49).
- **Future Work**: We plan to expand data collection to include more diverse social media platforms and improve our models by incorporating multilingual datasets.

### 7. **Generative AI**
We utilized generative AI to:
- Explore different text-mining approaches.
- Fine-tune models.
- Generate prompts for model testing and evaluation.
- Develop ideas for the implementation of our web application.

## Conclusion
Our project has laid a strong foundation for the early detection of suicidal language using text classification and topic modelling. In the future, we aim to enhance the models by using a larger and more diverse dataset and further refining the models for better accuracy.

For more detailed results and analysis, please refer to the individual sections of the code and report.
