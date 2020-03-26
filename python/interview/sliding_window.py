def  characterReverse( input):
    n = len(input)
    output = ''
    count_t = 0
    count_h = 0
    for i in range(n):
        a = input[i]
        if i == n-1:
            b = None
        else:
            b = input[i+1]
        if a == 't' and b == 't':
            count_t += 1
        if a == 't' and b == 'h':
            count_t += 1
        if a == 'h' and b == 'h':
            count_h += 1
        if a == 'h' and b == 't':
            count_h += 1
        if a == 't' and b != 't' and b != 'h':
            count_t += 1
        if a == 'h' and b != 't' and b != 'h':
            count_h += 1
        if a != 't' and a != 'h':
            output += 'h'*count_h + 't'*count_t + a
            count_h = 0
            count_t = 0
    return output

#print characterReverse('theatre')


def solution(A):
    counts = {}
    for num in A:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    (most_frequent_num, __) = max(counts.iteritems(), key=lambda kv: kv[1])
    return most_frequent_num

#print solution([20, 10, 30, 30, 40, 10])


def solution(A):
    # Compute M, average value.
    M = sum(A)/len(A)
    (max_deviation_index, __) = \
            max(enumerate(A), key=lambda index_number: abs(M - index_number[1]))
    return max_deviation_index

#print solution([9, 4, -3, -10])


class SlidingWindow(object):
    """ Data structure which maintains a sliding window on top of the input arr.

    Attrs:
        arr: list, of integers, the input array on which to trace the sliding window.
        start: integer, index of the start of the sliding window.
        end: integer, index of the end of the sliding window.
        diff_start: number, difference between the first two elements in the sliding window.
        diff_end: number, difference between the last two elements in the sliding window.
    """
    def __init__(self, arr):
        if len(arr) < 3:
            raise Exception("Input array too short")
        self.arr = arr
        self.start = 0
        self.end = 2
        self.diff_start = self.arr[1] - self.arr[0]
        self.diff_end = self.arr[2] - self.arr[1]

    def inc_right(self):
        """ Increases the size of the sliding window to the right of the array.
        Also maintains diff_end.

        Raises:
            Exception, if the increase gets beyond the array bounds.
        """

        if self.end + 1 == len(self.arr):
            raise Exception('Cannot increment to the right, end of array found')
        self.end += 1
        self.diff_end = self.arr[self.end] - self.arr[self.end - 1]

    def shrink_left(self):
        """ Shrinks the sliding window to the left of the array.
        Also maintains diff_start.

        Raises:
            Exception, when the window gets below two elements.
        """
        if self.start +1 == self.end:
            raise Exception('Cannot shrink sliding window below two elems')
        self.start += 1
        self.diff_start = self.arr[self.start + 1] - self.arr[self.start]

    def is_arithmetic(self):
        """ Checks if the slice encased in the sliding window is arithmetic by
        comparing diff_start and diff_end. It is the responsability of the
        client to call this method at appropriate times! TODO improve this!
        """
        return self.diff_start == self.diff_end

    def end_reached(self):
        """ Returns True if the end of the subject array was reached. """
        return self.end == len(self.arr) - 1

    def window_size(self):
        """ Returns the size of the current sliding window. """
        return self.end - self.start

def solution(A):
    """ The solution """
    if len(A) < 3:
        return 0 # No arithmetic slices with less than three elements.

    sw = SlidingWindow(A)
    count_slices = 0

    while not sw.end_reached():
        if sw.is_arithmetic():
            count_slices += 1
            sw.inc_right()
        else:
            sw.shrink_left()
            if sw.window_size() < 2:
                sw.inc_right()

    while sw.window_size() >= 2:
        if sw.is_arithmetic():
            count_slices += 1
        sw.shrink_left()

    return count_slices

#print solution([1,2]) # 0
#import pdb; pdb.set_trace()
#print solution([1,3,5,7,9]) # 5
#print solution([1,1,2,5,7]) # 0
#print solution([-1,1,3,3,3,2,1,0]) # 5
