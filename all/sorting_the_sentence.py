class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        string = []
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j][-1] > arr[j + 1][-1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
        for i in range(len(arr)):
            x = arr[i][-1]
            a = arr[i].replace(x, "")
            string.append(a) 
        return " ".join(string)
