l=[1,2,2,1,1]
n=len(l)
freq=0
ans=0
for i in range(n):
    if freq== 0:
        ans= l[i]
        fre=1
    else:
        if(ans == l[i]):
            freq=freq+1
        else:
            freq=freq-1
print(ans)


