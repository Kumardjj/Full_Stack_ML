l=[3,-4,5,4,-1,7,-8]
n=len(l)
maxsum=-1e309
currentsum =0
for i in range(n):
    currentsum=currentsum+l[i]
    maxsum= max(currentsum,maxsum)
    if(currentsum<0):
        currentsum=0
print(maxsum)
    
