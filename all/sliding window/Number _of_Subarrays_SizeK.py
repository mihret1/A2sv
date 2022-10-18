class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        n=len(arr)
        sum_of_k=0
        
        for i in range(k):
            sum_of_k +=arr[i]
        avg=sum_of_k/k
        
        if(avg>=threshold):
            ans +=1
        l =[sum_of_k]
        
        for i in range(1,   n-k +1):
            sum_of_k -=arr[i-1]
            sum_of_k +=arr[i+k-1]
            l.append(sum_of_k)
            if((sum_of_k/k)>=threshold):
                ans +=1
        return ans
