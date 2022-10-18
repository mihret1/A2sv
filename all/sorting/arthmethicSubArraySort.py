class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        store=[]
        bool=False
        for i in range(len(l)):
            data=nums[l[i]:r[i]+1]
            data.sort()
            for i in range(len(data)-1):
                if (data[1]-data[0])==(data[i+1]-data[i]):
                    bool=True
                else:
                    bool=False
                    break
            store+=[bool]
            return(store)
