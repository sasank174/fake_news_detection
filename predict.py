import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

import joblib

ps = PorterStemmer()

cv = joblib.load("models/cv.sav")
model1 = joblib.load("models/naviebayes.sav")
model2 = joblib.load("models/randomforest.sav")
model3 = joblib.load("models/decisiontree.sav")


def predict(text):
    input_data = []
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    input_data.append(text)
    X = cv.transform(input_data).toarray()
    t = []
    t.append(model1.predict(X)[0])
    t.append(model2.predict(X)[0])
    t.append(model3.predict(X)[0])
    return max(set(t), key = t.count)