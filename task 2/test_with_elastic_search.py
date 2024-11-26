import unittest

from elasticsearch import Elasticsearch

from threat_score_calculator import calculate_threat_score

ENGINEERING = "Engineering"
MARKETING = "Marketing"
FINANCE = "Finance"
HR = "HR"
SCIENCE = "Science"

es = Elasticsearch('http://localhost:9200')


def get_threat_scores_from_elasticsearch(index_name):
    query = {
        "query": {
            "match_all": {}
        }
    }

    response = es.search(index=index_name, body=query)

    hits = response['hits']['hits']

    # Extract Department and ThreatScore from each document
    all_data = []
    for hit in hits:
        threat_scores = [[] for i in range(5)]
        departments = hit["_source"]["Department"]
        threat_scores_list = hit["_source"]["ThreatScore"]
        for i in range(len(departments)):
            department_id = departments[i]
            threat_scores[department_id - 1].append(threat_scores_list[i])
        all_data.append(threat_scores)
    return all_data


class TestThreatScore(unittest.TestCase):

    def setUp(self):
        self.all_data = get_threat_scores_from_elasticsearch('threat_scores')

    def test_case1(self):
        """
        Case 1:
        All departments has quite same high scores.
        Expect that calculated threat score will be too high(within [78, 86])
        """
        # given
        data = self.all_data[0]

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
        data = self.all_data[1]

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
        data = self.all_data[2]

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
        data = self.all_data[3]

        # when
        actual = calculate_threat_score(data)

        # then
        self.assertTrue(70 <= actual <= 85)
