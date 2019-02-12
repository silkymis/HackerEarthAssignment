import numpy as np
import pandas as pd
import sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report

import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

def nbTrainer(X_train, X_test, y_train, y_test):
    mnb = MultinomialNB()
    model = mnb.fit(X_train, y_train)
    nbTestPredictor(model,X_test, y_test)
    return model

def transformPrediction(preds):
    preds.astype(int)
    preds[preds <3] = -1
    preds[preds ==3] = 0
    preds[preds >=4] = 1
    return preds

def nbTestPredictor(model, X_test,y_test):
    preds = model.predict(X_test)
    print(confusion_matrix(y_test ,preds))
    print(classification_report(y_test, preds))    

def nbPredictor(model,review):
    pred = model.predict(review)
    pred = transformPrediction(pred)
    return pred