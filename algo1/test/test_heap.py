import unittest

from src.heap import heap_sort, Median, Heap


class TestHeap(unittest.TestCase):

    def test_heap_sort(self):
        a = [5,2,7,8,4,3,1,9,6]
        expected = [1,2,3,4,5,6,7,8,9]
        actual = heap_sort(a)
        self.assertEqual(actual, expected, 'should have sorted the array')

    def test_median_maintenance(self):
        m = Median()

        median = m.add(1)
        self.assertEqual(median, 1, 'fist elem')

        median = m.add(5)
        self.assertEqual(median, 5, 'fist elem')

        median = m.add(3)
        self.assertEqual(median, 3, 'fist elem')

        median = m.add(100)
        self.assertEqual(median, 5, 'fist elem')

    # HEAP IMPLEMENTATION

    def test_static_is_heap(self):
        """ Tests static method is_heap if it can correctly verify if a
        list of elements preserves the heap property.
        """
        good = [4, 4, 8, 9, 4, 12, 9, 11, 13]
        bad = [1,2,3,114,5,6,7,8,9,10]

        self.assertTrue(Heap.is_heap(good), 'should hold the heap property')
        self.assertFalse(Heap.is_heap(bad), 'should not hold the heap property')

    def test_insert(self):
        """ Test that adding an element preserves the heap property.
        Given the following heap:
                        (4)
                       /   \
                    (4)    (8)
                   /  \    /  \
                 (9) (4) (12) (9)
                /  \
             (11)  (13)
        """
        data = [4, 4, 8, 9, 4, 12, 9, 11, 13]
        h = Heap(data)

        h.insert(7)
        self.assertTrue(Heap.is_heap(h.data), 'should still be a heap')

        h.insert(10)
        self.assertTrue(Heap.is_heap(h.data), 'should still be a heap')

        h.insert(5)
        self.assertTrue(Heap.is_heap(h.data), 'should still be a heap')

    def test_extract_min(self):
        """ Makes sure that the heap produces min values and that
        the heap property is preserved.
        Given the following heap:
                        (4)
                       /   \
                    (4)    (8)
                   /  \    /  \
                 (9) (4) (12) (9)
                /  \
             (11)  (13)
        """
        data = [4, 4, 8, 9, 4, 12, 9, 11, 13]
        h = Heap(data)

        min_key = h.extract_min()
        self.assertEqual(min_key, 4, 'should extract the min value')
        self.assertTrue(Heap.is_heap(data), 'should still hold the heap property')

        min_key = h.extract_min()
        self.assertEqual(min_key, 4, 'should extract the min value')
        self.assertTrue(Heap.is_heap(data), 'should still hold the heap property')

        min_key = h.extract_min()
        self.assertEqual(min_key, 4, 'should extract the min value')
        self.assertTrue(Heap.is_heap(data), 'should still hold the heap property')

    def test_delete(self):
        pass

    def test_static_heapafy(self):
        pass
