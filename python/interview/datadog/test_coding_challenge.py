# -*- coding: utf-8 -*-

import unittest

from coding_challenge import find_related_tags

stream1 = [
     'system.load.1|1|host:a,role:web,region:us-east-1a',
     'system.load.15|1|host:b,role:web,region:us-east-1b',
     'system.cpu.user|20|host:a,role:web,region:us-east-1a',
     'postgresql.locks|12|host:c,role:db,db_role:master,region:us-east-1e',
     'postgresql.db.count|2|host:d,role:db,db_role:replica,region:us-east-1a',
     'kafka.consumer.lag|20000|host:e,role:intake,region:us-east-1a',
     'kafka.consumer.offset|3000000|host:e,role:intake,region:us-east-1a',
     'kafka.broker.offset|25000|host:f,role:kafka,region:us-east-1a'
]

stream2 = [
    "cpu.load|0.5|role:web,env:stag,region:us",
    "cpu.load|0.6|role:app,env:prod,region:us",
    "cpu.load|0.7|role:web,env:prod,region:eu",
]


class TestCodingChallenge(unittest.TestCase):
    def test_find_related_tags(self):
        tests = [
            (stream2, ["role:web", "env:prod"], ["region:eu"]),
            (stream1, ["role:web"], ["host:a", "region:us-east-1a", "host:b", "region:us-east-1b"]),
            (stream1, ["role:db", "db_role:master"], ["host:c", "region:us-east-1e"]),
            (stream1, ["host:a", "role:web"], ["region:us-east-1a"]),
            (stream2, ["role:web", "region:us"], ["env:stag"]),
            (stream2, ["role:web", "env:stag", "region:us"], []),
        ]
        for test in tests:
            actual = find_related_tags(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))
