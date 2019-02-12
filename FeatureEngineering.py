import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def countVectorizer(documents, max_df, min_df, max_features):
    cv = CountVectorizer(max_df=max_df, min_df=min_df, max_features=max_features)
    cv_features = cv.fit_transform(documents)
    return cv, cv_features

def tfidf_vectorizer(documents, max_df=1.0, min_df=0.01,
                     max_features=20000, use_idf=True, ngram_range=(1,1)):
    
    tfidf_vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df,
                                       max_features=max_features, 
                                       use_idf=use_idf, ngram_range=ngram_range)
    tfidf_feature_matrix = tfidf_vectorizer.fit_transform(documents)
    return tfidf_vectorizer, tfidf_feature_matrix