# insertion sort:-
#insertion sort is basically a sorting technique.

arr= [7,4,2,3,5]
n=len(arr)
for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print(arr)
        

