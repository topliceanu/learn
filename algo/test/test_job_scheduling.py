import unittest

from src.job_scheduling import schedule


class TestJobScheduling(unittest.TestCase):

    def test_schedule(self):
        jobs = [(1, 3, 5), (2, 1, 2)]
        actual = schedule(jobs)
        expected = [1, 2]
        self.assertEqual(actual, expected,
                'should have correctly scheduled the two jobs')
