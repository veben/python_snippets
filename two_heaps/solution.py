from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        # Initialize two heaps: small to store the smaller half as a max heap
        # and large to store the larger half as a min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If large heap is not empty and the number is greater than the smallest number in large heap,
        # push it to the large heap. Otherwise, push the negation of the number to the small heap.
        if len(self.large) == 0 or -self.large[0] >= num:
            heappush(self.large, -num)
        else:
            heappush(self.small, num)

        # Balance the heaps by adjusting their sizes if necessary
        if len(self.large) > len(self.small) + 1:
            heappush(self.small, -heappop(self.large))
        elif len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        # If sizes of both heaps are equal, return the average of the maximum element in the small heap
        # and the minimum element in the large heap
        if len(self.large) == len(self.small):
            return (-self.large[0] + self.small[0]) / 2.0
        else:
            return -self.large[0]
