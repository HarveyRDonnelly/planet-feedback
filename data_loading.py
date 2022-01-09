"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Data Loading Module
Source Path: data_loading.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""

import json
import csv
import random
import config


def load_data() -> (list, list):
    """
    Loads raw data from datasets into Python object.
    """
    f = open('data/results.json')
    data = json.load(f)
    # Closing file
    f.close()
    training = ([], [])
    with open('data/training.csv') as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # Skip the dataset's header.
        for line in reader:
            training[0].append(line[0])
            training[1].append(line[1])
    return (data, training)


def create_random_test() -> list:
    """
    Retrieves random test data classification model.
    """
    f = open('data/test_data.csv', "w+")
    f.close()
    data = load_data()[0]
    return_data = []
    random.shuffle(data)
    for i in range(100):
        return_data.append(data[i]['CompleteReview'])
    return return_data


def create_employers_training() -> None:
    """
    Initialises employer_train.csv and employer_test.csv
    """
    data = load_data()[0]
    random.shuffle(data)
    i = 0
    for i in range(len(data) - 100):
        _, content, name = get_vars(data, i)
        comp_id = config.employer_index[name]
        config.employer_train[0].append(content)
        config.employer_train[1].append(comp_id)

    for j in range(i, len(data)):
        _, content, name = get_vars(data, j)
        comp_id = config.employer_index[name]
        config.employer_test[0].append(content)
        config.employer_test[1].append(comp_id)


def get_vars(data: list, index: int) -> (dict, str, str):
    """
    Return necessary variables for employer testing.
    """
    name = data[index]['URL'].replace('https://in.indeed.com/cmp/', '')
    ind = name.index('/')
    name = name[:ind]
    return (data[index], data[index]['CompleteReview'], name)


def create_employed_training() -> None:
    """
    Initializes data for employed or not training data
    """
    data = load_data()[0]
    random.shuffle(data)
    i = 0
    for i in range(len(data) - 100):
        content = data[i]['CompleteReview']
        review_details = data[i]['ReviewDetails']
        employed = 1
        if 'Current Employee' in review_details:
            employed = 0
        config.employed_train[0].append(content)
        config.employed_train[1].append(employed)

    for j in range(i, len(data)):
        content = data[j]['CompleteReview']
        review_details = data[j]['ReviewDetails']
        employed = 1
        if 'Current Employee' in review_details:
            employed = 0
        config.employed_test[0].append(content)
        config.employed_test[1].append(employed)

