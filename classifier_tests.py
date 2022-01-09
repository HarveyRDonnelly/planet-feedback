"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Testing Module
Source Path: classifier_testing.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""
import pytest

import classification
import classification as clf
import data_loading


class TestPay:
    """A collection of unit tests for feedback about salaries"""

    def test_pay_simple(self) -> None:
        """Test for obvious reviews about pay"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'I worked here at google for about 5 years now, and the most notable thing about ' \
                 'my time was the increasing wages. Any time I was set for a raise, my boss would' \
                 'always up my pay.'
        expected = 'pay'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_pay_complex(self) -> None:
        """Test for harder reviews about pay"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'although my friends were fun to work with at this job, the actual worst part was ' \
                 'the terrible wages.'
        expected = 'pay'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestEquality:
    """A collection of unit tests for feedback about equality"""

    def test_equality_simple(self) -> None:
        """Test for obvious reviews about equality"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'I found that during my time here at amazon, the condition were unfair, and ' \
                 'inequal towards people like me.'
        expected = 'equality'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_equality_complex(self) -> None:
        """Test for harder reviews about equality"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'Although it was a redeemable work invironment, the worst problem i ' \
                 'had with this job was the fact that everyone was treated unjustly and without' \
                 'dignity'
        expected = 'equality'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestWorkload:
    """A collection of unit tests for feedback about workload"""

    def test_workload_simple(self) -> None:
        """Test for obvious reviews about workload"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'I was working very long hours here this bank, but honeslty i really liked that part of the job.' \
                 'Sometimes the workload was a bit overwhelming however.'
        expected = 'workload'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_workload_complex(self) -> None:
        """Test for harder reviews about workload"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'Great place to work, the team is always keeping you distracted from the immense amount of task you ' \
                 'have to do every day. Often worked overtime'
        expected = 'workload'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestWorkEnvironment:
    """A collection of unit tests for feedback about work environments"""

    def test_workenv_simple(self) -> None:
        """Test for obvious reviews about work environments"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'Great place to work, the campus was very beautiful, I loved coming into the office everyday. ' \
                 'Great overall vibes.'
        expected = 'work environment'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_workenv_complex(self) -> None:
        """Test for harder reviews about work environments"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'At my time here at Rakuten I found that aside from rather long shifts, the job was quite fun. This ' \
                 'was mainly due to awesome work spaces we were provided that felt very comfortable to work in'
        expected = 'work environment'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestEmployees:
    """A collection of unit tests for feedback about employees"""

    def test_employees_simple(self) -> None:
        """Test for obvious reviews about employees"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'The best of this job was definitely meeting all the new people. Every day I got' \
                 'to hang out with my awesome coworkers and work on an amazing product.'
        expected = 'employees'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_employees_complex(self) -> None:
        """Test for harder reviews about employees"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'I enjoyed my stay here at Jordans Cottages, not only becuase of great work environment,' \
                 'but mainly due to the awesome team I got to work with. Everyone around me was a blast to have around'
        expected = 'employees'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestJobRequirements:
    """A collection of unit tests for feedback about job requirements"""

    def test_job_requirements_simple(self) -> None:
        """Test for obvious reviews about job requirements"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'The best part about my job was definetely working on the project that I got to work on. I enjoyed ' \
                 'learning all the new skills and techniques that are needed to excel in this field.'
        expected = 'job requirements'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_job_requirements_complex(self) -> None:
        """Test for harder reviews about job requirements"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'Although I loved hanging out with people at my work, I honestly really enjoyed the actual task I ' \
                 'was completing for my job. I learned many newq things along the way '
        expected = 'job requirements'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual


class TestManagement:
    """A collection of unit tests for feedback about management"""

    def test_job_requirements_simple(self) -> None:
        """Test for obvious reviews about management"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'I loved my boss and all of my managers'
        expected = 'management'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual

    def test_job_requirements_complex(self) -> None:
        """Test for harder reviews about management"""
        classifier = classification.train_categories(data_loading.load_data()[1])
        review = 'my boss and managers were definetely the highlight of my stay at amazon, but ' \
                 'the work env was pretty good as well '
        expected = 'management'
        actual = classification.predict_subject_category(review, classifier)
        assert expected == actual
