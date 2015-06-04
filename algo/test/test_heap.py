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
        self.assertEqual(median, 1, 'fist elem')

        median = m.add(3)
        self.assertEqual(median, 3, 'fist elem')

        median = m.add(100)
        self.assertEqual(median, 3, 'fist elem')

    def test_median_maintenance_for_longer_lists(self):
        m = Median()
        numbers = [4,3,1,5,1,3,34,6,2,7,8,2,45,7,2,4,7,23,
                   4,73,8,323,45,7,3,2,3,6,3,5,3,62,3,46,9]
        for number in numbers:
            median = m.add(number)

        numbers.sort()
        expected = numbers[len(numbers)/2]
        self.assertEqual(median, expected,
            'should return the element corresponding to the n/2 order statistic')

    # HEAP IMPLEMENTATION

    def test_static_is_heap(self):
        """ Tests static method is_heap if it can correctly verify if a
        list of elements preserves the heap property.
        """
        good = [4, 4, 8, 9, 4, 12, 9, 11, 13]
        bad = [1,2,3,114,5,6,7,8,9,10]

        self.assertTrue(Heap.is_heap(good), 'should hold the heap property')
        self.assertFalse(Heap.is_heap(bad), 'should not hold the heap property')

    def test_heap_length(self):
        data = [1,2,3,114,5,6,7,8,9,10]
        h = Heap.heapify(data)
        self.assertEqual(len(h), len(data), 'should be the same length')

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

    def test_extract_min_and_insert(self):
        """ Test if extracting min and adding a new value at the same time works.
        Given the following heap:
                        (4)
                       /   \
                    (5)    (8)
                   /  \    /  \
                 (9) (6) (12) (9)
                /  \
             (11)  (13)
        """
        data = [4, 5, 8, 9, 6, 12, 9, 11, 13]
        h = Heap(data)

        min_value = h.extract_min_and_insert(2)
        self.assertEqual(min_value, 4, 'should return the min value')
        expected = [2, 5, 8, 9, 6, 12, 9, 11, 13]
        self.assertEqual(h.data, expected, 'should remove the old min and '+
                                           'add new value correctly')

    def test_remove(self):
        """ Test the removal of a key from the middle of the heap.
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
        h.remove(3)
        self.assertTrue(Heap.is_heap(data), 'should preserve heap property')

    def test_remove_if_index_is_root(self):
        data = [3, 4, 5]
        h = Heap(data)
        h.remove(0)
        self.assertEqual(h.data, [4,5], 'should remove the root')
        self.assertTrue(Heap.is_heap(h.data), 'should maintain heap invariant')

    def test_remove_if_index_is_last(self):
        data = [3, 4, 5]
        h = Heap(data)
        h.remove(2)
        self.assertEqual(h.data, [3, 4], 'should remove the last leaf')
        self.assertTrue(Heap.is_heap(h.data), 'should maintain heap invariant')

    def test_remove_if_one_element(self):
        data = [3]
        h = Heap(data)
        h.remove(0)
        self.assertEqual(h.data, [], 'should remove the only elem in heap')
        self.assertTrue(Heap.is_heap(h.data), 'should maintain heap invariant')

    def test_static_heapify(self):
        data = [8,2,6,3,1,2,9,5,3,7,4]
        h = Heap.heapify(data)
        self.assertTrue(Heap.is_heap(data), 'should preserve heap property')

    def test_bubble_up(self):
        h = Heap([])
        h.data = [3, 4, 2]
        new_index = h.bubble_up(2)
        self.assertTrue(Heap.is_heap(h.data), 'should maintain the heap prop')
        self.assertEqual(h.data, [2,4,3], 'should have reorganized the heap')
        self.assertEqual(new_index, 0, 'should return the correct new index')

    def test_bubble_down(self):
        h = Heap([])
        h.data = [3, 2, 4]
        new_index = h.bubble_down(0)
        self.assertTrue(Heap.is_heap(h.data), 'should maintain the heap prop')
        self.assertEqual(h.data, [2,3,4], 'should have reorganized the heap')
        self.assertEqual(new_index, 1, 'should return the correct new index')

    def test_get_min(self):
        h = Heap(range(10))

        min_index = h.get_min(2, 4, 6)
        self.assertEqual(min_index, 2, 'should return the index with the min key')

        min_index = h.get_min(6, 4, 2)
        self.assertEqual(min_index, 2, 'should return the index with the min key')

        min_index = h.get_min(4, 2, 6)
        self.assertEqual(min_index, 2, 'should return the index with the min key')

        min_index = h.get_min(4, 2, 100)
        self.assertEqual(min_index, 2, 'should work for unknown indexes')
