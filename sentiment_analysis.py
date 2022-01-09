"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Sentiment Analysis Module
Source Path: sentiment_analysis.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import data_loading


def generate_sentiment_score(text: str) -> float:
    """
    Return the adjusted sentiment score for a given text using the VADER sentiment model.
    """

    sentiment_analyser = SentimentIntensityAnalyzer()
    sentiment_dictionary = sentiment_analyser.polarity_scores(text)
    return float(sentiment_dictionary['compound']) * 5


def rating_reliability_analysis() -> None:
    """
    Carries out an analysis for the reliability of user-inputted star ratings compared to the
    sentiment analysis scores.
    """
    data, _ = data_loading.load_data()
    total_matches = 0
    total_error = 0
    total_weighted = 0
    for feedback_entry in data:
        print('~~~')
        raw_rating = float(feedback_entry['Rating'])
        vader_score = generate_sentiment_score(feedback_entry['CompleteReview'])
        vader_rating = (vader_score + 1.0) * 2.5

        if round(raw_rating) == round(vader_rating):
            total_matches += 1

            print('> 5-Point Accurate: True')
        else:
            print('> 5-Point Accurate: False')
        total_error += (abs(raw_rating - round(vader_rating)) ** 2)
        total_weighted = 1 / (abs(raw_rating - round(vader_rating)) + 1)
        print('> Vader Score: ' + str(vader_score))
        print('> Vader Rating: ' + str(vader_rating))
        print('> Raw Rating: ' + str(raw_rating))
        print('> 5-Point Accuracy (so far): ' + str((total_matches / len(data)) * 100) + '%')

    print('~~~')
    print('Accuracy (total): ' + str((total_matches / len(data)) * 100) + '%')
    print('~~~')
    print('Accuracy (total error): ' + str((1 - (total_error / len(data))) * 100))
    print('Accuracy (total wighted): ' + str(total_weighted / len(data)) * 100)
