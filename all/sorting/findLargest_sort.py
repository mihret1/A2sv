class Solution(object):
    def kthLargestNumber(self, nums, k):
        data=[]
        for i in nums:
            data+=[int(i)]
        data.sort()  # i can use my own sorting algorithm too
        return str(data[len(nums)-k])
