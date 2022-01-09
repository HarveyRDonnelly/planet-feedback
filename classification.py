"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Classification Module
Source Path: classification.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

import data_loading
import config


def initialize() -> None:
    """
    Initialise model variables.
    """
    global training_data, test_data
    training_data = data_loading.load_data()[1]
    test_data = data_loading.create_random_test()
    data_loading.create_employers_training()
    data_loading.create_random_test()


def train_categories(train_data) -> object:
    """
    Trains model using textual data.
    """
    training_counts = config.c_vector.fit_transform(train_data[0])

    # Term frequency and term frequency times inverse document frequency transformations

    training_tfidf = config.tfidf_transformer.fit_transform(training_counts)
    # creating a classifier
    # clf = MultinomialNB().fit(training_tfidf, train_data[1])
    clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
    clf.fit(training_tfidf, train_data[1]) # return this an prev
    return clf


def predict_categories() -> None:
    """
    Predicts subject categories for all data (debug).
    """
    classifier = train_categories(training_data)
    test_counts = config.c_vector.transform(test_data)

    # Term frequency and term frequency times inverse document frequency transformations
    transformed_test = config.tfidf_transformer.transform(test_counts)
    predicted = classifier.predict(transformed_test)

    for review, category in zip(test_data, predicted):
        print(review)
        print(category)


def predict_subject_category(feedback_entry: str, classifier: object) -> str:
    """
    Predicts the subject category for a text.
    """
    training_counts = config.c_vector.transform([feedback_entry])

    # Term frequency and term frequency times inverse document frequency transformations
    transformed_test = config.tfidf_transformer.transform(training_counts)
    predicted = classifier.predict(transformed_test)
    return config.review_type[int(predicted[0])]


def predict_employer() -> None:
    """
    Predicts an employer when provided with a review (for fun).
    """
    data_loading.create_employers_training()
    config.c_vector = CountVectorizer()
    classifier = train_categories(config.employer_train)
    test_counts = config.c_vector.transform(config.employer_test[0])

    # Term frequency and term frequency times inverse document frequency transformations
    transformed_test = config.tfidf_transformer.transform(test_counts)
    predicted = classifier.predict(transformed_test)
    total = 0
    for predicted_company, actual_company in zip(predicted, config.employer_test[1]):
        print('~~~~~~')
        print(config.employer_index_inverse[predicted_company])
        print(config.employer_index_inverse[actual_company])
        print('~~~~~~')
        if predicted_company == actual_company:
            total += 1
    print('Accuracy: ' + str(total / len(config.employer_test[1])))
