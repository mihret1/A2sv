class Solution:
    def compress(self, chars: List[str]) -> int:
        store=[]
    
        counter=1
        endc=1
        start=0
        end=len(chars)-1
        while start!=end:
            print(start,chars[start],end,chars[end])
            # print("ermias")
            if chars[start]==chars[start+1]:
                # print('ermia',chars[start])
                counter+=1
               
            else:
                store.append(chars[start])
                store.append(str(counter))
                counter=0
          
            start+=1
            # end-=1
            if chars[end]==chars[end-1]:
                # print(chars[end])
                endc+=1
               
            else:
                store.append(chars[end])
                store.append(str(endc))
                endc=0
            end-=1
        if chars[start]==chars[end]:
            store.append(chars[start])
            store.append(str(counter))
        print(store,chars[end])
        print(store)
        return " ".join(store)
            
            
