import unittest

from src.bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_constructor(self):
        bf = BloomFilter(10, 3)

        self.assertEqual(len(bf.hash_fns), 3,
                'has generated the instructed num of hash functions')
        self.assertEqual(len(bf.bits), 10,
                'prepares an array of bits of instructed size')

    def test_insert(self):
        bf = BloomFilter(10, 3)
        bf.insert(12)

    def test_lookup(self):
        bf = BloomFilter(10, 3)
        bf.insert(12)
        self.assertTrue(bf.lookup(12), 'should detect it was inserted')
