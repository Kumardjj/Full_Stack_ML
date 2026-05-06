#bubble sort :- it is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
lst = [7,4,8,5,3]
n=len(lst)
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if(lst[j+1]<lst[j]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)