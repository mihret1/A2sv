class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictionary={}
        counter = 0

        for i in nums:
            if i in dictionary:
                counter += dictionary[i]
                dictionary[i] += 1

            else:
                dictionary[i] = 1

        return counter

    #Time complexity = o(n)
#     space:O(1)
