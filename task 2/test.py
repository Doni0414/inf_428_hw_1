import unittest
import numpy as np
from threat_score_calculator import calculate_threat_score

ENGINEERING = "Engineering"
MARKETING = "Marketing"
FINANCE = "Finance"
HR = "HR"
SCIENCE = "Science"

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def generate_department_data(name, mean, variance, num_samples, importance):
    return {
        "name": name,
        "threat_scores": generate_random_data(mean=mean, variance=variance, num_samples=num_samples),
        "importance": importance
    }


class TestThreatScore(unittest.TestCase):

# Case 1:
# - each department has no outliers (no really high threat scores)
# - each department mean threat score are NOT far from each other
# - similiar number of users.
# - all departments has the same importance
    def test_case1(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=10, variance=5, num_samples=100, importance=3),
            generate_department_data(name=MARKETING, mean=9, variance=5, num_samples=90, importance=3),
            generate_department_data(name=FINANCE, mean=12, variance=5, num_samples=95, importance=3),
            generate_department_data(name=HR, mean=13, variance=5, num_samples=92, importance=3),
            generate_department_data(name=SCIENCE, mean=10, variance=5, num_samples=93, importance=3),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)

# Case 2:
# - each department has high threat scores
# - each department mean threat score are same
# - each department has same variance threat score
# - each department has same number of users
# - each department has same and high importance
    def test_case2(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=80, variance=10, num_samples=80, importance=5),
            generate_department_data(name=MARKETING, mean=80, variance=10, num_samples=80, importance=5),
            generate_department_data(name=FINANCE, mean=80, variance=10, num_samples=80, importance=5),
            generate_department_data(name=HR, mean=80, variance=10, num_samples=80, importance=5),
            generate_department_data(name=SCIENCE, mean=80, variance=10, num_samples=80, importance=5),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)

# Case 3:
# - each department has 89 threat scores (mean = 89, variance = 0)
# - each department has same number of users
# - each department has same and high importance
    def test_case3(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=89, variance=0, num_samples=100, importance=5),
            generate_department_data(name=MARKETING, mean=89, variance=0, num_samples=100, importance=5),
            generate_department_data(name=FINANCE, mean=89, variance=0, num_samples=100, importance=5),
            generate_department_data(name=HR, mean=89, variance=0, num_samples=100, importance=5),
            generate_department_data(name=SCIENCE, mean=89, variance=0, num_samples=100, importance=5),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)
    
# Case 4:
# - each department has 90 threat scores (mean = 89, variance = 0)
# - each department has same number of users
# - each department has same and low importance
    def test_case4(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=89, variance=0, num_samples=100, importance=1),
            generate_department_data(name=MARKETING, mean=89, variance=0, num_samples=100, importance=1),
            generate_department_data(name=FINANCE, mean=89, variance=0, num_samples=100, importance=1),
            generate_department_data(name=HR, mean=89, variance=0, num_samples=100, importance=1),
            generate_department_data(name=SCIENCE, mean=89, variance=0, num_samples=100, importance=1),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)
    
# Case 5:
# - all departments has 89 threat scores (mean = 89, variance = 0)
# - departments has different random user numbers
# - departments has same high importance = 5
    def test_case5(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=89, variance=0, num_samples=100, importance=5),
            generate_department_data(name=MARKETING, mean=89, variance=0, num_samples=76, importance=5),
            generate_department_data(name=FINANCE, mean=89, variance=0, num_samples=23, importance=5),
            generate_department_data(name=HR, mean=89, variance=0, num_samples=5, importance=5),
            generate_department_data(name=SCIENCE, mean=89, variance=0, num_samples=33, importance=5),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)

# Case 6:
# - all departments has low threat scores
# - all departments has approximately same mean threat score (mean is same, but variance varies not so far)
# - similar high user numbers
# - same high importance
    def test_case6(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=25, variance=10, num_samples=88, importance=4),
            generate_department_data(name=MARKETING, mean=25, variance=9, num_samples=80, importance=4),
            generate_department_data(name=FINANCE, mean=25, variance=4, num_samples=95, importance=4),
            generate_department_data(name=HR, mean=25, variance=12, num_samples=100, importance=4),
            generate_department_data(name=SCIENCE, mean=25, variance=7, num_samples=83, importance=4),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)
    
# Case 7:
# - all departments has low threat scores
# - all departments has approximately same mean threat score (mean is same, but variance varies not so far)
# - similar high user numbers
# - same low importance = 2
    def test_case7(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=10, variance=5, num_samples=95, importance=2),
            generate_department_data(name=MARKETING, mean=10, variance=3, num_samples=90, importance=2),
            generate_department_data(name=FINANCE, mean=10, variance=7, num_samples=91, importance=2),
            generate_department_data(name=HR, mean=10, variance=2, num_samples=89, importance=2),
            generate_department_data(name=SCIENCE, mean=10, variance=10, num_samples=87, importance=2),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)
    
# Case 8:
# - all departments has low threat scores
# - all departments has approximately same mean threat score (mean is same, but variance varies not so far)
# - different user numbers
# - different importance
    def test_case8(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=15, variance=4, num_samples=99, importance=5),
            generate_department_data(name=MARKETING, mean=15, variance=3, num_samples=32, importance=3),
            generate_department_data(name=FINANCE, mean=15, variance=1, num_samples=51, importance=4),
            generate_department_data(name=HR, mean=15, variance=10, num_samples=16, importance=1),
            generate_department_data(name=SCIENCE, mean=15, variance=5, num_samples=40, importance=2),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)
    
# Case 9:
# - all departments has different threat scores (different mean and variance)
# - different user numbers
# - different importance
    def test_case9(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=34, variance=10, num_samples=100, importance=5),
            generate_department_data(name=MARKETING, mean=67, variance=20, num_samples=56, importance=4),
            generate_department_data(name=FINANCE, mean=80, variance=10, num_samples=30, importance=5),
            generate_department_data(name=HR, mean=10, variance=5, num_samples=24, importance=2),
            generate_department_data(name=SCIENCE, mean=52, variance=25, num_samples=15, importance=1),
        ]

        # when
        actual = calculate_threat_score(departments=departments)

        # then
        self.assertTrue(0 <= actual <= 90)

# Case 10:
# - all departments has 0 threat score (mean = 0, variance = 0)
# - 100 users for all departments
# - same high importance
    def test_case10(self):
        # given
        departments = [
            generate_department_data(name=ENGINEERING, mean=0, variance=0, num_samples=100, importance=5),
            generate_department_data(name=MARKETING, mean=0, variance=0, num_samples=100, importance=5),
            generate_department_data(name=FINANCE, mean=0, variance=0, num_samples=100, importance=5),
            generate_department_data(name=HR, mean=0, variance=0, num_samples=100, importance=5),
            generate_department_data(name=SCIENCE, mean=0, variance=0, num_samples=100, importance=5),
        ]