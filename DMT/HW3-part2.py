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

X_train, X_test_DUMMY_to_ignore, Y_train, Y_test_DUMMY_to_ignore = train_test_split(training_dataset.data,
													training_dataset.target,
													test_size=0.0)
target_names = training_dataset.target_names

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

output_classification_report = metrics.classification_report(
									Y_test,
									Y_predicted,
									target_names=target_names)
print(output_classification_report)

confusion_matrix = metrics.confusion_matrix(Y_test, Y_predicted)
print("Confusion Matrix: True-Classes X Predicted-Classes")
print(confusion_matrix)

print("Matthews Corr Coef")
pp.pprint(metrics.matthews_corrcoef(Y_test, Y_predicted))

pp.pprint(grid_search.best_params_)

print("Accuracy")
pp.pprint(metrics.accuracy_score(Y_test, Y_predicted))

###############################################################

from sklearn import linear_model

data_folder_training_set1 = "./Training"
data_folder_test_set1     = "./Test"

training_dataset1 = load_files(data_folder_training_set1)
test_dataset1 = load_files(data_folder_test_set1)

print(training_dataset1.target_names)

X_train1, X_test_DUMMY_to_ignore1, Y_train1, Y_test_DUMMY_to_ignore1 = train_test_split(training_dataset1.data,
													training_dataset1.target,
													test_size=0.0)
target_names1 = training_dataset1.target_names

X_train_DUMMY_to_ignore1, X_test1, Y_train_DUMMY_to_ignore1, Y_test1 = train_test_split(test_dataset1.data,
													test_dataset1.target,
													train_size=0.0)
target_names1 = training_dataset1.target_names
print(Y_train1.shape)
print(Y_test1.shape)
print(target_names1)

vectorizer1 = TfidfVectorizer(strip_accents= None,
							preprocessor = None,
							)
lmC = linear_model.SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,
        eta0=0.0, fit_intercept=True, l1_ratio=0.15,
        learning_rate='optimal', loss='hinge', n_iter=5, n_jobs=2,
        power_t=0.5, random_state=None, shuffle=True,)

pipeline1 = Pipeline([
	('vect', vectorizer1),
	('lmC', lmC),
	])

parameters1 = {
	'vect__tokenizer': [None, stemming_tokenizer],
	'vect__ngram_range': [(1, 1), (1, 2),],
   'lmC__loss':['hinge','log','squared_loss'],
   'lmC__penalty':['l2','l1','elasticnet']
    }

grid_search1 = GridSearchCV(pipeline1,
						   parameters1,
						   scoring=metrics.make_scorer(metrics.matthews_corrcoef),
						   cv=10,
						   n_jobs=2,
						   verbose=10)

grid_search1.fit(X_train1, Y_train1)

Y_predicted1 = grid_search1.predict(X_test1)

output_classification_report1 = metrics.classification_report(
									Y_test1,
									Y_predicted1,
									target_names=target_names1)
print(output_classification_report1)

confusion_matrix1 = metrics.confusion_matrix(Y_test1, Y_predicted1)
print("Confusion Matrix: True-Classes X Predicted-Classes")
print(confusion_matrix1)

print("Matthews Corr Coef")
pp.pprint(metrics.matthews_corrcoef(Y_test1, Y_predicted1))

pp.pprint(grid_search1.best_params_)

print("Accuracy")
pp.pprint(metrics.accuracy_score(Y_test1, Y_predicted1))

####################################################################
from sklearn.svm import SVC

data_folder_training_set2 = "./Training"
data_folder_test_set2     = "./Test"

training_dataset2 = load_files(data_folder_training_set2)
test_dataset2 = load_files(data_folder_test_set2)

print(training_dataset2.target_names)

X_train2, X_test_DUMMY_to_ignore2, Y_train2, Y_test_DUMMY_to_ignore2 = train_test_split(training_dataset2.data,
													training_dataset2.target,
													test_size=0.0)
target_names2 = training_dataset2.target_names

X_train_DUMMY_to_ignore2, X_test2, Y_train_DUMMY_to_ignore2, Y_test2 = train_test_split(test_dataset2.data,
													test_dataset2.target,
													train_size=0.0)
target_names2 = training_dataset2.target_names
print(Y_train2.shape)
print(Y_test2.shape)
print(target_names2)



vectorizer2 = TfidfVectorizer(strip_accents= None,
							preprocessor = None,
							)
svcC = SVC()
pipeline2 = Pipeline([
	('vect', vectorizer2),
	('svcC', svcC),
	])

parameters2 = {
	'vect__tokenizer': [None, stemming_tokenizer],
	'vect__ngram_range': [(1, 1), (1, 2),],
	'svcC__C':[0.5,1,2],
   	'svcC__gamma':[1,2],
     'svcC__kernel':['rbf','linear'],
   }

grid_search2 = GridSearchCV(pipeline2,
						   parameters2,
						   scoring=metrics.make_scorer(metrics.matthews_corrcoef),
						   cv=10,
						   n_jobs=2,
						   verbose=10)

grid_search2.fit(X_train2, Y_train2)


Y_predicted2 = grid_search2.predict(X_test2)

output_classification_report2 = metrics.classification_report(
									Y_test2,
									Y_predicted2,
									target_names=target_names2)
print(output_classification_report2)

confusion_matrix2 = metrics.confusion_matrix(Y_test2, Y_predicted2)
print("Confusion Matrix: True-Classes X Predicted-Classes")
print(confusion_matrix2)

print("Matthews Corr Coef")
pp.pprint(metrics.matthews_corrcoef(Y_test2, Y_predicted2))

print("Accuracy")
pp.pprint(metrics.accuracy_score(Y_test2, Y_predicted2))

print("Best Parameters:")
pp.pprint(grid_search2.best_params_)
