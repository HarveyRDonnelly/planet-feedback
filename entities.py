"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Entities Module
Source Path: entities.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""
from __future__ import annotations
import json
import uuid
from typing import Optional
import classification
import sentiment_analysis


class FeedbackEntry:
    """
    This class represents a feedback entry submitted by an employee regarding their employer.

    Instance Attributes:
     - id: the id of the feedback entry.
     - employer: the employer entity of which the feedback entry relates to.
     - text: a string representing the raw text of the feedback.
     - author: the optional attribute for an employee to be assigned to a feedback entry.
     - rating: the optional attribute to represent the user-inputted rating associated with their
     feedback entry (note that this does not impact sentiment score).
     - subject_category: the dominant subject category associated with this feedback entry's
     sentiment score.

     Representation Invariants:
      - -5 <= self.sentiment_score <= 5
      - subject_category in {'PAY', 'EQUALITY', 'WORKLOAD', 'WORK_ENVIRONMENT', 'EMPLOYEES',\
      'JOB_REQUIREMENTS', 'MANAGEMENT'}

    """
    id: uuid.UUID
    employer: Employer
    text: str
    author: Optional[Employee] = None
    rating: Optional[float] = None
    sentiment_score: float
    subject_category: str

    def __init__(self, employer: Employer, text: str, subject_category: str, sentiment: float) -> None:
        self.id = uuid.uuid4()
        self.employer = employer
        self.text = text
        self.subject_category = subject_category
        self.sentiment_score = sentiment

    def set_subject_category(self, subject_category: str) -> None:
        """
        Sets the feedback entry's subject category using the trained classification model.
        """
        self.subject_category = subject_category

    def set_sentiment_score(self) -> None:
        """
        Sets the feedback entry's sentiment score.
        """
        self.sentiment_score = sentiment_analysis.generate_sentiment_score(self.text)


class Employer:
    """
    This class represents an employer.
    """
    id: uuid.UUID
    name: str
    feedback_entries: dict[uuid.UUID, FeedbackEntry]
    pf_score: float
    pay_score: list[float, float, float]
    equality_score: list[float, float, float]
    workload_score: list[float, float, float]
    work_environment_score: list[float, float, float]
    employees_score: list[float, float, float]
    job_requirements_score: list[float, float, float]
    management_score: list[float, float, float]

    def __init__(self, name) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.feedback_entries = {}
        self.pf_score = 0
        self.pay_score = [0, 0, 0]
        self.equality_score = [0, 0, 0]
        self.workload_score = [0, 0, 0]
        self.work_environment_score = [0, 0, 0]
        self.employees_score = [0, 0, 0]
        self.job_requirements_score = [0, 0, 0]
        self.management_score = [0, 0, 0]

    def find_scores(self) -> None:
        """ finds scores """
        self.pay_score[2] = self.pay_score[0] / self.pay_score[1]
        self.equality_score[2] = self.equality_score[0] / self.equality_score[1]
        self.workload_score[2] = self.workload_score[0] / self.workload_score[1]
        self.work_environment_score[2] = self.work_environment_score[0] / self.work_environment_score[1]
        self.employees_score[2] = self.employees_score[0] / self.employees_score[1]
        self.job_requirements_score[2] = self.job_requirements_score[0] / self.job_requirements_score[1]
        self.management_score[2] = self.management_score[0] / self.management_score[1]

    def find_pf_score(self) -> None:
        """ finds pf score for an employer """
        total = 0
        for id in self.feedback_entries:
            score = self.feedback_entries[id].sentiment_score
            total += score
        self.pf_score = total / len(self.feedback_entries)

    def to_json(self) -> object:
        """ makes objects serializable """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Employee:
    """
    This class represents an employee.
    """
    id: uuid.UUID
    name: str
    employer: Employer
