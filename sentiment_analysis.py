"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Sentiment Analysis Module
Source Path: sentiment_analysis.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def generate_sentiment_score(text: str) -> float:
    """
    Return the adjusted sentiment score for a given text using the VADER sentiment model.
    """

    sentiment_analyser = SentimentIntensityAnalyzer()
    sentiment_dictionary = sentiment_analyser.polarity_scores(text)
    return float(sentiment_dictionary['compound']) * 5
