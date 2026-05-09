# pairsum :- in a sorted list.
l=[2,7,11,15]
target=int(input("enter a number: "))
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        sum=l[i]+l[j]
        if(sum == target ):
            print("indexes of elements: ",i,j)
            break

# it can also solve by two pointer approach.
l=[2,7,11,15]
target=int(input("enter a number: "))
n=len(l)
start=0
end= n-1
for i in range(start,end):
    sum = l[start]+l[end]
    if(sum>target):
        end=end-1
    elif(sum<target):
        start=start+1
    else:
        print("indexes of element:",start,end)