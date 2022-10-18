class  Solution(object):
    def maxSumTwoNoOverlap(self,nums,firstLen ,secondlen):
        first_round=min(firstLen,secondlen)
        second_round=max(firstLen, secondlen)
        first_index_store=[0]*first_round
        result=[0,0]
        i=0
        while i<len(nums)-first_round+1:
            sum=0
            for j in range(first_round):
                sum+=nums[j+i]
                
            
            if sum>(result[0]):
                result[0]=sum
                for k in range(first_round):
                    first_index_store[k]=i+k
            i+=1
        i=0
        while i<len(nums)-second_round+1:
            sum=0
            j=0
            while j <(second_round):
                if (j+i) not in first_index_store:
                    sum+=nums[j+i]
                    j+=1
                else:    
                    j=second_round
            
            if sum>(result[1]):
                result[1]=sum 
            i+=1
                
            
                    
        return(result[0]+result[1])
                
c=Solution()
c.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3)
