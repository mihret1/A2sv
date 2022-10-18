class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans, start = 0, None
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1] and (i == 1 or arr[i-2] >= arr[i-1]):
                start = i -1
            elif arr[i] == arr[i-1]:
                start = None
                
            elif arr[i] < arr[i-1] and start is not None:
                ans = max(ans, i-start+1)
                
        return ans
