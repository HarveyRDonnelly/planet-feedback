"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Entities Module
Source Path: entities.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""
from __future__ import annotations

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

    def __init__(self, employer: Employer, text: str, subject_category: str) -> None:
        self.id = uuid.uuid4()
        self.employer = employer
        self.text = text
        self.subject_category = subject_category
        self.sentiment_score = sentiment_analysis.generate_sentiment_score(self.text)

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
    feedback_entries: dict[int, FeedbackEntry]
    pf_score: float
    pay_score: float
    equality_score: float
    workload_score: float
    work_environment_score: float
    employees_score: float
    job_requirements_score: float
    management_score: float


class Employee:
    """
    This class represents an employee.
    """
    id: uuid.UUID
    name: str
    employer: Employer
