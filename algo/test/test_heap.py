import unittest

from src.heap import heap_sort, Median, Heap, IndexedHeap


class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        a = [5,2,7,8,4,3,1,9,6]
        expected = [1,2,3,4,5,6,7,8,9]
        actual = heap_sort(a)
        self.assertEqual(actual, expected, 'should have sorted the array')


class TestMedianMaintenance(unittest.TestCase):

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


class TestHeap(unittest.TestCase):

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
        h.remove(2)

        self.assertTrue(Heap.is_heap(data), 'should preserve heap property')
        self.assertNotIn(8, h.data, 'the value corresponding to the index was removed')

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


class TestIndexedHeap(unittest.TestCase):


    def test_insert(self):
        h = IndexedHeap()
        h.insert('x', 100)
        h.insert('y', 200)
        h.insert('z', 300)
        expected = [
            {'key': 'x', 'value': 100, 'index': 0},
            {'key': 'y', 'value': 200, 'index': 1},
            {'key': 'z', 'value': 300, 'index': 2}
        ]
        self.assertItemsEqual(h.data, expected,
            'correctly inserts data into the heap')

    def test_extract_min(self):
        h = IndexedHeap.heapify([('z', 3), ('y', 2), ('x', 1)])
        item = h.extract_min()
        expected = {'key': 'x', 'value': 1}
        self.assertEqual(expected, item, 'correctly extracts the min value')

    def test_remove(self):
        h = IndexedHeap()
        h.data = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 3, 'value': 30, 'index': 1},
            {'key': 4, 'value': 40, 'index': 2}
        ]
        item = h.remove(1)
        expected = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 4, 'value': 40, 'index': 1}
        ]
        self.assertItemsEqual(h.data, expected,
            'correctly removes the data')
        self.assertEqual(item, {'key': 3, 'value': 30},
            'removed item is correct')

    def test_heapify(self):
        h = IndexedHeap.heapify([(3, 'z'), (2, 'y'), (1, 'x')])
        expected = [
            {'key': 1, 'value': 'x', 'index': 0},
            {'key': 2, 'value': 'y', 'index': 1},
            {'key': 3, 'value': 'z', 'index': 2}
        ]
        self.assertItemsEqual(expected, h.data, 'should create a valid heap')

    def test_bubble_up_last(self):
        h = IndexedHeap()
        h.data = [
            {'key': 4, 'value': 40, 'index': 0},
            {'key': 3, 'value': 30, 'index': 1},
            {'key': 2, 'value': 20, 'index': 2},
        ]
        h.bubble_up(2)
        expected = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 3, 'value': 30, 'index': 1},
            {'key': 4, 'value': 40, 'index': 2}
        ]
        self.assertItemsEqual(h.data, expected, 'bubbles up the data correctly')

    def test_bubble_up_root(self):
        h = IndexedHeap()
        h.data = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 3, 'value': 30, 'index': 1},
            {'key': 4, 'value': 40, 'index': 2}
        ]
        h.bubble_up(0)
        expected = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 3, 'value': 30, 'index': 1},
            {'key': 4, 'value': 40, 'index': 2}
        ]
        self.assertItemsEqual(h.data, expected, 'bubbles up the data correctly')

    def test_bubble_down_root(self):
        h = IndexedHeap()
        h.data = [
            {'key': 4, 'value': 40, 'index': 0},
            {'key': 2, 'value': 20, 'index': 1},
            {'key': 3, 'value': 30, 'index': 2}
        ]
        h.bubble_down(0)
        expected = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 4, 'value': 40, 'index': 1},
            {'key': 3, 'value': 30, 'index': 2}
        ]
        self.assertItemsEqual(h.data, expected, 'sorts the data correctly')

    def test_bubble_down_last(self):
        h = IndexedHeap()
        h.data = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 4, 'value': 40, 'index': 1},
            {'key': 3, 'value': 30, 'index': 2},
        ]
        h.bubble_down(2)
        expected = [
            {'key': 2, 'value': 20, 'index': 0},
            {'key': 4, 'value': 40, 'index': 1},
            {'key': 3, 'value': 30, 'index': 2},
        ]
        self.assertItemsEqual(h.data, expected, 'sorts the data correctly')

    def test_get_parent_index(self):
        h = IndexedHeap()
        h.data = range(10)
        self.assertEqual(h.get_parent_index(0), None, 'no parent for root')
        self.assertEqual(h.get_parent_index(1), 0, '0 parent for 1')
        self.assertEqual(h.get_parent_index(2), 0, '0 parent for 2')
        self.assertEqual(h.get_parent_index(3), 1, '1 parent for 3')
        self.assertEqual(h.get_parent_index(4), 1, '1 parent for 4')
        self.assertEqual(h.get_parent_index(5), 2, '2 parent for 5')
        self.assertEqual(h.get_parent_index(6), 2, '2 parent for 6')
        self.assertEqual(h.get_parent_index(7), 3, '3 parent for 7')
        self.assertEqual(h.get_parent_index(8), 3, '3 parent for 8')
        self.assertEqual(h.get_parent_index(9), 4, '4 parent for 9')

    def test_get_child_indices(self):
        h = IndexedHeap()
        h.data = range(10)
        self.assertEqual(h.get_child_indices(0), [1, 2], 'correct children for 0')
        self.assertEqual(h.get_child_indices(1), [3, 4], 'correct children for 1')
        self.assertEqual(h.get_child_indices(2), [5, 6], 'correct children for 2')

    def test_get_min_for_indices(self):
        h = IndexedHeap()
        h.data = [{'key': i, 'value': i, 'index': i} for i in range(10)]

        actual = h.get_min_for_indices([9, None, None])
        self.assertEqual(actual, 9, 'no children so root is min')

        actual = h.get_min_for_indices([7, 8, 9])
        self.assertEqual(actual, 7, 'root is the smallest')

        actual = h.get_min_for_indices([2, 8, 1])
        self.assertEqual(actual, 1, 'third is the smallest')
