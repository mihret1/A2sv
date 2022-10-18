class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        
    def findMedian(self) -> float:
        self.nums.sort()
        mid = len(self.nums)//2
        if len(self.nums) % 2 == 0:
            mid1 = mid-1
            total = self.nums[mid] + self.nums[mid1]
            return total/2
        return self.nums[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
