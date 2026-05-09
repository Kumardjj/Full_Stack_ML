l=[3,-4,5,4,-1,7,-8]
n=len(l)
maxsum=-1e309
for st in range(n):
    currentsum=0
    for end in range(st,n):
        currentsum = currentsum+l[end]
        maxsum = max(currentsum,maxsum)
print(maxsum)