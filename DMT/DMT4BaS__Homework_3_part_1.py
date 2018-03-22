#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:41:40 2017

@author: Dovla
"""

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from nltk import word_tokenize

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sklearn import metrics

import pprint as pp

from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

stemmer = EnglishStemmer()
def stemming_tokenizer(text):
	stemmed_text = [stemmer.stem(word) for word in word_tokenize(text, language='english')]
	return stemmed_text

data_folder_training_set = "./Training"
data_folder_test_set     = "./Test"

training_dataset = load_files(data_folder_training_set)
test_dataset = load_files(data_folder_test_set)

print(training_dataset.target_names)

# Load Training-Set
X_train, X_test_DUMMY_to_ignore, Y_train, Y_test_DUMMY_to_ignore = train_test_split(training_dataset.data,
													training_dataset.target,
													test_size=0.0)
target_names = training_dataset.target_names

# Load Test-Set
X_train_DUMMY_to_ignore, X_test, Y_train_DUMMY_to_ignore, Y_test = train_test_split(test_dataset.data,
													test_dataset.target,
													train_size=0.0)
target_names = training_dataset.target_names
print(Y_train.shape)
print(Y_test.shape)
print(target_names)



vectorizer = TfidfVectorizer(strip_accents= None,
							preprocessor = None,
							)
#nbc = MultinomialNB()
knnC = KNeighborsClassifier()

pipeline = Pipeline([
	('vect', vectorizer),
	('knnC', knnC),
	])

parameters = {
	'vect__tokenizer': [None, stemming_tokenizer],
	'vect__ngram_range': [(1, 1), (1, 2),],
	#'nbc__alpha': [.001,.01, 1.0, 10.],
    'knnC__n_neighbors':[3,5,10],
    'knnC__leaf_size':[30,50],
	}

grid_search = GridSearchCV(pipeline,
						   parameters,
						   scoring=metrics.make_scorer(metrics.matthews_corrcoef),
						   cv=10,
						   n_jobs=2,
						   verbose=10)

grid_search.fit(X_train, Y_train)


Y_predicted = grid_search.predict(X_test)

# Evaluate the performance of the classifier on the original Test-Set
#####################################################3
output_classification_report = metrics.classification_report(
									Y_test,
									Y_predicted,
									target_names=target_names)
print(output_classification_report)

# Compute the confusion matrix
confusion_matrix = metrics.confusion_matrix(Y_test, Y_predicted)
print("Confusion Matrix: True-Classes X Predicted-Classes")
print(confusion_matrix)

print("Matthews Corr Coef")
pp.pprint(metrics.matthews_corrcoef(Y_test, Y_predicted))

pp.pprint(grid_search.best_params_)

print("Accuracy")
pp.pprint(metrics.accuracy_score(Y_test, Y_predicted))