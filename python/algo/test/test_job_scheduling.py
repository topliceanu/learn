import unittest

from src.job_scheduling import schedule


class TestJobScheduling(unittest.TestCase):

    def test_schedule(self):
        jobs = [[1, 3, 5], [2, 1, 2]]
        actual = schedule(jobs)
        expected = {
            'sorted_jobs': [
                [1, 3, 5, 0.6, 5],
                [2, 1, 2, 0.5, 7]
            ],
            'sum_completion_time': 22
        }
        self.assertEqual(actual, expected,
            'should return the correct data structure')
