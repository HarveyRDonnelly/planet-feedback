"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Run Project Module
Source Path: run.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""
import uuid
import data_loading
import classification
import entities
import sentiment_analysis
import json

employers = {}
data, train = data_loading.load_data()
classifier = classification.train_categories(train)

for feedback in data:
    content = feedback['CompleteReview']
    edited_URL = feedback['URL'].replace('https://in.indeed.com/cmp/', '')
    ind = edited_URL.index('/')
    name = edited_URL[:ind]

    sentiment = sentiment_analysis.generate_sentiment_score(content)

    category = classification.predict_subject_category(content, classifier)

    if name not in employers:
        employers[name] = entities.Employer(name)
    employers[name].feedback_entries[uuid.uuid4()] = \
        entities.FeedbackEntry(name, content, category, sentiment)

    if category == 'pay':
        employers[name].pay_score[0] += sentiment
        employers[name].pay_score[1] += 1
    elif category == 'equality':
        employers[name].equality_score[0] += sentiment
        employers[name].equality_score[1] += 1
    elif category == 'workload':
        employers[name].workload_score[0] += sentiment
        employers[name].workload_score[1] += 1
    elif category == 'work environment':
        employers[name].work_environment_score[0] += sentiment
        employers[name].work_environment_score[1] += 1
    elif category == 'employees':
        employers[name].employees_score[0] += sentiment
        employers[name].employees_score[1] += 1
    elif category == 'job requirements':
        employers[name].job_requirements_score[0] += sentiment
        employers[name].job_requirements_score[1] += 1
    elif category == 'management':
        employers[name].management_score[0] += sentiment
        employers[name].management_score[1] += 1

for employer in employers:
    employer.find_pf_score()
    employer.find_scores()

employers_json = {}
for employer in employers:
    name = employer.name
    employers_json[name] = employer.to_json()

with open("output.json", "w") as outfile:
    json.dump(employers_json, outfile)
