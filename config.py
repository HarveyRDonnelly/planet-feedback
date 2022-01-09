"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Config Module
Source Path: config.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

review_type = {0: 'pay', 1: 'equality', 2: 'workload', 3: 'work environment',
               4: 'employees', 5: 'job requirements', 6: 'management'}

employer_index_inverse = \
    {0: 'Axis-Bank', 1: 'Kotak-Mahindra-Bank', 2: 'Indeed', 3: 'Tata-Aia-Life', 4: 'Nokia', 5: 'Mphasis',
     6: 'Wells-Fargo',
     7: 'Facebook', 8: 'HP', 9: 'Icici-Prudential-Life-Insurance', 10: 'Ey', 11: 'Bharti-Airtel-Limited',
     12: 'Accenture',
     13: 'Standard-Chartered-Bank', 14: 'Microsoft', 15: 'Infosys', 16: 'Maersk', 17: 'IBM',
     18: 'L&T-Technology-Services-Ltd.', 19: 'Alstom', 20: 'Yes-Bank', 21: 'Apollo-Hospitals', 22: 'Ericsson',
     23: 'Sutherland', 24: 'Deloitte', 25: 'Google', 26: 'Flipkart.com', 27: 'Mahindra-&-Mahindra-Ltd',
     28: 'Reliance-Industries-Ltd', 29: 'Muthoot-Finance', 30: 'Oracle', 31: 'Ride.swiggy', 32: 'Kpmg',
     33: 'Teleperformance', 34: 'Concentrix', 35: 'JPMo'
                                                  'rgan-Chase', 36: 'Marriott-International,-Inc.', 37: 'DHL',
     38: 'Hinduja-Global-Solutions', 39: 'Tata-Consultancy-Services-(tcs)', 40: 'Wns-Global-Services',
     41: 'Deutsche-Bank',
     42: 'American-Express', 43: "Byju's", 44: 'Jll', 45: 'Jio', 46: 'UnitedHealth-Group', 47: 'Vodafoneziggo',
     48: 'Cognizant-Technology-Solutions', 49: 'Capgemini', 50: 'Amazon.com', 51: 'Hyatt', 52: 'HSBC', 53: 'Bosch',
     54: 'Hdfc-Bank', 55: 'Barclays', 56: 'Honeywell', 57: 'Citi', 58: 'Dell-Technologies'}

employer_index = \
    {'Axis-Bank': 0, 'Kotak-Mahindra-Bank': 1, 'Indeed': 2, 'Tata-Aia-Life': 3, 'Nokia': 4,
     'Mphasis': 5, 'Wells-Fargo': 6,
     'Facebook': 7, 'HP': 8, 'Icici-Prudential-Life-Insurance': 9, 'Ey': 10,
     'Bharti-Airtel-Limited': 11, 'Accenture': 12,
     'Standard-Chartered-Bank': 13, 'Microsoft': 14, 'Infosys': 15, 'Maersk': 16, 'IBM': 17,
     'L&T-Technology-Services-Ltd.': 18, 'Alstom': 19, 'Yes-Bank': 20, 'Apollo-Hospitals': 21,
     'Ericsson': 22,
     'Sutherland': 23, 'Deloitte': 24, 'Google': 25, 'Flipkart.com': 26,
     'Mahindra-&-Mahindra-Ltd': 27,
     'Reliance-Industries-Ltd': 28, 'Muthoot-Finance': 29, 'Oracle': 30, 'Ride.swiggy': 31,
     'Kpmg': 32,
     'Teleperformance': 33, 'Concentrix': 34, 'JPMorgan-Chase': 35,
     'Marriott-International,-Inc.': 36, 'DHL': 37,
     'Hinduja-Global-Solutions': 38, 'Tata-Consultancy-Services-(tcs)': 39,
     'Wns-Global-Services': 40, 'Deutsche-Bank': 41,
     'American-Express': 42, "Byju's": 43, 'Jll': 44, 'Jio': 45, 'UnitedHealth-Group': 46,
     'Vodafoneziggo': 47,
     'Cognizant-Technology-Solutions': 48, 'Capgemini': 49, 'Amazon.com': 50, 'Hyatt': 51,
     'HSBC': 52, 'Bosch': 53,
     'Hdfc-Bank': 54, 'Barclays': 55, 'Honeywell': 56, 'Citi': 57, 'Dell-Technologies': 58}

employed_index = {'Current Employee': 0, 'Former Employee': 1}
employed_index_inverse = {0: 'Current Employee', 1: 'Former Employee'}

employer_test = ([], [])
employer_train = ([], [])
employed_test = ([], [])
employed_train = ([], [])
c_vector = CountVectorizer()
tfidf_transformer = TfidfTransformer()
