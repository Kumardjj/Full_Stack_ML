# Selection sort :- it is a simple sorting algorithm. It works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element until the entire list is sorted.
lst = [3,4,1,2,6] 
n=len(lst)
for i in range(0,n-1):
    min_index=i
    for j in range(i+1,n):
        if(lst[j]<lst[min_index]):
            min_index=j
    lst[i],lst[min_index]=lst[min_index],lst[i]
print(lst)
