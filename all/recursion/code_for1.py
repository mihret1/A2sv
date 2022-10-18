def changeToOne_Zero(self,n,l,r):
    stack=[n]
    i=0
    count=0
    temp=stack[0]
    while i<=len(stack):
        while temp!=0 and temp!=1: 
            stack.insert(i, temp//2)
            stack.insert(i+1, temp%2)
            stack[i+2]=temp//2
            temp=int(stack[i])
            while temp==0 or temp==1 and i<len(stack)-1:
                i+=1
                temp=stack[i]
        i+=1
    for i in range(l,r+1):
        if stack[i]==1:
            count+=1     
    print( count)
