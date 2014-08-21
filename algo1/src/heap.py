import heapq


def heap_sort(arr):
    """ Sorts an array using a heap. """
    heapq.heapify(arr)
    out = []
    while True:
        try:
            min_value = heapq.heappop(arr)
            out.append(min_value)
        except IndexError as err:
            break
    return out

class Median(object):

    def __init__(self):
        self.h_low = []
        self.h_high = []

    def add(self, new_value):
        if len(self.h_low) > 0:
            max_low = self.h_low[-1]
        else:
            max_low = float('inf')

        if len(self.h_high) > 0:
            min_high = self.h_high[0]
        else:
            min_high = float('-inf')

        if new_value < max_low:
            heapq.heappush(self.h_low, new_value)
        else:
            heapq.heappush(self.h_high, new_value)

        if len(self.h_low) > len(self.h_high) + 1:
            extra = heapq.heappop(self.h_low)
            heapq.heappush(self.h_high, extra)

        if len(self.h_high) > len(self.h_low) + 1:
            extra = heapq.heappop(self.h_high)
            heapq.heappush(self.h_low, extra)

        if (len(self.h_low) > len(self.h_high)):
            return self.h_low[-1]
        else:
            return self.h_high[0]
