import os
import unittest

import numpy as np
import pandas as pd

from threat_score_calculator import calculate_threat_score

ENGINEERING = "Engineering"
MARKETING = "Marketing"
FINANCE = "Finance"
HR = "HR"
SCIENCE = "Science"

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def generate_or_load_data(params, file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        all_data = []
        for dept_id, (mean, variance, num_samples) in enumerate(params, start=1):
            data = generate_random_data(mean, variance, num_samples)
            all_data.append(pd.DataFrame({
                "Department": [dept_id] * len(data),
                "ThreatScore": data
            }))
        result = pd.concat(all_data, ignore_index=True)
        result.to_csv(file_path, index=False)
        return result

def convert_threat_score_df_to_array(df):
    grouped = df.groupby('Department')["ThreatScore"].apply(list)
    return grouped.tolist()

class TestThreatScore(unittest.TestCase):

    def test_case1(self):
        """
        Case 1:
        All departments has quite same high scores.
        Expect that calculated threat score will be too high(within [78, 86])
        """
        # given
        params = [(80, 5, 100), (82, 5, 100), (87, 5, 100), (85, 4, 100), (88, 4, 100)]
        file_path = 'test_case_1.csv'

        df = generate_or_load_data(params, file_path)
        data = convert_threat_score_df_to_array(df)

        # when
        actual = calculate_threat_score(data=data)

        # then
        self.assertTrue(78 <= actual <= 90)

    def test_case2(self):
        """
        Case 2:
        One department has high mean threat score, other low
        Expect high threat score
        """
        # given
        params = [(80, 4, 100), (30, 4, 100), (23, 3, 100), (10, 5, 100), (15, 3, 100)]
        file_path = 'test_case_2.csv'

        df = generate_or_load_data(params, file_path)
        data = convert_threat_score_df_to_array(df)

        # when
        actual = calculate_threat_score(data)

        # then
        self.assertTrue(75 <= actual <= 85)

    def test_case3(self):
        """
        All departments have the same mean threat scores, but in one department there are really high threat score users.
        Expect high threat score
        """

        # given
        params = [(80, 40, 100), (25, 3, 100), (30, 10, 100), (20, 4, 100), (15, 2, 100)]
        file_path = 'test_case_3.csv'

        df = generate_or_load_data(params, file_path)
        data = convert_threat_score_df_to_array(df)

        # when
        actual = calculate_threat_score(data)

        # then
        self.assertTrue(65 <= actual <= 85)

    def test_case4(self):
        """
        Case 4:
        All departments has a different number of users and quite high mean threat scores
        Expect high threat score
        """

        # given
        params = [(80, 4, 50), (74, 3, 10), (69, 2, 100), (85, 4, 83), (78, 2, 5)]
        file_path = 'test_case_4.csv'

        df = generate_or_load_data(params, file_path)
        data = convert_threat_score_df_to_array(df)

        # when
        actual = calculate_threat_score(data)

        # then
        self.assertTrue(70 <= actual <= 85)
